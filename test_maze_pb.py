from typing import List, Optional
from node import Node
from generate_maze_pb import GenerateMaze, MazeState, MazeAction
from search import tree_search


class TestMazePb:
    def test_actions_from_00(self):
        initial_state = MazeState(0, 0, 2, 1)
        gm: GenerateMaze = GenerateMaze(initial_state)
        actions: List[MazeAction] = gm.get_actions(gm.initial)
        assert actions == [MazeAction.RIGHT]

    def test_actions_from_10(self):
        state: MazeState = MazeState(1, 0, 2, 1)
        gm: GenerateMaze = GenerateMaze(state)
        actions: List[MazeAction] = gm.get_actions(gm.initial)
        assert actions == [MazeAction.LEFT]

    def test_result_from_00_to_south(self):
        state: MazeState = MazeState(0, 0, 2, 1)
        gm: GenerateMaze = GenerateMaze(state)
        actions: List[MazeAction] = gm.get_actions(gm.initial)
        assert actions == [MazeAction.RIGHT]

    def test_goal_success(self):
        initial_state = MazeState(0, 0, 2, 2)
        gm: GenerateMaze = GenerateMaze(initial_state)
        next_cell = gm.result(gm.initial, MazeAction.RIGHT)
        next_cell = gm.result(next_cell, MazeAction.BOTTOM)
        next_cell = gm.result(next_cell, MazeAction.LEFT)
        assert gm.goal_test(next_cell) is True

    def test_goal_echec(self):
        initial_state = MazeState(0, 0, 2, 2)
        gm: GenerateMaze = GenerateMaze(initial_state)
        next_cell = gm.result(gm.initial, MazeAction.RIGHT)
        next_cell = gm.result(next_cell, MazeAction.BOTTOM)
        next_cell = gm.result(next_cell, MazeAction.TOP)
        assert gm.goal_test(next_cell) is False

    def test_tree_search(self):
        initial_state = MazeState(0, 0, 2, 2)
        gm: GenerateMaze = GenerateMaze(initial_state)
        expected_solution = [MazeAction.RIGHT, MazeAction.BOTTOM, MazeAction.LEFT]
        node: Optional[Node] = tree_search(gm, False)
        assert node.solution() == expected_solution
