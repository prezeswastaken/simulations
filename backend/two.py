class AlgorithmTwo:
    def __init__(self, m, x0):
        self.m = m
        self.x0 = x0

    def get_middle_chars(self, s, n):
        if len(s) % 2 == 0 and n <= len(s):
            start = len(s) // 2 - n // 2
            end = start + n
            return s[start:end]

    def run(self, n):
        m = self.m
        x0 = self.x0

        if int(x0) <= 0:
            print("X0 must be bigger than 0!")
            exit(-1)

        results = []

        for i in range(n):
            x0: str = str(int(x0) * int(x0))
            while len(x0) < 2 * m:
                x0 = f"0{x0}"
            x0 = self.get_middle_chars(x0, m)
            results.append(int(x0))
            # print(f"Result for n = {i+1}: {x0}")
        return results
