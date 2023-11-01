import numpy as np

class Dense:
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size)
        self.biases = np.zeros((1, output_size))

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights) + self.biases
        return self.output

    def backward(self, error, learning_rate):
        weights_error = np.dot(self.inputs.T, error)
        biases_error = np.sum(error, axis=0, keepdims=True)
        input_error = np.dot(error, self.weights.T)

        self.weights -= learning_rate * weights_error / len(self.inputs)
        self.biases -= learning_rate * biases_error / len(self.inputs)

        return input_error