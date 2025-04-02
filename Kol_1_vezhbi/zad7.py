from searching_framework import Problem, breadth_first_graph_search, astar_search

# -1 = White, 1 = Black
class Game(Problem):
    def __init__(self, initial, n):
        super().__init__(initial, None)
        self.n = n

    def successor(self, state):
        successors = dict()

        coords = state[0]

        for i in range(len(coords)):
            colors = list(state[1])

            (x,y) = coords[i]
            colors[i] = -colors[i]

            neighbors = [(x+dx,y+dy) for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)] if 0<=x+dx<self.n and 0<=y+dy<self.n]
            for neighbor in neighbors:
                idx = coords.index(neighbor)
                colors[idx] = -colors[idx]

            successors[f"x: {x}, y: {y}"] = (coords, tuple(colors))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        for c in state[1]:
            if c == -1:
                return False
        return True


if __name__ == '__main__':
    n = int(input())
    fields = [int(el) if el=="1" else -1 for el in input().split(",")]

    coords = []

    for i in range(n):
        for j in range(n):
            coords.append((i, j))

    initial_state = (tuple(coords), tuple(fields))

    problem = Game(initial_state, n)
    res = breadth_first_graph_search(problem)

    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")
