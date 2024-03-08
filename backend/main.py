from one import AlgorithmOne
from two import AlgorithmTwo

calc = AlgorithmOne(a=4, m=9, x0=0.25)
calc.run(100)

calc2 = AlgorithmTwo(m=4, x0=1211)
results = calc.run(100)

for result in results:
    print(f"{result}")
