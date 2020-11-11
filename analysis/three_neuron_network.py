class BiologicalNeuralNetwork:
    def __init__(self, neurons, synapses):
        self.neurons = neurons
        for i, neuron in enumerate(neurons):
            neuron.index = i
        self.synapses = synapses
        for neuron_1_index, neuron_2_index in self.synapses:
            self.neurons[neuron_2_index].parent = self.neurons[neuron_1_index]

    def get_derivatives(self, delay=2):
        derivatives, current_neuron, neuron_index = [], self.neurons[-1], 0
        for current_neuron in self.neurons[::-1]:
            num_derivatives = len(current_neuron.derivatives)
            for derivative_index, derivative in enumerate(current_neuron.derivatives):
                if derivative_index == 0 and neuron_index > 0:
                    derivatives.append(
                        lambda t, x, neuron_index=current_neuron.index, derivative=derivative:
                            derivative(t, x[num_derivatives*current_neuron.index:num_derivatives*current_neuron.index 
                            + num_derivatives]) + x[num_derivatives*current_neuron.parent.index] 
                            if x[num_derivatives*current_neuron.parent.index] > 50
                            else derivative(t, x[num_derivatives*current_neuron.index:num_derivatives*current_neuron.index + num_derivatives]))
                else:
                    derivatives.append(
                        lambda t, x, neuron_index=neuron_index, derivative=derivative:
                            derivative(t, x[num_derivatives*current_neuron.index: num_derivatives*current_neuron.index + num_derivatives]))
        return derivatives

    def get_starting_point(self):
        return (0, [position for i, neuron in enumerate(self.neurons) for position in neuron.initial_positions[1]])
