import numpy as np
import tensorflow as tf
from tensorflow.models.rnn import rnn, rnn_cell
from BiRNN import BiRNN
from data_handler import pull_data_chunk

learn_rate = 0.001
training_iterations = 10000
log_frequency = 100

n_hidden = 64
n_classes = 36

x = tf.placeholder("float", [None, n_steps, n_input])
y = tf.placeholder("float", [None, n_classes])

weights = {
    'out': tf.Variable(tf.random_normal([2*n_hidden, n_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([n_classes]))
}

pred = BiRNN(x, weights, biases)
#print pred

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init)
	step = 1
	while step < training_iterations:
		xtrain, ytrain = pull_data_chunk()
		sess.run(optimizer, feed_dict={x: xtrain, y: ytrain})
		if step % log_frequency == 0:
			acc = sess.run(accuracy, feed_dict={x: xtrain, y: ytrain})
			loss = sess.run(cost, feed_dict={x: xtrain, y: ytrain})
			print "Iteration: ", step, "\Accuracy: ", acc, "\Loss: ", loss
		step += 1

