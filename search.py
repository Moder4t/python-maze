

from collections import deque
from queue import PriorityQueue
import random
from typing import Optional, List
from node import Node


class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, __init__ and goal_test
    Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial: 'State'):
        """The constructor specifies the initial state,
        Your subclass's constructor can add
        other arguments."""
        self.initial: 'State' = initial

    def get_actions(self, state: 'State') -> List['MazeAction']:
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state: 'State', action: 'MazeAction') -> Optional['State']:
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state: 'State') -> bool:
        """Return True if the state is a goal."""
        raise NotImplementedError


def tree_search(problem: Problem, use_random: bool = True) -> Optional[Node]:
    frontier: List[Node] = [Node(problem.initial)]

    while len(frontier) > 0:
        node: Node = random.choice(frontier) if use_random else frontier[0]
        frontier.remove(node)
        if problem.goal_test(node.state):
            return node

        frontier.extend(node.expand(problem))
    return None


def graph_search(problem: Problem, use_random: bool = True) -> Optional[Node]:
    frontier: List[Node] = [Node(problem.initial)]
    explored: List[Node] = []
    while frontier:
        node: Node = random.choice(frontier) if use_random else frontier[0]
        frontier.remove(node)
        if problem.goal_test(node.state):
            return node
        explored.append(node)
        children = node.expand(problem)
        for child in children:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None


# Breath First Search (BFS) - Implemented using a queue (FIFO)
def breath_first_search(problem: Problem) -> Optional[Node]:
    frontier: deque = deque([Node(problem.initial)])
    frontier.append(Node(problem.initial))
    explored: List[Node] = []
    while frontier:
        node: Node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        explored.append(node)
        children = node.expand(problem)
        for child in children:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None


# Depth First Search (DFS) - Implemented using a stack (LIFO)
def depth_first_search(problem: Problem) -> Optional[Node]:
    frontier: List[Node] = [Node(problem.initial)]
    explored: List[Node] = []
    while len(frontier) > 0:
        node: Node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.append(node)
        children = node.expand(problem)
        for child in children:
            if child not in explored:
                frontier.append(child)
    return None


# Uniform cost search (UCS) - Implementation is using automatically sorted list by depth (PriorityQueue)
def uniform_cost_search(problem: Problem) -> Optional[Node]:
    frontier: PriorityQueue = PriorityQueue()
    frontier.put(Node(problem.initial))
    explored: List[Node] = []
    while not frontier.empty():
        node: Node = frontier.get()
        if problem.goal_test(node.state):
            return node
        explored.append(node)
        children: List[Node] = node.expand(problem)
        for child in children:
            if child not in explored:
                frontier.put(child)
    return None
