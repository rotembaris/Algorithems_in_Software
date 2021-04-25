import random
import unittest

from Almost_Equitable_Scheduling.Heuristics.LocalSearch import LocalSearch
from Almost_Equitable_Scheduling.IO_module import IOModule
from Almost_Equitable_Scheduling.Testing.LPTTest import LPTTest
from Almost_Equitable_Scheduling.Testing.SolutionTest import even_input


def random_input():
    arr = []
    m = random.randrange(3, 15)
    n = random.randrange(3*m, min(15*m, int(1000/m)))
    while len(arr) < n*m:
        num = random.random()
        num = int(1 / num)
        if num >= 5:
            arr.append((len(arr), num))
    return arr, m, "_{M}_{N}".format(M=m, N=n)


class LocalSearchTest(unittest.TestCase):

    @staticmethod
    def LocalSearch_solution(input):
        tasks, machines = input[0], input[1]
        solution = LocalSearch(tasks, machines)
        print("\nLocal Search {INPUT_NAME}"
              "\n{SOLUTION}"
              "\ngoal function: {MIN_WEIGHT}"
              "".format(
                INPUT_NAME=input[2], SOLUTION=str(solution),
                MIN_WEIGHT=str(min(solution.machines).weight),
                MIN_TASK=str(min(solution.machines, key=lambda m: m.taskNum).taskNum),
                MAX_TASK=str(max(solution.machines, key=lambda m: m.taskNum).taskNum)))
        return solution

    def test_LocalSearch(self):
        self.io = IOModule()
        for i in range(1):
            self.io.create_input_file(random_input())
        for file in self.io.file_arrays:
            i = self.io.load_input(file)
            self.io.save_output(LPTTest.LPT_solution(i), file, "LPT "+i[2])
            self.io.save_output(self.LocalSearch_solution(i), file, "Local Search "+i[2])
        return True


if __name__ == '__main__':
    unittest.main()
