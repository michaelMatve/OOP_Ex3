from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

def checkA0():
    print("graph A0")
    my_algo = GraphAlgo()
    if my_algo.load_from_json("..\\data\\A0.json"):
        print("success load")
    print(my_algo.get_graph().get_all_v())
    t_short = my_algo.shortest_path(0,5)
    print ("\n the shortest path between 0 to 5 is:{} \n and the distans is:{} \n".format(t_short[1],t_short[0]))
    t_tsp= my_algo.TSP([2,0,4,5])
    print("the shortest path to travel on all the nodes:{} \n and the distans is:{} \n".format(t_tsp[0], t_tsp[1]))
    t_cnt = my_algo.centerPoint()
    print("the center node is:{} \n and his distance to the furthest is:{} \n".format(t_cnt[0], t_cnt[1]))
    my_algo.plot_graph()

def checkA1():
    print("graph A1")
    my_algo = GraphAlgo()
    if my_algo.load_from_json("..\\data\\A1.json"):
        print("success load")
    print(my_algo.get_graph().get_all_v())
    t_short = my_algo.shortest_path(0,5)
    print ("\n the shortest path between 0 to 5 is:{} \n and the distans is:{} \n".format(t_short[1],t_short[0]))
    t_tsp= my_algo.TSP([2,0,4,5])
    print("the shortest path to travel on all the nodes:{} \n and the distans is:{} \n".format(t_tsp[0], t_tsp[1]))
    t_cnt = my_algo.centerPoint()
    print("the center node is:{} \n and his distance to the furthest is:{} \n".format(t_cnt[0], t_cnt[1]))
    my_algo.plot_graph()

def checkA2():
    print("graph A2")
    my_algo = GraphAlgo()
    if my_algo.load_from_json("..\\data\\A2.json"):
        print("success load")
    print(my_algo.get_graph().get_all_v())
    t_short = my_algo.shortest_path(0,5)
    print ("\n the shortest path between 0 to 5 is:{} \n and the distans is:{} \n".format(t_short[1],t_short[0]))
    t_tsp= my_algo.TSP([2,0,4,5])
    print("the shortest path to travel on all the nodes:{} \n and the distans is:{} \n".format(t_tsp[0], t_tsp[1]))
    t_cnt = my_algo.centerPoint()
    print("the center node is:{} \n and his distance to the furthest is:{} \n".format(t_cnt[0], t_cnt[1]))
    my_algo.plot_graph()

def checkA3():
    print("graph A3")
    my_algo = GraphAlgo()
    if my_algo.load_from_json("..\\data\\A3.json"):
        print("success load")
    print(my_algo.get_graph().get_all_v())
    t_short = my_algo.shortest_path(0,5)
    print ("\n the shortest path between 0 to 5 is:{} \n and the distans is:{} \n".format(t_short[1],t_short[0]))
    t_tsp= my_algo.TSP([2,0,4,5])
    print("the shortest path to travel on all the nodes:{} \n and the distans is:{} \n".format(t_tsp[0], t_tsp[1]))
    t_cnt = my_algo.centerPoint()
    print("the center node is:{} \n and his distance to the furthest is:{} \n".format(t_cnt[0], t_cnt[1]))
    my_algo.plot_graph()

def checkA4():
    print("graph A4")
    my_algo = GraphAlgo()
    if my_algo.load_from_json("..\\data\\A4.json"):
        print("success load")
    print(my_algo.get_graph().get_all_v())
    t_short = my_algo.shortest_path(0,5)
    print ("\n the shortest path between 0 to 5 is:{} \n and the distans is:{} \n".format(t_short[1],t_short[0]))
    t_tsp= my_algo.TSP([2,0,4,5])
    print("the shortest path to travel on all the nodes:{} \n and the distans is:{} \n".format(t_tsp[0], t_tsp[1]))
    t_cnt = my_algo.centerPoint()
    print("the center node is:{} \n and his distance to the furthest is:{} \n".format(t_cnt[0], t_cnt[1]))
    my_algo.plot_graph()

def checkA5():
    print("graph A5")
    my_algo = GraphAlgo()
    if my_algo.load_from_json("..\\data\\A5.json"):
        print("success load")
    print(my_algo.get_graph().get_all_v())
    t_short = my_algo.shortest_path(0,5)
    print ("\n the shortest path between 0 to 5 is:{} \n and the distans is:{} \n".format(t_short[1],t_short[0]))
    t_tsp= my_algo.TSP([2,0,4,5])
    print("the shortest path to travel on all the nodes:{} \n and the distans is:{} \n".format(t_tsp[0], t_tsp[1]))
    t_cnt = my_algo.centerPoint()
    print("the center node is:{} \n and his distance to the furthest is:{} \n".format(t_cnt[0], t_cnt[1]))
    my_algo.plot_graph()

def checkT0():
    print("graph T0")
    my_algo = GraphAlgo()
    if my_algo.load_from_json("..\\data\\T0.json"):
        print("success load")
    print(my_algo.get_graph().get_all_v())
    my_algo.plot_graph()

if __name__ == '__main__':
    checkA0()
    checkA1()
    checkA2()
    checkA3()
    checkA4()
    checkA5()
    checkT0()