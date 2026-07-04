class DiskAnalyzer:
    def __init__(self):
        self.counter = 0

    def analyze(self, disk, threshold):
        if disk > threshold:
            self.counter += 1
        else:
            self.counter = 0
        return self.counter
