"""
Generation de labyrinthe:

Etat:
- Nos cellules.

Etat initial:
- Une grille jamais visiter, avec un point initial (example: (0,0))

MazeAction:
- Verification des voisins valides (A l'interieur de la grille)

Transition:
- F(position(0,0)), Allez (0,1) = Dans (0,1)
        position de depart vers la 2e position.
        NSEW

Test de but:
- Quand toute les cellules ont ete visite.

Cout:
- Le nombres de deplacements. (1 par deplacements)


taille = 2 expr (hauteur:2 * largeur:3)


"""
from __future__ import annotations

from enum import Enum
from typing import Optional, List

from search import Problem


class MazeAction(Enum):
    LEFT = 1
    TOP = 2
    RIGHT = 3
    BOTTOM = 4


class MazeState:
    def __init__(self, col: int, row: int, width: int, height: int):

        self.width = width
        self.height = height
        self.col: int = col
        self.row: int = row
        self.visited_matrix: List = [[False for _ in range(self.width)] for _ in range(self.height)]

    def __str__(self):
        return f"({self.col}, {self.row})"

    def __eq__(self, state) -> bool:
        # if either both rows or both cols don't match then return false
        if not (isinstance(state, MazeState) and
                self.col == state.col and
                self.row == state.row):
            return False
        # if both matrix don't match then return false
        for row in range(self.height):
            for col in range(self.width):
                if self.visited_matrix[row][col] != state.visited_matrix[row][col]:
                    return False
        return True

    def clone(self):
        state: MazeState = MazeState(self.col, self.row, self.width, self.height)
        for row in range(self.height):
            for col in range(self.width):
                state.visited_matrix[row][col] = self.visited_matrix[row][col]
        return state

    def move(self, action: MazeAction):
        if action == MazeAction.LEFT:
            self.col -= 1
        elif action == MazeAction.RIGHT:
            self.col += 1
        elif action == MazeAction.TOP:
            self.row -= 1
        elif action == MazeAction.BOTTOM:
            self.row += 1
        self.visited_matrix[self.row][self.col] = True


class GenerateMaze(Problem):
    def __init__(self, initial: MazeState):
        super().__init__(initial)
        initial.visited_matrix[initial.row][initial.col] = True

    def get_actions(self, state: MazeState) -> List[MazeAction]:
        actions: List[MazeAction] = []
        if state.col > 0:
            actions.append(MazeAction.LEFT)
        if state.col < state.width - 1:
            actions.append(MazeAction.RIGHT)
        if state.row > 0:
            actions.append(MazeAction.TOP)
        if state.row < state.height - 1:
            actions.append(MazeAction.BOTTOM)
        return actions

    def result(self, state: MazeState, action: MazeAction) -> Optional[MazeState]:
        new: MazeState = state.clone()
        new.move(action)
        return new

    def goal_test(self, state: MazeState) -> bool:
        for r in range(state.height):
            for c in range(state.width):
                if not state.visited_matrix[r][c]:
                    return False
        return True
