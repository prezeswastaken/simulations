class AlgorithmOne:
    def __init__(self, a, m, x0):
        self.a = a
        self.m = m
        self.x0 = x0
        self.results = set()

    def calculate(self, n):
        if n < 0:
            print("N < 0, something definitely went wrong :(")
            exit(-1)

        if n == 0:
            return self.x0

        result = self.a * self.calculate(n - 1) % self.m
        self.results.add(result)
        return result

    def run(self, n):
        self.calculate(n)
        print(f"Generated {len(self.results)} results:\n{self.results}")
        return self.results
