# Handwritten Digit Recognition using Neural Network
This is a simple implementation of a neural network to recognize handwritten digits from the MNIST dataset. The neural network is implemented in Python using the NumPy and SciPy libraries.

## Usage
Run the main.py file to train and test the neural network:

```python main.py```

By default, the neural network is trained for 5 epochs with a learning rate of 0.1. You can change these parameters by editing the corresponding variables in the main.py file.

## Neural Network Architecture
The neural network has an input layer of 784 nodes (corresponding to the 28x28 pixel images in the MNIST dataset), a hidden layer of 100 nodes, and an output layer of 10 nodes (corresponding to the digits 0-9).

The activation function used in the hidden and output layers is the sigmoid function, implemented using the SciPy ```expit``` function.

## Results
After training the neural network on the MNIST dataset, it achieves an accuracy of around 95% on the test set.

During testing, the neural network outputs its guess for each digit, along with the confidence of the guess and whether it was correct or not.
