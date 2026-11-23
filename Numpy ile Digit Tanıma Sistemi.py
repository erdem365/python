import numpy as np


def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return x > 0

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)


def cross_entropy(y_true, y_pred):
    m = y_true.shape[0]
    return -np.sum(y_true * np.log(y_pred + 1e-9)) / m


def one_hot(y, num_classes):
    return np.eye(num_classes)[y]


class NeuralNetwork:
    def __init__(self):
        self.W1 = np.random.randn(784, 64) * 0.01
        self.b1 = np.zeros((1, 64))
        self.W2 = np.random.randn(64, 10) * 0.01
        self.b2 = np.zeros((1, 10))

    def forward(self, X):
        self.Z1 = X.dot(self.W1) + self.b1
        self.A1 = relu(self.Z1)
        self.Z2 = self.A1.dot(self.W2) + self.b2
        self.A2 = softmax(self.Z2)
        return self.A2

    def backward(self, X, y, lr=0.01):
        m = X.shape[0]
        y_onehot = one_hot(y, 10)

        dZ2 = self.A2 - y_onehot
        dW2 = self.A1.T.dot(dZ2) / m
        db2 = np.sum(dZ2, axis=0, keepdims=True) / m

        dA1 = dZ2.dot(self.W2.T)
        dZ1 = dA1 * relu_derivative(self.Z1)
        dW1 = X.T.dot(dZ1) / m
        db1 = np.sum(dZ1, axis=0, keepdims=True) / m

        self.W1 -= lr * dW1
        self.b1 -= lr * db1
        self.W2 -= lr * dW2
        self.b2 -= lr * db2

    def train(self, X, y, epochs=10):
        for i in range(epochs):
            output = self.forward(X)
            loss = cross_entropy(one_hot(y, 10), output)
            self.backward(X, y)

            print(f"Epoch {i}, Loss: {loss:.4f}")


X = np.random.rand(1000, 784)
y = np.random.randint(0, 10, 1000)


model = NeuralNetwork()
model.train(X, y, epochs=10)
