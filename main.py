import tensorflow as tf
from os import path, getcwd, chdir

path = f'{getcwd()}/mnist.npz'

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)


def train_mnist_conv():

    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if (logs.get('acc') > 0.998):
                print("99.8% accuracy achieved. Done training.")
                self.model.stop_training = True

    callback = myCallback()

    mnist = tf.keras.datasets.mnist
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data(path=path)

    training_images = training_images.reshape(60000, 28, 28, 1)
    test_images = test_images.reshape(10000, 28, 28, 1)
    training_images = training_images / 255.0
    test_images = test_images / 255.0

    model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28,28,1)),
            tf.keras.layers.MaxPooling2D(2,2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    history = model.fit(training_images, training_labels, epochs=20, verbose=2, callbacks=[callback])

    return history.epoch, history.history['acc'][-1]

if __name__ == '__main__':
    _, _ = train_mnist_conv()