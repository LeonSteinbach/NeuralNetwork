import numpy
from NeuralNetwork import NeuralNetwork


def train(nn, training_data_list, epochs=1):
    for _ in range(epochs):
        for record in training_data_list:
            all_values = record.split(',')

            inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01
            targets[int(all_values[0])] = 0.99

            nn.train(inputs, targets)


def test(nn, test_data_list):
    scorecard = []

    for record in test_data_list:
        all_values = record.split(',')
        
        correct_label = int(all_values[0])

        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = nn.query(inputs)

        label = numpy.argmax(outputs)

        correct = label == correct_label
        confidence = round(numpy.max(outputs) * 100)
        result_text = 'RIGHT' if correct else 'WRONG'

        print(f'Correct: {correct_label}    Guess: {label}    Confidence: {confidence}%\t{result_text}')

        if (correct):
            scorecard.append(1)
        else:
            scorecard.append(0)
    
    average = sum(scorecard) / float(len(scorecard))
    print(f'\nAverage: {average}%')


if __name__ == '__main__':
    input_nodes = 784
    hidden_nodes = 100
    output_nodes = 10

    learning_rate = 0.1
    epochs = 5

    nn = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    with open('mnist_dataset/mnist_train.csv', 'r') as f:
        training_data_list = f.readlines()
    
    with open('mnist_dataset/mnist_test.csv', 'r') as f:
        test_data_list = f.readlines()
    
    train(nn, training_data_list, epochs)
    test(nn, test_data_list)
