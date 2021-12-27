from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

def load_test():
    my_graph = GraphAlgo(DiGraph())
    my_graph.load_from_json('C:\\Users\\Dell\\PycharmProjects\\OOP_Ex3\\data\\A1.json')
    print(my_graph.graph.nodes.get(0).out_edges[1])
    print(my_graph.graph.nodes.get(0).in_edges[1])
    my_graph.save_to_json('first save.json')
    my_graph1 = GraphAlgo(DiGraph())
    my_graph1.load_from_json('first save.json')
    print(my_graph1.graph.nodes.get(0).out_edges[1])
    print(my_graph1.graph.nodes.get(0).in_edges[1])



if __name__ == '__main__':
    load_test()
