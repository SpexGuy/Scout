# Scout
A search space expander for small problems

## Usage
Scout is meant for usage with the `dot` graph visualizer, which can be obtained as part of the GraphViz project.
On mac, `brew install graphviz` will install it.

Once you have `dot`, type `python scout.py <problem> | dot -Tpng > out.png` to render the graph of `problem` to `out.png`.

To get a list of problems, type `python scout.py Problem`.

## Creating problems
Problems, defined in problems.py, are classes which implement the Problem interface.

A Problem explicitly defines the functions:
```
    __init__(self) - Problems must have a default constructor
    getStartState(self) - returns the start state.
    getEndState(self) - returns the end state. Currently unused.
    isValidState(self, state) - returns True iff the given state is valid
    getSuccessors(self, state) - returns or generates a sequence of successor states
    getStringRepr(self, state) - returns the string label for a state
```
A problem also implicitly defines its own states. These may use whatever representation the Problem deems appropriate.  The scout program will not modify or inspect them.  It will merely pass them back to the Problem whenever it needs information about them.

Scout uses reflection to inspect the contents of problems.py.  For you, this means that the program will automatically detect your Problem and add it to the list of available problems.
