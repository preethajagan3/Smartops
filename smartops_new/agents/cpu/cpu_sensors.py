import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_top_process():
    processes = sorted(
        psutil.process_iter(['pid', 'name', 'cpu_percent']),
        key=lambda p: p.info['cpu_percent'],
        reverse=True
    )
    return processes[0] if processes else None
