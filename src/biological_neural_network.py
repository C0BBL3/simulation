from graphs.directed_graph import DirectedGraph

class BiologicalNeuralNetwork(DirectedGraph):
    def __init__(self, values, edges):
        super().__init__(edges, values)
        self.neurons = values
        self.synapses = edges

    def get_derivatives(self): return [lambda t,x: derivative(t,x[4*i:4*i+4]) + x[0] if j == 0 else derivative(t,x[4*i:4*i+4]) for i, node in enumerate(self.nodes) for j, derivative in enumerate(node.value.derivatives)]
    def get_starting_point(self): return self.nodes[0]
