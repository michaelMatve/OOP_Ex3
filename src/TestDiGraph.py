from unittest import TestCase
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

class TestDiGraph(TestCase):

    def test_v_size(self):
        algo1 = GraphAlgo()
        algo1.load_from_json("..\\data\\A1.json")
        self.assertEqual(17, algo1.graph.v_size())
        algo1.load_from_json("..\\data\\A2.json")
        self.assertEqual(31, algo1.graph.v_size())
        algo1.graph.remove_node(0)
        self.assertEqual(30, algo1.graph.v_size())
        algo1.graph.add_node(0, (1,2,3))
        self.assertEqual(31, algo1.graph.v_size())



    def test_e_size(self):
        algo1 = GraphAlgo()
        algo1.load_from_json("..\\data\\A1.json")
        self.assertEqual(36, algo1.graph.e_size())
        algo1.graph.remove_node(0)
        self.assertEqual(32, algo1.graph.e_size())
        algo1.graph.add_edge(0,1,4)
        self.assertEqual(32, algo1.graph.e_size())
        algo1.graph.add_node(0,(0,1,2))
        algo1.graph.add_edge(0,1,4)
        self.assertEqual(33, algo1.graph.e_size())




    def test_get_all_v(self):

        self.fail()

    def test_all_in_edges_of_node(self):
        algo1 = GraphAlgo()
        algo1.load_from_json("..\\data\\A1.json")
        self.assertEqual(1.8635670623870366, algo1.graph.all_in_edges_of_node(0).get(1))
        algo1.graph.remove_edge(1,0)
        self.assertEqual(None, algo1.graph.all_in_edges_of_node(0).get(1))
        algo1.graph.remove_node(0)
        self.assertEqual(None, algo1.graph.all_in_edges_of_node(0))




    def test_all_out_edges_of_node(self):
        algo1 = GraphAlgo()
        algo1.load_from_json("..\\data\\A1.json")

        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
