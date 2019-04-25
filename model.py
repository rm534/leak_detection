__author__ = "Robin M."

import wntr
import networkx as nx

class Model():
    def __init__(self, inp_file):
        self.title = inp_file
        self.wn = wntr.network.WaterNetworkModel(inp_file)
        self.get_graph()


    def simulate_network(self):
        wntr_sim = wntr.sim.WNTRSimulator(self.wn)
        self.results = wntr_sim.run_sim()
        self.flowrate = self.results.link["flowrate"]
        self.pressure = self.results.node["pressure"]
        return self.results

    def get_flowrate_at_link(self, link):
        flowrate_at_link = self.flowrate.loc[:, link]
        return flowrate_at_link

    def get_pressure_at_node(self, node):
        pressure_at_node = self.pressure.loc[:, node]
        return pressure_at_node

    def get_graph(self):
        self.graph = self.wn.get_graph()
        return self.graph

    def get_node(self, node):
        return self.graph[node]

    def save_results(self):
        pass

    def load_results(self):
        pass
    
    def get_input_output_pressure(self):
        pipe_nodes = []
        pipes_iterator = self.wn.pipes()
        for item in pipes_iterator:
            pipe_nodes.append((str(item[1].start_node), str(item[1].end_node)))
        return pipe_nodes

    def print_graph(self):
        wntr.graphics.network.plot_interactive_network(self.wn, title=self.title)

if __name__ == "__main__":
    model = Model("models/net2.inp")
    #print(model.get_node("node1"))
    #results = model.simulate_network()
    #print(model.get_pressure_at_node("node3"))
    model.get_input_output_pressure()
    model.print_graph()
