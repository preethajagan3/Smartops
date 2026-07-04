import time
import psutil   # ✅ REQUIRED

from smartops_new.common.logger import get_logger
from smartops_new.core.shared_state import STATE, LOCK

from .disk_config import DISK_THRESHOLD, DISK_DURATION, CHECK_INTERVAL
from .disk_analyzer import DiskAnalyzer
from .disk_actions import clean_disk


# ---------------- LOGGER ----------------
log = get_logger("DISK_AGENT", "logs/disk.log")

# ---------------- ANALYZER ----------------
analyzer = DiskAnalyzer()

log.info("Disk Agent Started")

# ---------------- AGENT LOOP ----------------
while True:
    # Get disk usage
    disk = psutil.disk_usage('/').percent

    # Analyze against threshold
    count = analyzer.analyze(disk, DISK_THRESHOLD)

    # Update shared state for dashboard
    with LOCK:
        STATE["disk"] = disk

    # Real-time log (console + file)
    log.info(f"DISK={disk}%")

    # Threshold breach → action
    if count >= DISK_DURATION:
        clean_disk()
        log.warning(f"DISK HIGH | {disk}%")

        with LOCK:
            STATE["alerts"].append("Disk high")

        analyzer.counter = 0

    time.sleep(CHECK_INTERVAL)
