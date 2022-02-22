from generate_maze_pb import MazeState


class Test_labo_01:

    def test_exercise_4_a(self):
        matrice_un = [[1, 2, 3], [4, 5, 6]]
        matrice_deux = [[1, 2, 3], [4, 5, 6]]

        assert matrice_un == matrice_deux

    def test_exercise_4_b(self):
        matrice_un = [[1, 2, 3], [4, 5, 6]]
        matrice_deux = [[1, 2, 3], [4, 5, 6]]

        assert id(matrice_un) != id(matrice_deux)

    def test_exercise_4_c(self):
        liste_un = [
            MazeState(0, 0, 1, 2),
            MazeState(0, 0, 1, 3),
            MazeState(0, 0, 1, 4)
        ]
        liste_deux = [
            MazeState(0, 0, 1, 2),
            MazeState(0, 0, 1, 3),
            MazeState(0, 0, 1, 4),
        ]

        assert liste_un == liste_deux

    def test_exercise_4_d(self):
        matrice_un = [
            MazeState(0, 0, 1, 2),
            MazeState(0, 0, 1, 3),
            MazeState(0, 0, 1, 4)
        ]
        matrice_deux = [
            MazeState(0, 0, 1, 2),
            MazeState(0, 0, 1, 3),
            MazeState(0, 0, 1, 4),
        ]

        assert id(matrice_un) != id(matrice_deux)