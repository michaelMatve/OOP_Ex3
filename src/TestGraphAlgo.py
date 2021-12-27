from unittest import TestCase
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph


class TestGraphAlgo(TestCase):

    def make_my_graph(self):
        my_algo = GraphAlgo()
        my_algo.graph.add_node((1.1, 1.5, 0), 0)
        my_algo.graph.add_node((1.4, 1.3 , 0), 2)
        my_algo.graph.add_node((1.1, 0.5, 0), 5)
        my_algo.graph.add_node((1.3, 1, 0), 6)
        my_algo.graph.add_node((1.5, 0.8, 0), 7)
        my_algo.graph.add_node((2.0, 1.1, 0), 10)
        my_algo.graph.add_node((2.5, 1.4, 0), 12)
        my_algo.graph.add_node((1.3, 0.3, 0), 13)
        my_algo.graph.add_edge(0, 2, 1.2)
        my_algo.graph.add_edge(2, 0, 2.5)
        my_algo.graph.add_edge(2, 10, 1.8)
        my_algo.graph.add_edge(6, 2, 1.3)
        my_algo.graph.add_edge(6, 5, 1.4)
        my_algo.graph.add_edge(5, 7, 0.2)
        my_algo.graph.add_edge(7, 13, 2.6)
        my_algo.graph.add_edge(13, 10, 1.85)
        my_algo.graph.add_edge(10, 6, 1.1)
        my_algo.graph.add_edge(10, 7, 1.32)
        my_algo.graph.add_edge(10, 12, 1.0)
        my_algo.graph.add_edge(12, 13, 1.7)
        return my_algo

    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()

    def test_random_pos(self):
        self.fail()

    def test_to_json_file(self):
        self.fail()

    def test_dijkstra_algo(self):
        self.fail()

    def test_max_dist(self):
        self.fail()

    def test_dfs(self):
        self.fail()

    def test_get_transpose(self):
        self.fail()

    def test_set_tags_weight(self):
        self.fail()

    def test_is_connected(self):
        self.fail()
