
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


def search(problem):
    print "Searching..."



if (__name__ == '__main__'):
    problem = Problem();
    search(problem)
