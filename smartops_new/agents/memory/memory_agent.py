import time
import psutil   # ✅ REQUIRED

from smartops_new.common.logger import get_logger
from smartops_new.core.shared_state import STATE, LOCK

from .memory_config import MEMORY_THRESHOLD, MEMORY_DURATION, CHECK_INTERVAL
from .memory_analyzer import MemoryAnalyzer
from .memory_actions import recover_memory


log = get_logger("MEMORY_AGENT", "logs/memory.log")
analyzer = MemoryAnalyzer()

log.info("Memory Agent Started")

while True:
    mem = psutil.virtual_memory().percent
    count = analyzer.analyze(mem, MEMORY_THRESHOLD)

    with LOCK:
        STATE["memory"] = mem

    log.info(f"MEMORY={mem}%")

    if count >= MEMORY_DURATION:
        recover_memory()
        log.warning(f"MEMORY HIGH | {mem}%")

        with LOCK:
            STATE["alerts"].append("Memory high")

        analyzer.counter = 0

    time.sleep(CHECK_INTERVAL)
