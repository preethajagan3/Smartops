import multiprocessing
import os
import time

def burn():
    print(f"🔥 CPU stress process started | PID={os.getpid()}")
    while True:
        pass  # infinite loop = max CPU usage

if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count()
    print(f"⚠️ Launching CPU stress on {cpu_count} cores")

    processes = []
    for _ in range(cpu_count):
        p = multiprocessing.Process(target=burn)
        p.start()
        processes.append(p)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Stress stopped manually")
        for p in processes:
            p.terminate()
