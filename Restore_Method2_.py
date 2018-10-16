import tensorflow as tf

sess = tf.Session()

saver = tf.train.import_meta_graph('../data/graph.meta')
saver.restore(sess,'../data/model-1')

x = tf.get_collection('x')[0]
y = tf.get_collection('y')[0]
z = tf.get_collection('z')[0]


sess.run(tf.global_variables_initializer())
print sess.run(z,feed_dict={x:90})