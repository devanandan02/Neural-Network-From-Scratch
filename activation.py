import numpy as np

class TanhActivation:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.tanh(inputs)
        return self.output

    def backward(self, error):
        return error * (1 - np.square(self.output))

class SoftmaxActivation:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        return probabilities

    def backward(self, error):
        return error