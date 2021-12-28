import unittest
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_load_from_json(self):
        graph = GraphAlgo()
        # graph.load_from_json("nss1000.json")
        # graph.load_from_json("nss10000.json")
        # graph.load_from_json("nss100000.json")

    def test_save_to_json(self):
        graph = GraphAlgo()
        # graph.load_from_json("nss1000.json")
        # graph.load_from_json("nss10000.json")
        # graph.load_from_json("nss100000.json")

        # graph.save_to_json("nss1000.json")
        # graph.save_to_json("nss10000.json")
        # graph.save_to_json("nss100000.json")

    def test_shortest_path(self):
        graph = GraphAlgo()
        # graph.load_from_json("nss1000.json")
        # graph.load_from_json("nss10000.json")
        # graph.load_from_json("nss100000.json")

        # self.assertEqual(3.616768943234364, graph.shortest_path(35,123)[0])
        # self.assertEqual(4.175305974288818, graph.shortest_path(124, 5000)[0])
        # self.assertEqual(3.616768943234364, graph.shortest_path(1000, 55000)[0])



    def test_tsp(self):
        graph = GraphAlgo()
        # graph.load_from_json("nss1000.json")
        # self.assertEqual((graph.TSP([12,0, 10, 6])[0]), [12, 936, 6, 525, 446, 0, 87, 10])
        # graph.load_from_json("nss10000.json")
        # self.assertEqual((graph.TSP([12,0, 10, 6])[0]), [12, 7491, 8121, 1639, 0, 8162, 8464, 10, 9312, 6856, 6])
        # graph.load_from_json("nss100000.json")
        # self.assertEqual((graph.TSP([12,0, 10, 6])[0]), [12, 765, 346, 10, 200, 88, 6, 329, 54, 0])


    def test_centerPoint(self):
        graph = GraphAlgo()
        # graph.load_from_json("nss1000.json")
        # self.assertEqual(445, graph.centerPoint()[0])


if __name__ == '__main__':
    unittest.main()
