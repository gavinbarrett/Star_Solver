#!/usr/bin/env python3

class Node:

    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.f = self.g = self.h = 0
        self.new_pos = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

    def __eq__(self, other):
        return self.pos == other.pos

def in_range(node_pos, maze):
    if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze) - 1]) - 1) or node_pos[1] < 0:
        return False
    if maze[node_pos[0]][node_pos[1]] == 1:
        return False
    return True

def generate_children(curr, maze):
    children = []
    for newpos in curr.new_pos:
        node_pos = (curr.pos[0] + newpos[0], curr.pos[1] + newpos[1])

        if(in_range(node_pos, maze)):
            n = Node(curr.pos, node_pos)
            children.append(n)

    return children

def heuristic(curr, child, goal_node):
    child.g = curr.g + 1
    child.h = (abs(goal_node.pos[0]-child.pos[0]) + abs(goal_node.pos[1]-child.pos[1]))
    child.f = child.g + child.h
    child.parent = curr

def get_lowest_node(open_list):
    open_list.sort(key=lambda x: x.f)
    a = open_list.pop(0)
    return a

def is_goal(n, goal):
    if n == goal:
        path = []
        while n is not None:
            path.append(n)
            n = n.parent
        path.reverse()
        return path

def a_star(maze, start, goal):
    start_node = Node(None, start)
    goal_node = Node(None, goal)

    open_list = []
    closed_list = []

    open_list.append(start_node)
    curr_succ_cost = 0
    n = start_node
    while open_list:
        # pop lowest node from open list
        n = get_lowest_node(open_list)
        
        # generate children
        children = generate_children(n, maze)

        if n == goal_node:
            path = []
            while n is not None:
                path.append(n.pos)
                n = n.parent
            path.reverse()
            return path

        for child in children:

            # set child variables f, g, h
            heuristic(n, child, goal_node)

            if child in open_list:
                if child.g > curr_succ_cost:
                    continue
            
            elif child in closed_list:
                if child.g > curr_succ_cost:
                    continue
                else:
                    open_list.append(child)
            else:
                open_list.append(child)
        closed_list.append(n)

def main():
    maze1 = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

    maze2 = [
            [0, 1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [1, 1, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1]
            ]

    maze3 = [
            [0, 0, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 1, 0],
            [1, 1, 1, 0]
            ]

    maze4 = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 0, 1]
            ]

    start = (0, 0)
    goal = (2, 3)
    path = a_star(maze3, start, goal)
    if path:
        print(path)
    else:
        print('Goal could not be reached!')

main()
