class BiologicalNeuralNetwork:
	def __init__(self, neurons, synapses):
		self.neurons = neurons
		self.synapses = synapses
		for neuron_1_index, neuron_2_index in self.synapses:
			print('self.neurons[neuron_1_index].child', self.neurons[neuron_1_index].child)
			self.neurons[neuron_1_index].child = self.neurons[neuron_2_index]
			print('self.neurons[neuron_1_index].child', self.neurons[neuron_1_index].child)
			self.neurons[neuron_2_index].parent = self.neurons[neuron_1_index]

	def get_derivatives(self):
		#print([lambda t,x: derivative(t,x[len(neuron.derivatives)*i:len(neuron.derivatives)*i]) + x[len(neuron.derivatives)*i] if j == 0 else derivative(t,x[len(neuron.derivatives)*i:len(neuron.derivatives)*i+len(neuron.derivatives)]) for i, neuron in enumerate(self.neurons) for j, derivative in enumerate(neuron.derivatives)])
		#return [lambda t,x: derivative(t,x[len(neuron.derivatives)*i:len(neuron.derivatives)*i]) + x[len(neuron.derivatives)*i] if j == 0 else derivative(t,x[len(neuron.derivatives)*i:len(neuron.derivatives)*i+len(neuron.derivatives)]) for i, neuron in enumerate(self.neurons) for j, derivative in enumerate(neuron.derivatives)]
		derivatives, current_neuron, i = [], self.neurons[0], 0
		while current_neuron.child != None:
			for j, derivative in enumerate(current_neuron.derivatives):
				if j == 0: derivatives.append(lambda t,x: derivative(t,x[len(current_neuron.derivatives)*i:len(current_neuron.derivatives)*i]) + x[len(current_neuron.derivatives)*i])
				else: derivatives.append(lambda t,x: derivative(t,x[len(current_neuron.derivatives)*i:len(current_neuron.derivatives)*i+len(current_neuron.derivatives)]))
			if current_neuron.child != None: current_neuron = current_neuron.child
			else: break
			i += 1
		print('derivatives', derivatives)
		return derivatives


	def get_starting_point(self): 
		print('starting_point', (0, [position for i, neuron in enumerate(self.neurons) for position in neuron.initial_positions[1]]))
		return (0, [position for i, neuron in enumerate(self.neurons) for position in neuron.initial_positions[1]])
