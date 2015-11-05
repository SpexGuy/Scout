import sys
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

def printProblemsToStderr():
    # go through the members of problems, and print the ones which aren't builtins or the base class
    for item in problems.__dict__:
        if not item.startswith("__") and item != "Problem":
            sys.stderr.write(item + "\n")


if (__name__ == '__main__'):
    if len(sys.argv) > 1:
        try:
            if sys.argv[1].startswith("__") or sys.argv[1] == "Problem":
                raise AttributeError
            problem = getattr(problems, sys.argv[1])()
        except AttributeError:
            sys.stderr.write("Couldn't find class or function %s in problems.py\n" % (sys.argv[1]))
            sys.stderr.write("Options are:\n")
            printProblemsToStderr()
            sys.exit(1)
        except TypeError:
            sys.stderr.write("Failed to invoke %s. problems.%s must be a function or class which takes no arguments.\n" % (sys.argv[0], sys.argv[0]))
            sys.exit(2)
    else:
        sys.stderr.write("No problem specified. Defaulting to the Cannibal Problem.\n")
        sys.stderr.write("To specify a problem, use 'python %s <problem>', where problem is one of:\n" % (sys.argv[0]))
        printProblemsToStderr()
        problem = problems.CannibalProblem()

    search(problem)
