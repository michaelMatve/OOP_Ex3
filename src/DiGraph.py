from src.GraphInterface import GraphInterface
from node import Node


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = {}

    def v_size(self) -> int:
        pass

    def e_size(self) -> int:
        pass

    def get_mc(self) -> int:
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        self.nodes.get(id1).out_edges[id2] = weight
        self.nodes.get(id2).in_edges[id1] = weight

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        self.nodes[node_id]= Node(node_id, pos)

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass


