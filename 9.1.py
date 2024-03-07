x0: float = float(input("Enter x0 (it must be a number between 0 and 1): "))

if x0 <= 0 or x0 >= 1:
    print("X0  out of given bounds!")
    exit(-1)

a = 4
m = 9

# We make results a set instead of a list, to ignore any duplicates
results = set()


def calculate(n: int):
    # This shouldn't ever be called
    if n < 0:
        print("N < 0, something definitely went wrong :(")
        exit(-1)

    # Value for Xn when n = 0
    if n == 0:
        return x0

    # Value for Xn when n >= 1
    result = a * calculate(n - 1) % m
    results.add(result)
    # print(f"Result for n = {n}: {result}\n")
    return result


calculate(100)
print(f"Generated {len(results)} results:\n{results}")
