import json
import random
from typing import List
import matplotlib.pyplot as plt

from src.GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from node import Node
from src.GraphInterface import GraphInterface

"""

"""
class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph=None):
        if graph==None:
            graph = DiGraph()
        self.graph = graph



    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as file:
                temp_dict = json.load(file)

            for node in temp_dict['Nodes']:
                if node.get('pos') != None:
                    self.graph.add_node(node.get('id'), tuple(float(s) for s in node.get('pos').strip("()").split(",")))
                else:
                    self.graph.add_node(node.get('id'))
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
        if(check_node.tag == -1):
            return (float("inf"),[])
        while check_node.tag != -1:
            answerList.insert(0,check_node.id)
            check_node = self.graph.nodes.get(check_node.tag)
        answerList.insert(0,check_node.id)
        answer = (self.graph.nodes.get(id2).weight,answerList)
        return answer

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        sum = 0.0
        answerlist = []
        run_node_id = node_lst[0]
        dest_node_id = run_node_id
        while run_node_id!=None and len(node_lst)>1:
            node_lst.remove(run_node_id)
            self.dijkstra_algo(run_node_id)
            mindist = float("inf")
            for id_n in node_lst:
                temp_node = self.graph.nodes.get(id_n)
                if temp_node.weight<mindist:
                    mindist = temp_node.weight
                    dest_node_id = temp_node.id
            if mindist==float("inf"):
                return ([],float("inf"))
            sum = sum + mindist
            check_node = self.graph.nodes.get(dest_node_id)
            temp_list =[]
            while check_node.tag != -1:
                temp_list.insert(0,check_node.id)
                check_node = self.graph.nodes.get(check_node.tag)
            temp_list.insert(0, check_node.id)
            while len(temp_list)!=1:
                answerlist.append(temp_list.pop(0))
            run_node_id = dest_node_id
        answerlist.append(self.graph.nodes.get(run_node_id).id)
        return (answerlist, sum)


    """
    this function calculates the center of the graph, 
    it calculates the max_dist of every node and returns the id of the center along with distance
    """

    def centerPoint(self) -> (int, float):
        if not self.is_connected():  # cheack if the graph is connected, if not it means no center
            return (-1 , float("inf"))
        min = float("inf")  # sets the min to float("inf"), and the id to None
        min_id = None
        for node in self.graph.nodes.values():  # go through every node in the graph, and checks if it max_dist is the minimum
            temp = self.max_dist(node.id)
            if temp<=min:  # if so updated the id of the center, and the distance
                min = temp
                min_id = node.id
        return (min_id, min)


    """
    this function draws the line on the screen
    """

    def plot_graph(self) -> None:
        for node in self.graph.nodes.values(): # go through every node in the graph
            if node.pos == None:  # if the node doesnt have a pos, creates a new pos for him
                node.pos = self.random_pos()
        for node in self.graph.nodes.values():  # go through every node in the graph
            x, y, z = node.pos
            plt.plot(x, y, markersize= 10, marker= "o", color= "black")  # uses plot and text functions to draw the node on the screen
            plt.text(x, y, str(node.id), color= "red", fontsize= 12)
            for neigh in node.out_edges:  # go through every in edge the node has
                neigh_x, neigh_y, neigh_z = self.graph.nodes.get(neigh).pos
                plt.annotate("", xy=(x, y), xytext=(neigh_x, neigh_y), arrowprops=dict(arrowstyle="<|-"))  # draws an edge to that node

        plt.show()


    """
    this function generates a random pos for the node
    """

    def random_pos(self) -> tuple:
        x = random.uniform(35.187594216303474, 35.21310882485876)  # creates random x, in range
        y = random.uniform(32.10152879327731, 32.10788938151261)  # creates random y, in range
        z = 0.0
        ans = (x, y, z)
        return ans  # returns the new pos



    def to_json_file(self):
        temp_dict = {}
        temp_dict['Edges'] = []
        temp_dict['Nodes'] = []
        for node in self.graph.nodes.values():
            if node.pos!=None:
                temp_dict['Nodes'].append({'pos': "{},{},{}".format(node.pos[0], node.pos[1], node.pos[2]), 'id': node.id})
            else:
                temp_dict['Nodes'].append({'id': node.id})
            for d in node.out_edges:
                temp_dict['Edges'].append({'src': node.id, 'w': node.out_edges[d], 'dest': d})
        return temp_dict

    def dijkstra_algo(self, src: int):
        self.set_tags_weight()
        run_node = self.graph.nodes.get(src)
        run_node.weight = 0.0
        while run_node != None:
            run_node.info = 'b'
            for des in run_node.out_edges:
                temp_node = self.graph.nodes.get(des)
                if temp_node.info == 'w':
                    if temp_node.weight > (run_node.weight + run_node.out_edges.get(des)):
                        temp_node.weight = run_node.weight + run_node.out_edges.get(des)
                        temp_node.tag = run_node.id
            run_node = None
            for node in self.graph.nodes.values():
                if node.info == 'w' and node.tag != -1:
                    if run_node == None:
                        run_node = node
                    elif node.weight < run_node.weight:
                        run_node = node
        return


    """
    this returns the max shortest path from this node to a certain node in the graph
    """

    def max_dist(self, src):
        self.dijkstra_algo(src)  # makes dijkstra on this node to calculate shortest path from this node to every node in the graph
        max =0.0
        for node in self.graph.nodes.values():  # go through every node in the graph, and if there is a path longer than max sets max to it
            if node.weight>max and node.weight!= float("inf"):
                max = node.weight
        return max


    """
    this function makes dfs from a certain node
    """

    def dfs(self, node : Node) -> None:
        stack = list() # create a stack
        stack.append(node) # push the node to the stack
        while stack: # as long as the stack is not empty, pop the stack
            node = stack.pop()
            if node.tag == -1: # checks if the node is not visited, if not change it to visited
                node.tag = 1

            for i in node.out_edges: # go through the nodes neighbours
                if self.graph.nodes.get(i).tag == -1: # if the neighbour is not visited yet, push him to the stack
                    stack.append(self.graph.nodes.get(i))

    """
    this function makes a transpose graph out of the original graph
    """

    def get_transpose(self):
        for i in self.graph.nodes.values(): # go through all the nodes and changes the in_edges to out_edges and vice versa
            temp = i.in_edges.copy()
            i.in_edges = i.out_edges.copy()
            i.out_edges = temp.copy()


    """
    this function sets all the nodes tag to -1, the weight to float("inf"), the info to "w" (not visited)
    """

    def set_tags_weight(self) -> None:
        for i in self.graph.nodes.values():
            i.tag = -1
            i.weight = float("inf")
            i.info = 'w'

    """
    this function checks if the graph is SCC, if so, it returns true, else false
    """

    def is_connected(self):
        self.set_tags_weight() # sets the tag of every node to -1
        self.dfs(self.graph.nodes.get(0)) # does dfs on the first node in the graph
        for i in self.graph.nodes.values(): # checks if after the dfs there is a node with tag -1, if so it means the graph isnt SCC
            if i.tag == -1:
                return False

        self.get_transpose() # make a transpose graph
        self.set_tags_weight() # sets the tag of every node to -1
        self.dfs(self.graph.nodes.get(0)) # does dfs on the first node in the graph
        for i in self.graph.nodes.values(): # checks if after the dfs there is a node with tag -1, if so it means the graph isnt SCC
            if i.tag == -1:
                self.get_transpose() # returns the graph to it original form
                return False
        self.get_transpose() # returns the graph to it original form
        return True



