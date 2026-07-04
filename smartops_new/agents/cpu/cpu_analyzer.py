class CPUAnalyzer:
    def __init__(self):
        self.counter = 0

    def analyze(self, cpu, threshold):
        if cpu > threshold:
            self.counter += 1
        else:
            self.counter = 0
        return self.counter
