__author__ = "Robin M."

import model
import classifier

MODEL = "net2.inp"


class TaskManager(model, classifier):
    def __init__(self):
        model.Model.__init__(self, MODEL)
        classifier.Classifier.__init__(self, inputs, outputs)

    def analyse_simulation(self):
        # simulate model
        results = self.simulate_model()
        # get input and outputs for all nodes
        inp_out_pressure = self.get_input_output_pressure()
        # feed the inputs and outputs into neural network classifier

if __name__ == "__main__":
    pass
