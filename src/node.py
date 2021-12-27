class Node:
    def __init__(self,id : int, pos : tuple):
        self.pos = pos
        self.id = id
        self.in_edges = {}
        self.out_edges = {}


