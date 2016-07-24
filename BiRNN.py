def BiRNN(x, weights, biases):
	lstm_fw_cell = rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)
	lstm_bw_cell = rnn_cell.BasicLSTMCell(n_hidden, forget_bias=1.0)
	outputs = rnn.bidirectional_rnn(lstm_fw_cell, lstm_bw_cell, x, dtype=tf.float32)
	return tf.matmul(outputs[-1], weights['out']) + biases['out']