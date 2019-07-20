import NeuralNetwork
import numpy

# number of input, hidden, output nodes
input_nodes = 3
output_nodes = 3
hidden_nodes = 3

# learning rate is 0.3
learning_rate = 0.3

# create an instance of a Neural Network
n = NeuralNetwork.NeuralNetwork(input_nodes, output_nodes, hidden_nodes, learning_rate)
print(numpy.random.rand(3, 3) - 0.5)
