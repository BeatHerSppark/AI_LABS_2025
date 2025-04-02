from searching_framework import Problem, breadth_first_graph_search, astar_search

class BallGame(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
        self.size = (8, 6)
        self.invalid_player = {(3,3), (5,4)}
        self.invalid_ball = set()
        self.get_invalid_ball()

    def successor(self, state):
        successors = dict()

        px, py = state[0]
        bx, by = state[1]
        max_x, max_y = self.size[0], self.size[1]

        #push ball
        if (px,py+1) == (bx,by) and by+1 < max_y and (bx,by+1) not in self.invalid_ball:
            successors["Turni topka gore"] = ((px, py+1), (bx, by+1))

        if (px,py-1) == (bx,by) and by-1 >= 0 and (bx,by-1) not in self.invalid_ball:
            successors["Turni topka dolu"] = ((px, py-1), (bx, by-1))

        if (px+1,py) == (bx,by) and bx+1 < max_x and (bx+1,by) not in self.invalid_ball:
            successors["Turni topka desno"] = ((px+1, py), (bx+1, by))

        if (px+1,py+1) == (bx,by) and bx+1 < max_x and by+1 < max_y and (bx+1,by+1) not in self.invalid_ball:
            successors["Turni topka gore-desno"] = ((px+1, py+1), (bx+1, by+1))

        if (px+1,py-1) == (bx,by) and bx+1 < max_x and by-1 >= 0 and (bx+1,by-1) not in self.invalid_ball:
            successors["Turni topka dolu-desno"] = ((px+1, py-1), (bx+1, by-1))

        #move player only
        if py+1 < max_y and (px,py+1) != (bx,by) and (px,py+1) not in self.invalid_player:
            successors["Pomesti coveche gore"] = ((px,py+1), (bx,by))

        if py-1 >=0 and (px,py-1) != (bx,by) and (px,py-1) not in self.invalid_player:
            successors["Pomesti coveche dolu"] = ((px,py-1), (bx,by))

        if px+1 < max_x and (px+1,py) != (bx,by) and (px+1,py) not in self.invalid_player:
            successors["Pomesti coveche desno"] = ((px+1,py), (bx,by))

        if py+1 < max_y and px+1 < max_x and (px+1,py+1) != (bx,by) and (px+1,py+1) not in self.invalid_player:
            successors["Pomesti coveche gore-desno"] = ((px+1,py+1), (bx,by))

        if py-1 >= 0 and px+1 < max_x and (px+1,py-1) != (bx,by) and (px+1,py-1) not in self.invalid_player:
            successors["Pomesti coveche dolu-desno"] = ((px+1,py-1), (bx,by))

        return successors

    def h(self, node):
        ball = node.state[1]
        goal = self.goal[1]

        return abs(ball[0]-goal[0]) + abs(ball[1]-goal[1])

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        ball = state[1]
        return ball in self.goal

    def get_invalid_ball(self):
        base = list(self.invalid_player)
        for x, y in base:
            self.invalid_ball.add((x,y))
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
                self.invalid_ball.add((x+dx, y+dy))


if __name__ == '__main__':
    player = tuple([int(el) for el in input().split(',')])
    ball = tuple([int(el) for el in input().split(',')])
    goal = ((7,2), (7,3))

    game = BallGame((player, ball), goal)
    res = astar_search(game)

    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")