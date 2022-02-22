# https://stackoverflow.com/questions/15853469/putting-current-class-as-return-type-annotation
from __future__ import annotations
from typing import Optional

import string


class Node:

    def __init__(self, state, parent=None, action=None):
        """Créer un noeud dans un arbre/graphe de recherche,
        excepté le noeud de départ, un noeud est dérivé d'un parent par une action.
        state est l'information du noeud courant, notez que si un state est obtenu
        par 2 chemins différents il y a alors 2 noeuds différents dans l'arbre ou le graphe
        avec le même état
        vous devez utiliser cette classe telle quelle sans la dériver
        """
        self.state: 'State' = state
        self.parent: Optional[Node] = parent
        self.action: Optional['MazeAction'] = action
        self.depth: int = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem: 'Problem') -> [Node]:
        """Retourne la liste de noeuds atteignables par chacune des actions disponibles selon le state de ce noeud."""
        state_actions: ['MazeAction'] = problem.get_actions(self.state)
        child_nodes: [Node] = []
        for action in state_actions:
            next_node = self.child_node(problem, action)
            child_nodes.append(next_node)
        return child_nodes

    def child_node(self, problem: 'Problem', action: 'MazeAction') -> Node:
        """Crée le noeud atteignable à partir du noeud courant selon l'action passée en paramètre."""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node

    def solution(self) -> ['MazeAction']:
        """Retourne la solution sous forme d'une séquence d'actions pour se déplacer de la racine à ce noeud."""
        return [node.action for node in self.path()[1:]]

    def path(self) -> [Node]:
        """Retourne le chemin composé des noeuds pour se déplacer de la racine à ce noeud."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __str__(self) -> string:
        if self.state:
            description = f'Node state {self.state}'
            description += f'Parent state {self.parent.state}' if self.parent else 'No parent'
            return description
        else:
            return f'No state'

    def __eq__(self, other_class: Node) -> bool:
        return isinstance(other_class, Node) and self.state == other_class.state

    def __lt__(self, other):
        return self.depth < other.depth


