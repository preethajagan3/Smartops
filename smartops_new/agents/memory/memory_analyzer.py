class MemoryAnalyzer:
    def __init__(self):
        self.counter = 0

    def analyze(self, mem, threshold):
        if mem > threshold:
            self.counter += 1
        else:
            self.counter = 0
        return self.counter
