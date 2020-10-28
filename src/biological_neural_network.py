import sys
sys.path.append('graphs')
from directed_graph import DirectedGraph

class BiologicalNeuralNetwork(DirectedGraph):
	def __init__(self, values, edges):
		super().__init__(edges, values)
		self.neurons = values
		self.synapses = edges

	def get_derivatives(self):
		print([lambda t,x: derivative(t,x[4*i:4*i+4]) + x[0] if j == 0 else derivative(t,x[4*i:4*i+4]) for i, node in enumerate(self.nodes) for j, derivative in enumerate(node.value.derivatives)])
		return [lambda t,x: derivative(t,x[4*i:4*i+4]) + x[0] if j == 0 else derivative(t,x[4*i:4*i+4]) for i, node in enumerate(self.nodes) for j, derivative in enumerate(node.value.derivatives)]
    
	def get_starting_point(self): 
		print((0, [position for i, node in enumerate(self.nodes) for position in node.value.initial_positions[1]]))
		return (0, [position for i, node in enumerate(self.nodes) for position in node.value.initial_positions[1]])
