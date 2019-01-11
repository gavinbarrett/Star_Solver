#!/usr/bin/env python3
import sys
from src.colors import colors
from src.reader import Reader

class Node:
    
    ''' A representation of a single position '''
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.f = self.g = self.h = 0
        self.new_pos = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

    def __eq__(self, other):
        return self.pos == other.pos

class Maze_Solver:

    ''' A class for solving mazes '''
    def __init__(self, f,  start, goal):
        self.reader = Reader(f)
        self.start = tuple(map(int, start.split(',')))
        self.goal = tuple(map(int, goal.split(',')))
        
    
    def print_solved(self, path):
        ''' Print solved maze '''
        if path:
            tup = []
            for i in range(0, len(self.reader.maze)):
                for j in range(0, len(self.reader.maze)):
                    tup.append(i)
                    tup.append(j)
                    if tuple(tup) in path:
                        print(colors.red + str(self.reader.maze[i][j]) + ' ' + colors.white , end='')
                    else:
                        print(str(self.reader.maze[i][j]) + ' ', end='')
                    tup = []
                print('')
        else:
            print('Goal could not be reached!')


    def in_range(self, node_pos):
        ''' Check to see if tile is valid '''
        if node_pos[0] > (len(self.reader.maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(self.reader.maze[len(self.reader.maze) - 1]) - 1) or node_pos[1] < 0:
            return False
        if self.reader.maze[node_pos[0]][node_pos[1]] == 1:
            return False
        return True

    def generate_children(self, curr):
        ''' Return list of possible steps '''
        children = []
        for newpos in curr.new_pos:
            node_pos = (curr.pos[0] + newpos[0], curr.pos[1] + newpos[1])

            if(self.in_range(node_pos)):
                n = Node(curr.pos, node_pos)
                children.append(n)
        return children


# FIXME: REFACTOR FUNCTION TO EVALUATION FUNCTION
    def heuristic(self, curr, child, goal_node):
        ''' Calculate traversal cost from g + h '''
        child.g = curr.g + 1
        child.h = (abs(goal_node.pos[0]-child.pos[0]) + abs(goal_node.pos[1]-child.pos[1]))
        child.f = child.g + child.h
        child.parent = curr

    def get_lowest_node(self, open_list):
        ''' Return open node with the lowest cost '''
        open_list.sort(key=lambda x: x.f)
        a = open_list.pop(0)
        return a

    def is_goal(self, n, goal):
        ''' Check to see if we are at the goal '''
        if n == goal:
            path = []
            while n is not None:
                path.append(n.pos)
                n = n.parent
            path.reverse()
            return path

    def a_star(self):
        ''' Perform A* search for the goal '''
        # initialization 
        start_node = Node(None, self.start)
        goal_node = Node(None, self.goal)

        open_list = []
        closed_list = []

        open_list.append(start_node)
        #FIXME: Should below be initialized to something else?
        curr_succ_cost = 0

        # main search loop
        while open_list:
            # pop lowest node from open list
            n = self.get_lowest_node(open_list)
        
            # generate children of node n
            children = self.generate_children(n)
        
            # return path if goal has been reached
            path = self.is_goal(n, goal_node)
            if path:
                return path
        
            # compare each child
            for child in children:
    
                # set child variables f, g, h
                self.heuristic(n, child, goal_node)

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
    goal = (5, 4)
    
    MSolver = Maze_Solver(sys.argv[1], sys.argv[2], sys.argv[3])
    
    path = MSolver.a_star()
    
    MSolver.print_solved(path)

main()
