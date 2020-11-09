class BiologicalNeuralNetwork:
    def __init__(self, neurons, synapses):
        self.neurons = neurons
        self.synapses = synapses
        for neuron_1_index, neuron_2_index in self.synapses:
            self.neurons[neuron_1_index].child = self.neurons[neuron_2_index]

    def get_derivatives(self, delay = 2):
        derivatives, current_neuron, neuron_index = [], self.neurons[0], 0
        while True:
            num_derivatives = len(current_neuron.derivatives)
            for derivative_index, derivative in enumerate(current_neuron.derivatives):
                if derivative_index == 0 and neuron_index > 0: derivatives.append(lambda t, x, neuron_index=neuron_index, derivative=derivative: derivative(t - (2 * neuron_index), x[num_derivatives*neuron_index:(num_derivatives+1)*neuron_index])+ x[num_derivatives*(neuron_index-1)])
                else: derivatives.append(lambda t, x, neuron_index=neuron_index, derivative=derivative: derivative(t - (2 * neuron_index), x[num_derivatives*neuron_index:(num_derivatives+1)*neuron_index]))
            if current_neuron.child != None: current_neuron = current_neuron.child
            else: break
            neuron_index += 1
        return derivatives

    def get_starting_point(self):
        return (0, [position for i, neuron in enumerate(self.neurons) for position in neuron.initial_positions[1]])
