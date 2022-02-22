from queue import *
from typing import List
from node import *


class Test_labo_01_deux:
    def test_exercise_5_a(self):
        queue_un: List[int] = [3, 6, 7]
        estimated_number: int = 3

        assert queue_un.pop(0) == estimated_number

    def test_exercise_5_b(self):
        queue_un: List[int] = [3, 6, 7]
        estimated_number: int = 7

        assert queue_un.pop() == estimated_number

    def test_exercise_5_c(self):
        queue_un: Queue = Queue()
        queue_un.put(1)
        queue_un.put(2)
        queue_un.put(3)
        estimated_number: int = 1

        assert queue_un.get() == estimated_number

    def test_exercise_5_d(self):
        queue_un: LifoQueue = LifoQueue()
        queue_un.put(1)
        queue_un.put(2)
        queue_un.put(3)
        estimated_number: int = 3

        assert queue_un.get() == estimated_number

    def test_exercise_5_e(self):
        queue_node: "PriorityQueue[(int, Node)]" = PriorityQueue()
        child_un: Node = (0, 1)
        child_deux: Node = (0, 2, child_un)
        child_trois: Node = (0, 3, child_deux)
        queue_node.put(3, child_un)
        queue_node.put(2, child_deux)
        queue_node.put(1, child_trois)

        estimated_node: Node = Node(0, 3)

        assert queue_node.get() == estimated_node

    def test_exercise_5_f(self):
        queue_un: List[int] = [3, 6, 7]
        estimated_number: int = 7

        assert queue_un.pop() == estimated_number


