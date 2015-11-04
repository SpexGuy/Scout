# Python does not require explicit interfaces,
# but I believe that code which does is more
# maintainable. Thus I include this explicit
# interface for Problems.
class Problem:
    def getStartState(self):
        return None

    def getEndState(self):
        return None

    def isValidState(self, state):
        return False

    def getSuccessors(self, state):
        return []

    def getStringRepr(self, state):
        return "BadProblem"


class SquareProblem(Problem):
    def __init__(self, size):
        self.size = size

    def getStartState(self):
        return (0, 0)

    def getEndState(self):
        return (self.size, self.size)

    def isValidState(self, state):
        return 0 <= state[0] <= self.size and 0 <= state[1] <= self.size

    def getSuccessors(self, state):
        return [(state[0]+dx, state[1]+dy) for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    def getStringRepr(self, state):
        return "(%d, %d)" % state


class CannibalProblem(Problem):
    def getStartState(self):
        return (3, 3, False)

    def getEndState(self):
        return (0, 0, True)

    def isValidState(self, state):
        return (state[0] >= state[1] or state[0] == 0) and (state[1] >= state[0] or state[0] == 3)

    def getSuccessors(self, state):
        if state[2]:
            if state[0] < 3:
                yield (state[0]+1, state[1], not state[2])
            if state[0] < 2:
                yield (state[0]+2, state[1], not state[2])
            if state[1] < 3:
                yield (state[0], state[1]+1, not state[2])
            if state[1] < 2:
                yield (state[0], state[1]+2, not state[2])
            if state[0] < 3 and state[1] < 3:
                yield (state[0]+1, state[1]+1, not state[2])
        else:
            if state[0] > 0:
                yield (state[0]-1, state[1], not state[2])
            if state[0] > 1:
                yield (state[0]-2, state[1], not state[2])
            if state[1] > 0:
                yield (state[0], state[1]-1, not state[2])
            if state[1] > 1:
                yield (state[0], state[1]-2, not state[2])
            if state[0] > 0 and state[1] > 0:
                yield (state[0]-1, state[1]-1, not state[2])

    def getStringRepr(self, state):
        return "o"*state[0] + "x"*state[1] + (">" if state[2] else "<") + "o"*(3-state[0]) + "x"*(3-state[1])
