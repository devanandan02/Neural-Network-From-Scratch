<h3>Basic Deep Learning Steps</h3>
<br>
1. Feed input -> Data flow from layer to layer -> Retrieve output
<br>
2. Calculate the error (cost function/ loss function)
<br>
3. Adjust the parameter using the optimization function so to reduce the error
<br>
4. Repeat again until the error is minimized
<br><br>
The important step is 3 because it's where the learning happens
<br><br>
<h3>Terms</h3>
Layer : Layers are like different levels of processing that information goes through. There are 3 types of layers input layer, hidden layers, and output layer.
<br><br>
Forward Propogation : It is a process of receiveing weighted input, transforms it with a set of mostly non-linear functions and then passes these values as output to the next layer.
<br><br>
Backward Propogaation : It is the process that adjusts the weights of the network's connections in order to minimize the difference between the predicted output and the actual target values.
<br><br>
Dense Layer : It connects n input neurons to a set of m output neurons. The value of n is the number of features and m is the numbers of classes for classification problem and for regression m = 1. Dense layer is a fully connected layer
<br><br>
Activation Layer : It refers to the application of an activation function to the output of a neuron or a group of neurons in a neural network layer. Activation functions introduce non-linearities into the network, enabling it to learn complex patterns in the data.
<br><br>
Loss Function : It is a mathematical function to calculate the difference between predicted output and actual target value. It helps to quantify how well the model performed. It is also called cost function.
<br><br>
Learning Rate : The learning rate is a hyperparameter that controls how much to change the model in response to the estimated error each time the model weights are updated.
<br><br>
Epochs : An epoch refers to one complete cycle through the entire training dataset. During each epoch, the neural network processes every training example once and updates the model's parameters (weights and biases) based on the computed errors.
<br><br>
StandardScaler : It is a preprocessing technique used in machine learning to standardize the features of a dataset. It scales the features such that the distribution of each feature has a mean value of 0 and a standard deviation of 1.
<br><br>
Label encoding : It is a technique used to convert categorical data into numerical format. Based on the type of data different label encoding techniques are used.
<br><br>
Evaluation metrics : They are measures used to assess the performance of machine learning models. These metrics help quantify the quality of the model's predictions and provide valuable insights into how well the model is performing on a specific task. 
