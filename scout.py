
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
        return 0 <= state[0] <= self.size and
               0 <= state[1] <= self.size

    def getSuccessors(self, state):
        return [(state[0]+dx, state[1]+dy) for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

    def getStringRepr(self, state):
        return "(%d, %d)" % state


def search(problem):
    print "Searching..."



if (__name__ == '__main__'):
    problem = SquareProblem(2);
    search(problem)
