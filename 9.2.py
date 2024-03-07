def get_middle_chars(s, n):
    if len(s) % 2 == 0 and n <= len(s):
        start = len(s) // 2 - n // 2
        end = start + n
        return s[start:end]
    else:
        return "Invalid input. Ensure string length is even and n is less than or equal to string length."


x0 = input("Enter x0: ")

if int(x0) <= 0:
    print("X0 must be bigger than 0!")
    exit(-1)

m = 4
n = 100

results = set()

for i in range(n):
    x0: str = str(int(x0) * int(x0))
    while len(x0) < 2 * m:
        x0 = f"0{x0}"
    x0 = get_middle_chars(x0, m)
    print(f"Result for n = {i+1}: {x0}")
