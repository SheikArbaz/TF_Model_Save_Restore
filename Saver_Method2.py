import tensorflow as tf

x = tf.placeholder(tf.float32, shape=None)
y = tf.cast(tf.Variable(22, name="weight"), tf.float32)
z = tf.add(x,y)

tf.add_to_collection('x',x)
tf.add_to_collection('y',y)
tf.add_to_collection('z',z)

sess = tf.Session()


saver = tf.train.Saver(tf.trainable_variables() , max_to_keep = 1)
sess.run(tf.global_variables_initializer())
saver.export_meta_graph('../data/graph.meta')
saver.save(sess,'../data/model',global_step = 1, write_meta_graph = False)



feed = {x:10}



sess.run(tf.global_variables_initializer())
print sess.run(z,feed_dict=feed)














# sess.run(tf.global_variables_initializer())



