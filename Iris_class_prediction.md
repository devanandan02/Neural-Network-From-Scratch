<h3>Code Explanation</h3>
The Iris_class_prediction file implements a neural network with an input layer, one hidden layer and an output layer to classsify the iris dataset.
<br><br>
The steps involved are<br>
1.Data Loading<br>
2.Data Preprocessing<br>
3.Neural Network Architecture<br>
4.Training<br>
5.Prediction<br>
6.Accuracy Calculation<br>
<br>
A few things to note:
<ul>
<li>The number of hidden node is set to <b>8</b>.</li>
<li>The learning rate is set to <b>0.01</b>.</li>
<li>The number of epochs is set to <b>1000</b>. Depending on the problem, you might need more or fewer epochs for training.</li>
<li>The loss function used is categorical cross-entropy since it is a multi-class classification problem.</li>
<li>The number of hidden node, learning rate and number of epochs are hyperparameter that can be tuned for better performance</li>
</ul>
<br>
<h3>Data</h3>
The data used is iris data set which contains <b>4</b> features and based on the features it is classified into <b>3</b> classes.
<br>
The features are are standardized to have mean as <b>0</b> and standard deviation as <b>1</b>.
<br>
The labels are encode using one hot encoding, which represent a categorical variable as a group of binary variables, where each binary variable represents one category.
<br>
The feature(<b>X variable</b>) and classes(<b>Y variable</b>) are splitted into two sets in the ratio <b>8:2</b>, i.e., <b>80%</b> for training and <b>20%</b> for testing.(The splitted data are <b>X_train,X_test,Y_train,</b> and <b>Y_test</b>)
<br><br>
<h3>Training Process</h3>
When we pass data to the train_neural_network function,<br><br> 
1. The <b>X varibale</b> is forward propagated through the hidden layer(dense layer), where the weights and bias is added. The weights and bias are inialized with random values and zeros respectively in the dense layer. Then it is passed through the activation and then given as the input to the output layer.
<br><br>
The activation function used here is Hyperbolic Tangent "tanh". It is a smooth, differentiable function that incorporates nonlinearity into the network which means that the output of this function is not a simple linear function of its input. The tanh function squashes its input to the range <b>[−1,1]<b>, which is zero-centered. When the outputs are zero-centered, the gradients during backpropagation do not all have the same sign. This property can help the model converge faster.
<br><br>
2. In the output layer(dense layer) the output of the tanh activation function are foward propogated, i.e., weights and bias is added, same as earlier the weights and bias are inialized with random values and zeros respectively in the dense layer. Then it is passed to the softmax activation function. And the output from softmax function is passed to the loss function.
<br><br>
3. In the loss function the loss value is calculated by using Categorical Cross-Entropy. The total loss for a dataset is the average of individual sample losses. For a batch of samples, you calculate the loss for each sample, sum them up, and then divide by the number of samples in the batch.
<br>loss = sum(true_class*log(predicted_probality))/number of X_variables<br>
<br><br>
5. After finding loss value, the goal is to reduce the loss value by adjusting the weights and biases, here comes the backward-propagation. 
<br><br>
This process repeats for <b>1000</b> times as we initialized the value of epoch as <b>1000</b>.
<br><br>
<h3>Evaluation</h3>
The model has attained an accuracy of <b>93%</b>. By proper tuning of hyperparameters we can increase the accuracy.

