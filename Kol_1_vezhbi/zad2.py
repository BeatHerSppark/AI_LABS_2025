from searching_framework import Problem, breadth_first_graph_search, astar_search

class HanoiGame(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        pillars = [list(el) for el in state]

        for i in range(len(pillars)):
            if len(pillars[i]) == 0: continue

            pillar = pillars[i]
            top = pillar[-1]

            for j in range(len(pillars)):
                if j==i: continue

                if len(pillars[j])==0 or pillars[j][-1] >= top:
                    pillars_cp = [el[:] for el in pillars]
                    pillars_cp[j].append(pillars_cp[i].pop())
                    successors[f"MOVE TOP BLOCK FROM PILLAR {i+1} TO PILLAR {j+1}"] = tuple([tuple(el) for el in pillars_cp])

        return successors

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return state == self.goal


def get_input():
    inp = list(input())
    pillars = inp.count(";")+1
    donuts = tuple([int(num) for num in inp if num.isnumeric()])

    idx_init = -1
    for i in range(len(inp)):
        if inp[i].isnumeric():
            idx_init = i
            break

    state = []
    for i in range(pillars):
        if i == idx_init:
            state.append(donuts)
        else:
            state.append(())

    return state

if __name__ == '__main__':

    initial_state = get_input()
    goal_state = get_input()

    problem = HanoiGame(tuple(initial_state), tuple(goal_state))
    res = breadth_first_graph_search(problem)

    if res is not None:
        solution = res.solution()
        print(f"Number of action {len(solution)}")
        print(solution)
    else:
        print("No solution!")
