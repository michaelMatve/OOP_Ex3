from src.GraphInterface import GraphInterface
from node import Node


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0
        self.num_edges = 0
        self.mc = 0


    def v_size(self) -> int:
        return self.num_nodes

    def e_size(self) -> int:
        return self.num_edges

    def get_all_v(self) -> dict:
        pass

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].out_edges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if(self.nodes.get(id1)==None) :
            return False
        if (self.nodes.get(id2) == None):
            return False
        if (self.nodes.get(id1).out_edges[id2] != None):
            return False
        self.nodes.get(id1).out_edges[id2] = weight
        self.nodes.get(id2).in_edges[id1] = weight
        self.num_edges += 1
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if (self.nodes.get(node_id) != None):
            return False
        self.nodes[node_id]= Node(node_id, pos)
        self.num_nodes += 1
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if (self.nodes.get(node_id) == None):
            return False
        for node in self.nodes.values() :
            if(node.id != node_id) :
                node.out_edges.pop(node_id)
                node.in_edges.pop(node_id)
        self.nodes.pop(node_id)
        self.num_nodes -= 1
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (self.nodes.get(node_id1) == None):
            return False
        if (self.nodes.get(node_id2) == None):
            return False
        if (self.nodes.get(node_id1).out_edges[node_id2] == None):
            return False
        self.nodes.get(node_id1).out_edges.pop(node_id2)
        self.nodes.get(node_id1).in_edges.pop(node_id2)
        self.mc += 1
        return True


