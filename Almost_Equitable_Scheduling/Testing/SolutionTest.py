import unittest


def easy_input():
    tasks = [(1, 1), (2, 2), (3, 4), (4, 7), (5, 9), (6, 13), (7, 16), (8, 19), (9, 21)]
    machine_num = 3
    return tasks, machine_num, "EASY"


def hard_input():
    tasks = [(1, 1), (2, 2), (3, 3), (4, 5), (5, 6), (6, 7), (7, 8), (8, 13), (9, 21), (10, 28), (11, 34), (12, 47),
             (13, 55), (14, 64),
             (15, 66), (16, 68), (17, 77), (18, 89), (19, 93), (20, 98)]
    machine_num = 5
    return tasks, machine_num, "HARD"


def uneven_input():
    tasks = [(1, 1), (2, 2), (3, 3), (4, 5), (5, 6), (6, 7), (7, 8), (8, 13), (9, 21), (10, 28), (11, 34), (12, 47),
             (13, 55), (14, 64),
             (15, 66), (16, 68), (17, 77), (18, 89), (19, 93), (20, 1198)]
    machine_num = 5
    return tasks, machine_num, "UNEVEN"


def even_input():
    tasks = [(1, 3), (2, 3), (3, 3), (4, 3), (5, 4), (6, 4), (7, 4), (8, 6), (9, 6)]
    machine_num = 3
    return tasks, machine_num, "EVEN"


class SolutionTest(unittest.TestCase):
    def test_Solution(self):
        pass


if __name__ == '__main__':
    unittest.main()
