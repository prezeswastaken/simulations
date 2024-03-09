import matplotlib.pyplot as plt


class GraphMaker:
    def __init__(self, results):
        self.results = results

    def make_graph(self):
        # Set the 'dark_background' style
        plt.style.use("dark_background")
        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot the results
        ax.plot(self.results)

        # Save the figure as an image in the ./public directory
        graph = fig.savefig("./public/graph.png")
        self.graph = graph

    def get_graph(self):
        return self.graph
        pass
