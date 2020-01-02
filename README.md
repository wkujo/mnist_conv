# mnist_conv
Basic "Hello World" convolutional neural network 

Using the standard MNIST clothing dataset, achieve 99.8% accuracry in objection recognition. 

ConvNet:
  1. 2D (relu-activated) conv layer followed by max pooling
  2. 128-unit (relu-activated) fully connected layer
  3. 10-unit softmax output layer

Using Adam for optimization, model will continue learning for 20 epochs (or likely exit early due to the 99.8% accuracy threshold on the callback). 
