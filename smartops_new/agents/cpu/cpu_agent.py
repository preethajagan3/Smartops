import time
import os
import signal

from smartops_new.common.logger import get_logger
from smartops_new.core.shared_state import STATE, LOCK

from .cpu_config import CPU_THRESHOLD, CPU_DURATION, CHECK_INTERVAL
from .cpu_sensors import get_cpu_usage, get_top_process
from .cpu_analyzer import CPUAnalyzer


log = get_logger("CPU_AGENT", "logs/cpu.log")
analyzer = CPUAnalyzer()

log.info("CPU Agent Started")

while True:
    cpu = get_cpu_usage()   # ✅ now defined
    count = analyzer.analyze(cpu, CPU_THRESHOLD)

    # Update dashboard state
    with LOCK:
        STATE["cpu"] = cpu

    # Real-time console + file log
    log.info(f"CPU={cpu}%")

    if count >= CPU_DURATION:
        proc = get_top_process()
        if proc:
            os.kill(proc.pid, signal.SIGTERM)
            log.warning(
                f"CPU THROTTLED | {proc.info['name']} | {cpu}%"
            )

        with LOCK:
            STATE["alerts"].append("CPU throttled")

        analyzer.counter = 0

    time.sleep(CHECK_INTERVAL)
