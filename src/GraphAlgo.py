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
        return self.graph

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
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as file:
                temp_dict = self.to_json_file()
                json.dump(temp_dict, indent=4, fp=file)
        except IOError as e:
            print(e)
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.dijkstra_algo(id1)
        answerList = []
        check_node = self.graph.nodes.get(id2)
        while check_node.tag != -1:
            answerList.insert(0,check_node.id)
            check_node = self.graph.nodes.get(check_node.tag)
        answerList.insert(0,check_node.id)
        answer = (self.graph.nodes.get(id2).weight,answerList)
        return answer

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        sum = 0.0
        answerlist = []
        run_node_id = self.graph.nodes.get(node_lst.get(0))
        dest_node_id = run_node_id
        while run_node_id!=None and len(node_lst)!=1:
            node_lst.remove(run_node_id)
            self.dijkstra_algo(run_node_id)
            mindist = float("inf")
            for id_n in node_lst:
                temp_node = self.graph.nodes.get(id_n)
                if temp_node.tag == -1:
                    return ([],float("inf"))
                if temp_node.weight<mindist:
                    mindist = temp_node.weight
                    dest_node_id = temp_node.id
            sum = sum + mindist
            check_node = self.graph.nodes.get(dest_node_id)
            temp_list =[]
            while check_node.tag != -1:
                temp_list.insert(0,check_node.id)
                check_node = self.graph.nodes.get(check_node.tag)
            temp_list.insert(0, check_node.id)
            while len(temp_list)!=1:
                answerlist.insert(-1, temp_list.pop(0))
            run_node_id = dest_node_id
        answerlist.add(self.graph.nodes.get(run_node_id))
        return (answerlist, sum)


    def centerPoint(self) -> (int, float):
        if self.is_connected():
            return (-1 , float("inf"))
        min = float("inf")
        min_id = None
        for node in self.graph.nodes.values():
            temp = self.max_dist(node.id)
            if temp<=min:
                min = temp
                min_id = node.id
        return (min_id, min)




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

    def dijkstra_algo(self, src: int):
        self.set_tags_weigth()
        run_node = self.graph.nodes.get(src)
        run_node.weight = 0.0
        while run_node != None:
            run_node.info = 'b'
            for des in run_node.out_edge:
                temp_node = self.graph.nodes.get(des)
                if temp_node.info == 'w':
                    if temp_node.weight >(run_node.weight + run_node.get(des)):
                        temp_node.weight = run_node.weight + run_node.get(des)
                        temp_node.tag = run_node.id
            run_node = None
            for node in self.graph.nodes.values():
                if node.info == 'w' and node.tag != -1:
                    if run_node == None:
                        run_node = node
                    elif node.weight < run_node.weigth:
                        run_node = node
        return

    def max_dist(self, src):
        self.dijkstra_algo(src)
        max =0.0
        for node in self.graph.nodes.values():
            if node.weight>max and node.weight!= float("inf"):
                max = node.weight
        return max

    def dfs(self, node : Node) -> None:
        stack = list()
        stack.append(node)
        while stack:
            node = stack.pop()
            if node.tag == -1:
                node.tag = 1

            for i in node.in_edges:
                if self.graph.nodes.get(i).tag == -1:
                    stack.append(self.graph.nodes.get(i))


    def get_transpose(self):
        transpose = GraphAlgo(DiGraph())
        for i in self.graph.nodes.values():
            transpose.graph.add_node(i.id, i.pos)

        for i in self.graph.nodes.values():
            for j in i.in_edges:
                transpose.graph.add_edge(j, i.id, i.in_edges.get(j))

            for j in i.out_edges:
                transpose.graph.add_edge(j, i.id, i.out_edges.get(j))

        return transpose


    def set_tags_weigth(self) -> None:
        for i in self.graph.nodes.values():
            i.tag = -1
            i.weigth = float("inf")
            i.info = 'w'

    def is_connected(self):
        self.set_tags_weigth()
        self.dfs(self.graph.nodes.get(0))
        for i in self.graph.nodes.values():
            if i.tag == -1:
                return False

        transpose = self.get_transpose()
        transpose.set_tags_weigth()
        transpose.dfs(self.graph.nodes.get(0))
        for i in transpose.graph.nodes.values():
            if i.tag == -1:
                return False

        return True



