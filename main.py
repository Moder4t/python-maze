

from typing import Optional
from generate_maze_pb import GenerateMaze, MazeState
from node import Node
from search import tree_search, graph_search, breath_first_search, depth_first_search, \
    uniform_cost_search


# initial_state = MazeState(0, 0, 2, 2)
# gm: GenerateMaze = GenerateMaze(initial_state)
# solution: Optional[Node] = tree_search(gm)
# print(solution.solution())

# initial_state = MazeState(0, 0, 2, 2)
# gm: GenerateMaze = GenerateMaze(initial_state)
# solution = graph_search(gm)
# print(solution.solution())

# initial_state = MazeState(0, 0, 4, 3)
# gm: GenerateMaze = GenerateMaze(initial_state)
# solution = breath_first_search(gm)
# print(solution.solution())

# initial_state = MazeState(0, 0, 4, 3)
# gm: GenerateMaze = GenerateMaze(initial_state)
# solution = depth_first_search(gm)
# print(solution.solution())

initial_state = MazeState(0, 0, 3, 3)
gm: GenerateMaze = GenerateMaze(initial_state)
solution = uniform_cost_search(gm)
print(solution.solution())

