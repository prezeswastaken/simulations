from one import AlgorithmOne
from two import AlgorithmTwo
from graph_maker import GraphMaker

calc = AlgorithmOne(a=4, m=9, x0=0.25)
calc.run(100)

# calc2 = AlgorithmTwo(m=4, x0=1211)
calc2 = AlgorithmTwo(m=4, x0=1212)
results = calc2.run(100)

graph = GraphMaker(results)
graph.make_graph()

for result in results:
    print(f"{result}")
