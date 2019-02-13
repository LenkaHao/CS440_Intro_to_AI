## Problem Definition
In this assignment, we are trying to:
- Understand how neural networks work
- Implement a simple neural network
- Understand how different parameters would influence a neural network


## Method and Implementation
- compute_cost: This function computes the total cost on the dataset.
- predict: This function makes a prediction based on current model parameters.
- fit: This function trains the model on the dataset.
  - This function uses backpropagation and gradient descent to train the model.
  - It uses hyperbolic tangent function as activation function.
- We use L2 regularization to deal with overfitting. We use cross-validation to test the perforamnce of L2 regularization.


## Experiments
Our experiments include:
- Neural nets with no hidden layer (Logistic regression)
  - Training and testing on linear decision boundary
  - Training and testing on non-linear decision boundary
- Neural nets with one hidden layer
  - Training and testing on linear decision boundary
  - Training and testing on non-linear decision boundary
    - with different learning rates: learning rate = 0.001, 0.01, 0.1, 0.2
    - with different number of nodes in the hidden layer: n = 4, 2, 1, 50
    - with L2 regularization
      - We split our dataset into 4 groups, and by using the concept of cross-validation, we use each group as testing data and the rest of it as training data, and get the average accuracy of all four testing data.
- Neural nets to recognize digits
Evaluation metrics:
- Accuracy
- Cost


# Results
Source images

![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/source_linear.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/source_non_linear.png)

Logistic regression on linear and non-linear decision boundary

![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/logistic_regression_linear.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/logistic_regression_non_linear.png)
 
A neural network with one hidden layer on linear and non-linear decision boundary

![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/nn_linear.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/nn_nonlinear.png)
 
A neural network with one hidden layer on different learning rates

![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/learning_rate_1.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/learning_rate_2.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/learning_rate_3.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/learning_rate_4.png)
   
A neural network with one hidden layer with different number of nodes

![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/node_1.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/node_2.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/node_3.png)
![Source](https://github.com/LenkaHao/CS440_Intro_to_AI/blob/master/Neural%20Nets/img/node_4.png)
   
A neural net with L2 regularization (using k=4 cross validation)
Average accuracy
- Linear dataset
  - Before using L2	0.93
  - After using L2	0.942
- Non-linear dataset
  - Before using L2	0.96
  - After using L2	0.962

A neural net to recognize digits
- Accuracy: 0.94     Cost: 0.25


## Discussion and conclusion

Question 3: Can your 3-layer neural network model (with one hidden layer) learn non-linear decision boundaries? Why or why not?

According to the diagram, a neural netwrok with one hidden layer can learn non-linear decision boundaries
Reason: The output is non-linear because there are interactions among the weights via the hidden layer.

Question 6: What is overfitting and why does it occur in practice? Name and briefly explain 3 ways to reduce overfitting.

Overfitting is a modeling error which occurs when a function is too closely fit to a particuar set of data points, and may therefore fail to fit additional data or predict future observations reliably.
Overfitting occurs when a learning model customizes itself too much to describe the relationship between training data and the labels. It occurs when number of epochs is too high, and parameters (for a neural net it can be the number of nodes in the hidden layers) are too many.

Ways to reduce overfitting (see credits and bibliography)
- Use "wrapper" to enumerate models h according to model size (e.g., number of nodes in neural net h). Select model with smallest error.
- Feature selection: Simplify model by discarding irrelevant attributes (dimensionality reduction).
- Minimum description length: Select model with smallest number of bits required to encode program and data.

Question 7: One common technique used to reduce overfitting is L2 regularization. How does L2 regularization prevent overfitting? Implement L2 regularization. How differently does your model perform before and after implementing L2 regularization?

Regularization adds a regularization term in order to prevent the coefficients to fit so perfectly to overfit. For L2 regularization, it adds "squared magnitude" of coefficient as penalty term to the loss function, and decreases the change of the weights in each iteration.
See the accuracy above

As we can see, the average accuracy of testing data slightly increases after applying L2 regularization for both linear and non-linear dataset. The reason the increments are so small is that our datasets are good enough to avoid overfitting. The increment of accuracy would be larger if we use other datasets.


## Credits and Bibliography
Boston University Department of Computer Science, CS440, Professor Betke

This project is contributed by Jiatong Hao and Xianhui Li

