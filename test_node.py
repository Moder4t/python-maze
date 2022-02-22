

from typing import List
from generate_maze_pb import GenerateMaze, MazeState, MazeAction
from node import Node


class TestNode:
    def test_create_initial_node(self):
        # Arrange
        state: MazeState = MazeState(0, 0, 2, 3)
        gm: GenerateMaze = GenerateMaze(state)

        # Act
        node: Node = Node(gm.initial)

        # Assert
        print(gm.initial)
        assert node.state == gm.initial \
               and node.parent is None \
               and node.action is None \
               and node.depth == 0

    def test_child_node(self):
        # Arrange
        initial: MazeState = MazeState(1, 1, 3, 3)
        gm: GenerateMaze = GenerateMaze(initial)
        node: Node = Node(initial)

        # act
        child: Node = node.child_node(gm, MazeAction.RIGHT)

        # Assert
        assert child.action == MazeAction.RIGHT and \
               child.state.col == 2 and \
               child.state.row == 1

    def test_expand_initial_node(self):

        # Arrange
        state: MazeState = MazeState(1, 1, 3, 3)
        gm: GenerateMaze = GenerateMaze(state)

        # Act
        node: Node = Node(gm.initial)
        children: List[Node] = node.expand(gm)

        # assert
        assert len(children) is 4
