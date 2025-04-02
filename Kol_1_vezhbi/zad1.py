from searching_framework import Problem, breadth_first_graph_search, astar_search

class GhostOnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    # @staticmethod
    # def check_valid(state, walls, n):
    #     pass

    def successor(self, state):
        successors = dict()

        g_x, g_y = state[0], state[1]

        #Gore
        if 0<=g_y+1<n and (g_x, g_y+1) not in self.walls:
            successors["Gore 1"] = (g_x, g_y+1)
        if 0<=g_y+2<n and (g_x, g_y+2) not in self.walls:
            successors["Gore 2"] = (g_x, g_y+2)
        if 0<=g_y+3<n and (g_x, g_y+3) not in self.walls:
            successors["Gore 3"] = (g_x, g_y+3)

        #Desno
        if 0<=g_x+1<n and (g_x+1, g_y) not in self.walls:
            successors["Desno 1"] = (g_x+1, g_y)
        if 0<=g_x+2<n and (g_x+2, g_y) not in self.walls:
            successors["Desno 2"] = (g_x+2, g_y)
        if 0<=g_x+3<n and (g_x+3, g_y) not in self.walls:
            successors["Desno 3"] = (g_x+3, g_y)

        return successors

    def h(self, node):
        state = node.state
        goal = self.goal

        return (abs(state[0] - goal[0]) + abs(state[1] - goal[1]))/3


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, holes, n, goal_pos)
    res = astar_search(problem)

    if res is not None:
        print(res.solution())
    else:
        print('No solution!')