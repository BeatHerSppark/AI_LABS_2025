from searching_framework import Problem, breadth_first_graph_search, astar_search


class Squares(Problem):
    def __init__(self, initial, house):
        super().__init__(initial, house)

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state):
        x,y = state
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        return True

    def successor(self, state):
        successors = dict()

        for i, (x, y) in enumerate(state):
            if self.check_valid((x, y+1)):
                state_cp = [list(el) for el in state]
                state_cp[i] = [x, y+1]
                successors[f'Pomesti kvadratche {i+1} gore'] = tuple(tuple(el) for el in state_cp)
            if self.check_valid((x, y-1)):
                state_cp = [list(el) for el in state]
                state_cp[i] = [x, y-1]
                successors[f'Pomesti kvadratche {i+1} dolu'] = tuple(tuple(el) for el in state_cp)
            if self.check_valid((x+1, y)):
                state_cp = [list(el) for el in state]
                state_cp[i] = [x+1, y]
                successors[f'Pomesti kvadratche {i+1} desno'] = tuple(tuple(el) for el in state_cp)
            if self.check_valid((x-1, y)):
                state_cp = [list(el) for el in state]
                state_cp[i] = [x-1, y]
                successors[f'Pomesti kvadratche {i+1} levo'] = tuple(tuple(el) for el in state_cp)

        return successors

    def h(self, node):
        state = node.state
        goal = self.goal

        return sum(abs(state_coord[0]-goal_coord[0]) + abs(state_coord[1]-goal_coord[1]) for (state_coord, goal_coord) in zip(state, goal))

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    initial_state = tuple()
    for _ in range(5):
        initial_state += (tuple(map(int, input().split(','))), )

    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(initial_state, goal_state)
    res = astar_search(squares)

    if res is not None:
        print(res.solution())
    else:
        print('No solution!')
