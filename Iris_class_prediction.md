<h3>Code Explanation</h3>
The Iris_class_prediction file implements a neural network with an input layer, one hidden layer and an output layer to classsify the iris dataset.
<br><br>
The steps involved are<br><br>
1.Data Loading<br>
2.Data Preprocessing<br>
3.Neural Network Architecture<br>
4.Training<br>
5.Prediction<br>
6.Accuracy Calculation<br>
<br>
A few things to note:
<br><br>
<ul>
<li>The number of hidden node is set to 8.<li>
<li>The learning rate (learning_rate) is set to 0.01.</li>
<li>The number of epochs is set to 1000. Depending on the problem, you might need more or fewer epochs for training.</li>
<li>The loss function used is categorical cross-entropy since it is a multi-class classification problem.</li>
<li>The number of hidden node, learning rate and number of epochs are hyperparameter that can be tuned for better performance</li>
</ul>
<br><br>
<h3>Data</h3>
<br><br>
The data used is iris data set which contains 4 features and based on the features it is classified into 3 classes.
<br>
The features are are standardized to have mean as 0 and standard deviation as 1.
<br>
The labels are encode using one hot encoding, which represent a categorical variable as a group of binary variables, where each binary variable represents one category.
<br>
The feature(X variable) and classes(Y variable) are splitted into two sets in the ratio 8:2, i.e., 80% for training and 20% for testing.(The splitted data are X_train,X_test,Y_train, and Y_test)
<br><br>
<h3>Training Process</h3>
<br><br>
This process repeats for 1000 times as we initialized the value of epoch as 1000.
<br><br>
<h3>Evaluation</h3>
<br><br>
The model has attained an accuracy of 93.33%. By proper tuning of hyperparameters we can increase the accuracy.

