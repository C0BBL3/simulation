from src.euler_estimator import EulerEstimator
from src.biological_neuron import BiologicalNeuron
from analysis.three_neuron_network import BiologicalNeuralNetwork
import matplotlib.pyplot as plt


print('\nTesting...\n')


def electrode_voltage(t):
    if t in [10,11,20,21,30,40,50,51,53,54,56,57,59,60,62,63,65,66]: return 50
    else: return 0

neuron_0 = BiologicalNeuron(stimulus=electrode_voltage)
neuron_1 = BiologicalNeuron()
neuron_2 = BiologicalNeuron()
neurons = [neuron_0, neuron_1, neuron_2]
synapses = [(0, 1), (1, 2)]
network = BiologicalNeuralNetwork(neurons, synapses)
euler = EulerEstimator(
    derivatives=network.get_derivatives(),
    start_point=network.get_starting_point()
)
plt.plot([n/2 for n in range(160)], [electrode_voltage(n/2) for n in range(160)])
euler.plot([0, 80], stepsize=0.001)
