import threading
from collections import deque

STATE = {
    "cpu": [],
    "memory": [],
    "disk": [],
    "alerts": deque(maxlen=10),
    "logs": deque(maxlen=50)
}

LOCK = threading.Lock()
