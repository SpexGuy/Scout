from collections import deque
import problems

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
                    print "    %s [label=\"%s\" color=%s]" % (succnode.id, problem.getStringRepr(succnode.state), "black" if succnode.valid else "red")
                    print "    %s -> %s;" % (node.id, succnode.id)
    print "}"



if (__name__ == '__main__'):
    problem = problems.SquareProblem(2)
    search(problem)
