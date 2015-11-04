from collections import deque

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

class Node:
    index = 0
    def __init__(self, state, valid):
        self.state = state
        self.valid = valid
        self.successors = set()
        self.id = "S_%d" % (Node.index)
        Node.index += 1

def search(problem):
    state = problem.getStartState()
    print "// Searching starting at %s" % (problem.getStringRepr(state))
    print "digraph {"

    startnode = Node(state, problem.isValidState(state))
    print "    %s [label=\"%s\"]" % (startnode.id, problem.getStringRepr(state))
    seen = dict({state: startnode})
    frontier = deque([startnode])
    while frontier:
        node = frontier.popleft()
        if node.valid:
            for successor in problem.getSuccessors(node.state):
                if successor in seen:
                    node.successors.add(seen[successor])
                    print "    %s -> %s;" % (node.id, seen[successor].id)
                else:
                    succnode = Node(successor, problem.isValidState(successor))
                    node.successors.add(succnode)
                    seen[successor] = succnode
                    frontier.append(succnode)
                    print "    %s [label=\"%s\"]" % (succnode.id, problem.getStringRepr(succnode.state))
                    print "    %s -> %s;" % (node.id, succnode.id)
    print "}"



if (__name__ == '__main__'):
    problem = SquareProblem(2);
    search(problem)
