from searching_framework import Problem, breadth_first_graph_search


class Snake(Problem):
    def __init__(self, initial, red_apples):
        super().__init__(initial)
        self.red_apples = red_apples
        self.size = 10

    def successor(self, state):
        successors = dict()

        snake = list(state[0])
        green_apples = state[1]
        direction = state[2]
        head_x, head_y = snake[-1][0], snake[-1][1]

        if direction == 'Down':
            for (dx, dy, action, new_dir) in [(0,-1,'ProdolzhiPravo', 'Down'), (-1,0,'SvrtiDesno', 'Left'), (1,0,'SvrtiLevo', 'Right')]:
                new_state = self.create_successors(dx, dy, head_x, head_y, snake, green_apples, new_dir)
                if new_state:
                    successors[action] = new_state
        elif direction == 'Up':
            for (dx, dy, action, new_dir) in [(0,1,'ProdolzhiPravo', 'Up'), (-1,0,'SvrtiLevo', 'Left'), (1,0,'SvrtiDesno', 'Right')]:
                new_state = self.create_successors(dx, dy, head_x, head_y, snake, green_apples, new_dir)
                if new_state:
                    successors[action] = new_state
        elif direction == 'Left':
            for (dx, dy, action, new_dir) in [(-1,0,'ProdolzhiPravo', 'Left'), (0,1,'SvrtiDesno', 'Up'), (0,-1,'SvrtiLevo', 'Down')]:
                new_state = self.create_successors(dx, dy, head_x, head_y, snake, green_apples, new_dir)
                if new_state:
                    successors[action] = new_state
        elif direction == 'Right':
            for (dx, dy, action, new_dir) in [(1,0,'ProdolzhiPravo', 'Right'), (0,1,'SvrtiLevo', 'Up'), (0,-1,'SvrtiDesno', 'Down')]:
                new_state = self.create_successors(dx, dy, head_x, head_y, snake, green_apples, new_dir)
                if new_state:
                    successors[action] = new_state

        return successors

    def create_successors(self, dx, dy, head_x, head_y, snake, green_apples, new_dir):
        nx, ny = head_x+dx, head_y+dy
        if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in snake[1:] and (nx, ny) not in self.red_apples:
            snake_cp = list(snake)
            snake_cp.append((nx, ny))
            green_apples_cp = list(green_apples)
            if (nx, ny) in green_apples_cp:
                green_apples_cp.remove((nx, ny))
            else:
                snake_cp.pop(0)
            return (tuple(snake_cp), tuple(green_apples_cp), new_dir)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0


if __name__ == '__main__':
    n_green_apples = int(input())
    green_apples = []
    for _ in range(n_green_apples):
        green_apples.append(tuple([int(el) for el in input().split(',')]))

    n_red_apples = int(input())
    red_apples = []
    for _ in range(n_red_apples):
        red_apples.append(tuple([int(el) for el in input().split(',')]))

    snake = Snake((((0,9),(0,8),(0,7)), tuple(green_apples), "Down"), red_apples)

    res = breadth_first_graph_search(snake)

    if res is not None:
        print(res.solution())
    else:
        print("")