import json
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from node import Node
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        pass

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as file:
                temp_dict = json.load(file)

            for node in temp_dict['Nodes']:
                self.graph.add_node(node.get('id'), tuple(float(s) for s in node.get('pos').strip("()").split(",")))
            for edge in temp_dict['Edges']:
                self.graph.add_edge(edge.get('src'), edge.get('dest'), edge.get('w'))
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as file:
                temp_dict = self.to_json_file()
                json.dump(temp_dict, indent=4, fp=file)
        except IOError as e:
            print(e)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass


    def plot_graph(self) -> None:
        pass

    def to_json_file(self):
        temp_dict = {}
        temp_dict['Edges'] = []
        temp_dict['Nodes'] = []
        for node in self.graph.nodes.values():
            temp_dict['Nodes'].append({'pos': "{},{},{}".format(node.pos[0], node.pos[1], node.pos[2]), 'id': node.id})
            for d in node.out_edges:
                temp_dict['Edges'].append({'src': node.id, 'w': node.out_edges[d], 'dest': d})
        return temp_dict
















































    def dfs(self, node : Node) -> None:
        stack = list()
        stack.append(node)
        while stack.__sizeof__() != 0:
            node = stack.pop()
            if node.tag == 0:
                node.tag = 1

            for i in node.in_edges:
                if self.graph.nodes.get(i).tag == 0:
                    stack.append(self.graph.nodes.get(i))

    def get_transpose(self):
        transpose = DiGraph()
        for i in self.graph.nodes.values():
            transpose.add_node(i)

        for i in transpose.nodes.values():
            i.in_edges



