import tensorflow as tf

with tf.Session() as sess:
    x = tf.constant([2, 3, 4])
    y = tf.sign(x)

    print sess.run(y)
