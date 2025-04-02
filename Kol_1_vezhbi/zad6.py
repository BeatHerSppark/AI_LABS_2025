from searching_framework import Problem, breadth_first_graph_search, astar_search


class BallGame(Problem):
    def __init__(self, initial, blocks, n):
        super().__init__(initial, None)
        self.blocks = blocks
        self.n = n

    # GoreLevo GoreDesno DoluLevo DoluDesno Levo Desno
    def successor(self, state):
        successors = dict()

        for x,y in state:
            if 0<=x-2<self.n and 0<=y+2<self.n and (x-2,y+2) not in self.blocks and (x-1,y+1) in state:
                state_cp = [list(el) for el in state]
                state_cp[state_cp.index([x,y])] = [x-2,y+2]
                state_cp.remove([x-1,y+1])
                successors[f'Gore Levo: (x={x},y={y})'] = tuple([tuple(el) for el in state_cp])

            if 0<=x+2<self.n and 0<=y+2<self.n and (x+2,y+2) not in self.blocks and (x+1,y+1) in state:
                state_cp = [list(el) for el in state]
                state_cp[state_cp.index([x,y])] = [x+2,y+2]
                state_cp.remove([x+1,y+1])
                successors[f'Gore Desno: (x={x},y={y})'] = tuple([tuple(el) for el in state_cp])

            if 0<=x-2<self.n and 0<=y-2<self.n and (x-2,y-2) not in self.blocks and (x-1,y-1) in state:
                state_cp = [list(el) for el in state]
                state_cp[state_cp.index([x,y])] = [x-2,y-2]
                state_cp.remove([x-1,y-1])
                successors[f'Dolu Levo: (x={x},y={y})'] = tuple([tuple(el) for el in state_cp])

            if 0<=x+2<self.n and 0<=y-2<self.n and (x+2,y-2) not in self.blocks and (x+1,y-1) in state:
                state_cp = [list(el) for el in state]
                state_cp[state_cp.index([x,y])] = [x+2,y-2]
                state_cp.remove([x+1,y-1])
                successors[f'Dolu Desno: (x={x},y={y})'] = tuple([tuple(el) for el in state_cp])

            if 0<=x-2<self.n and (x-2,y) not in self.blocks and (x-1,y) in state:
                state_cp = [list(el) for el in state]
                state_cp[state_cp.index([x,y])] = [x-2,y]
                state_cp.remove([x-1,y])
                successors[f'Levo: (x={x},y={y})'] = tuple([tuple(el) for el in state_cp])

            if 0<=x+2<self.n and (x+2,y) not in self.blocks and (x+1,y) in state:
                state_cp = [list(el) for el in state]
                state_cp[state_cp.index([x,y])] = [x+2,y]
                state_cp.remove([x+1,y])
                successors[f'Desno: (x={x},y={y})'] = tuple([tuple(el) for el in state_cp])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state)==1 and state[0][0] == self.n // 2


if __name__ == '__main__':
    n = int(input())
    n_balls = int(input())
    balls = tuple()

    for _ in range(n_balls):
        balls += (tuple(map(int, input().split(','))), )

    n_blocks = int(input())
    blocks = tuple()

    for _ in range(n_blocks):
        blocks += (tuple(map(int, input().split(','))), )

    problem = BallGame(balls, blocks, n)
    res = breadth_first_graph_search(problem)

    if res is not None:
        print(res.solution())
    else:
        print('No solution!')