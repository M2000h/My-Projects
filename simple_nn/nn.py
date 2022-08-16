from typing import List
import random


class Layer:
    def __init__(self, size: int):
        self.size = size
        self.neurons = [0.] * size
        self.biases = [0.] * size
        self.weights = []


class NeuralNetwork:
    def __init__(self, learningRate: float, activation, derivative, sizes: List[int]):
        self.learningRate = learningRate
        self.activation = activation
        self.derivative = derivative
        self.layers = []
        for i in range(len(sizes)):
            nextSize = 0
            if i < len(sizes) - 1:
                nextSize = sizes[i + 1]
            self.layers.append(Layer(sizes[i]))
            for j in range(sizes[i]):
                self.layers[i].biases[j] = random.random() * 2.0 - 1.0
                self.layers[i].weights.append([])
                for k in range(nextSize):
                    self.layers[i].weights[j].append(random.random() * 2.0 - 1.0)

    def feedForward(self, inputs: List[float]) -> List[float]:
        self.layers[0].neurons = inputs
        for i in range(1, len(self.layers)):
            l = self.layers[i-1]
            l1 = self.layers[i]
            for j in range(l1.size):
                l1.neurons[j] = 0
                for k in range(l.size):
                    l1.neurons[j] += l.neurons[k] * l.weights[k][j]
                l1.neurons[j] += l1.biases[j]
                l1.neurons[j] = self.activation(l1.neurons[j])
        return self.layers[-1].neurons

    def backpropagation(self, targets: List[float]):
        errors = []
        for i in range(self.layers[-1].size):
            errors.append(targets[i] - self.layers[-1].neurons[i])
        for k in range(len(self.layers) - 2, -1, -1):
            l = self.layers[k]
            l1 = self.layers[k + 1]
            errorsNext = [0]
            gradients = []
            for i in range(l1.size):
                gradients.append(errors[i] * self.derivative(self.layers[k + 1].neurons[i]))
                gradients[i] *= self.learningRate
            deltas = []
            for i in range(l1.size):
                deltas.append([])
                for j in range(l.size):
                    deltas[i].append(gradients[i] * l.neurons[j])
            for i in range(l.size):
                errorsNext.append(0)
                for j in range(l1.size):
                    errorsNext[i] += l.weights[i][j] * errors[j]

            errors = errorsNext
            weightsNew = []
            for i in range(l.size):
                weightsNew.append([])
                for j in range(l1.size):
                    weightsNew[i].append([])

            for i in range(l1.size):
                for j in range(l.size):
                    weightsNew[j][i] = l.weights[j][i] + deltas[i][j]
            for i in range(l1.size):
                for j in range(l.size):
                    weightsNew[j][i] = l.weights[j][i] + deltas[i][j]

            l.weights = weightsNew
            for i in range(l1.size):
                l1.biases[i] += gradients[i]
