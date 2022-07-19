import numpy as np

class Node:
    
    def __init__(self, s):  
        self.child = s
        self.parent = None
        self.gn = 0
        self.hn = 0
        self.fn = 0

    def get_parent(self):
        return self.parent
    
    def get_hn(self):
        return self.hn
    
    def get_fn(self):
        return self.gn + self.hn
    
    def get_gn(self):
        return self.gn
    
    def get_current_state(self):
        return self.child
    
    def update_gn(self, gn):
        self.gn=gn
        
    def update_hn(self, hn):
        self.hn=hn
    
    def update_parent(self, parent):
        self.parent= parent
    
    def expand_node(fringe, explored_nodes, current_node, goal_node, zero, g, count,heuristic):
        a                   =   [ list(item.get_current_state()) for item in explored_nodes ]
        explored_nodes.append(current_node)
        current_node_array  =   np.asarray(current_node.get_current_state())

        if zero != 0 and zero!=3 and zero!=6:
            node_copy           =   current_node_array.copy()
            temp                =   node_copy[zero-1]
            node_copy[zero-1]   =   current_node_array[zero]
            node_copy[zero]     =   temp
            distance            =   Distance.distance(node_copy,goal_node,heuristic)
            count               =   count+1
            
            if not list(node_copy) in a:
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)            
                node_copy.update_parent(current_node)
                fringe.append(node_copy)
       
        if zero!=6 and zero!=7 and zero!=8:
            node_copy           =   current_node_array.copy()
            temp                =   node_copy[zero+3]
            node_copy[zero+3]   =   current_node_array[zero]
            node_copy[zero]     =   temp
            distance            =   Distance.distance(node_copy,goal_node,heuristic)
            count               =   count+1
            if not list(node_copy) in a:
                node_copy       =   Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)            
                node_copy.update_parent(current_node)
                fringe.append(node_copy)

        if zero != 0 and zero!=1 and zero!=2:
            node_copy           =   current_node_array.copy()
            temp                =   node_copy[zero-3]
            node_copy[zero-3]   =   current_node_array[zero]
            node_copy[zero]     =   temp
            distance            =   Distance.distance(node_copy,goal_node,heuristic)
            count               =   count+1
            if not list(node_copy) in a:
                node_copy=Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)            
                node_copy.update_parent(current_node)
                fringe.append(node_copy)
    
 
        if zero != 2 and zero!=5 and zero!=8:
            node_copy           =   current_node_array.copy()
            temp                =   node_copy[zero+1]
            node_copy[zero+1]   =   current_node_array[zero]
            node_copy[zero]     =   temp
            distance            =   Distance.distance(node_copy,goal_node,heuristic)
            count               =   count+1
            if not list(node_copy) in a:
                node_copy       =   Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)            
                node_copy.update_parent(current_node)
                fringe.append(node_copy)
        return count
            
class Puzzle:
    
    def least_fn(fringe):
        fn_fringe           =   []
        for i in range(len(fringe)):
            fn_fringe.append(fringe[i].get_fn())
        minimum_fn          =   min(fn_fringe)
        minimum_fn_index    =   fn_fringe.index(minimum_fn)
        return minimum_fn_index
        
    def print_state(node):
        print("\n")
        print(node.get_current_state()[0] , " | " , node.get_current_state()[1] , " | "
                , node.get_current_state()[2]);
        print(node.get_current_state()[3] , " | " , node.get_current_state()[4] , " | "
                , node.get_current_state()[5]);
        print(node.get_current_state()[6] , " | " , node.get_current_state()[7] , " | "
                , node.get_current_state()[8]);
        
    def goal_reached(explored_nodes, count):
        nodes_expanded  =   len(explored_nodes)-1
        path            =   []
        init            =   explored_nodes[0]
        current         =   explored_nodes.pop()
        
        while init!=current:
            path.append(current)
            current = current.get_parent()
        
        path.append(init)
        path.reverse()
        
        for i in path:
            Puzzle.print_state(i)
        
        print("Path Cost: ", len(path)-1, "\n");
        
    def path(explored_nodes):
        explored_nodes.pop()


class Distance:
    '''Here I was trying out misplaced tiles(hamming distance) heuristic and manhattan distance heuritic to compare the amount of time they took to complete the problem. The misplaced tile took 118 seconds to complete a 
    difficult level problem that you had given. I believe it was the 3x3_5 example that took 118s for misplaced tile and 0.2s for manhattan. I couldve removed the if else from here but decided to just 
    leave it here instead and give heuristic variable a hard value of 2 so that it always does manhattan'''
    def distance(arr, goal, heuristic):
        distance = 0
        if heuristic == 1:
            for i in range(8):
                if arr[i]!=goal[i]:
                    distance=distance+1
            return distance
        elif heuristic == 2:
            arr     = np.asarray(arr).reshape(3,3)
            goal    = np.asarray(goal).reshape(3,3)
            for i in range(8):
                a,b      = np.where(arr == i+1)
                x,y      = np.where(goal == i+1)
                distance = distance + abs((a-x)[0])+abs((b-y)[0])
            return distance