
import tensorflow as tf


class Trainer(object):

    learning_rate = 0.001

    def __init__(self):
        self.session = None

    def _has_saved_checkpoint(self) -> bool:
        return False

    def build_model(self):
        if self.session is not None:
            return

        self.X = tf.placeholder(tf.float32, [None, 28, 28, 1], name='X')
        self.Y = tf.placeholder(tf.float32, [None, 10], name='Y')

        layer_1 = tf.layers.conv2d(self.X, 32, [3, 3])
        layer_1 = tf.layers.max_pooling2d(layer_1, [2, 2], [2, 2])
        layer_1 = tf.layers.dropout(layer_1, 0.7, True)

        layer_2 = tf.layers.conv2d(layer_1, 64, [3, 3])
        layer_2 = tf.layers.max_pooling2d(layer_2, [2, 2], [2, 2])
        layer_2 = tf.layers.dropout(layer_2, 0.7, True)

        layer_3 = tf.layers.flatten(layer_2)
        layer_3 = tf.layers.dense(layer_3, 256, activation=tf.nn.relu)
        layer_3 = tf.layers.dropout(layer_3, 0.5, True)

        model = tf.layers.dense(layer_3, 10, activation=None)
        self.cost = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(logits=model, labels=self.Y))
        self.optimizer = tf.train.AdamOptimizer(self.learning_rate).minimize(self.cost)
        self.init = tf.global_variables_initializer()

        self.session = tf.Session()

        if self._has_saved_checkpoint():
            raise NotImplementedError()
        else:
            self.session.run(self.init)

    def close(self, type, value, traceback):
        self.session.close()

    def train(self, xs, ys):
        if self.session is None:
            raise Exception("session not created")

        cost, _ = self.session.run(
            [self.cost, self.optimizer],
            feed_dict={
                self.X: xs,
                self.Y: ys
            })

        print(cost)
