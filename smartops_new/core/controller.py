import subprocess
import sys
import time

print("🧠 SmartOps Orchestrator Started")

agents = [
    "smartops_new.agents.cpu.cpu_agent",
    "smartops_new.agents.memory.memory_agent",
    "smartops_new.agents.disk.disk_agent",
]

for agent in agents:
    subprocess.Popen([sys.executable, "-m", agent])

while True:
    time.sleep(10)
