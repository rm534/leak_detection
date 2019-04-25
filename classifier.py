__author__ = "Robin M."

import tensorflow as tf
from tensorflow import keras


class Classifier():
    def __init__(self):
        self.model = self.create_model()

    # Data to be used, input and output pressure of pipe segment (two junctions) and output will be a classfier 0-15, use time maybe as well and flow rate over time and demand
    # Data could be normalised using gaussian normalisation
    def create_model(self):
        model = tf.keras.models.Sequential([
            keras.layers.Flatten(input_shape=(4, 24)),
            keras.layers.Dense(512, activation=tf.keras.activations.relu, input_shape=(784,)),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(15, activation=tf.keras.activations.softmax)
        ])

        model.compile(optimizer=tf.keras.optimizers.Adam(),
                      loss=tf.keras.losses.sparse_categorical_crossentropy,
                      metrics=['accuracy'])

        return model

    def train_model(self, training_data, training_labels, epochs=5):
        self.model.fit(training_data, training_labels, epochs=epochs)

    def test_model(self, test_data, test_labels):
        test_loss, test_acc = self.model.evaluate(test_data, test_labels)
        return test_loss, test_acc

    def save_model(self, model_title):
        self.model.save("classifiers/" + model_title + ".h5")

    def load_model(self, model_title):
        loaded_model = tf.contrib.saved_model.load_keras_model("classifiers/" + model_title + ".h5")
        self.model = loaded_model

    def summarise_model(self):
        self.model.summary()

class TrainingTestDataGenerator():
    def __init__(self):
        pass


if __name__ == "__main__":
    classifier = Classifier()
    classifier.save_model("eg")
