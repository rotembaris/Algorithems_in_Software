import unittest

from Almost_Equitable_Scheduling.Naive_Solutions.LPT import LPT
from Almost_Equitable_Scheduling.Testing.SolutionTest import easy_input, hard_input, even_input, uneven_input


class LPTTest(unittest.TestCase):

    @staticmethod
    def LPT_solution(input):
        tasks, machines = input[0], input[1]
        solution = LPT(tasks, machines)
        print("\nLPT {INPUT_NAME}"
              "\n{SOLUTION}"
              "\ngoal function: {MIN_WEIGHT}"
              # "\nleast tasks: {MIN_TASK}"
              # "\nmost tasks: {MAX_TASK}"
              "".format(
                INPUT_NAME=input[2], SOLUTION=str(solution),
                MIN_WEIGHT=str(min(solution.machines).weight),
                MIN_TASK=str(min(solution.machines, key=lambda m: m.task_num).task_num),
                MAX_TASK=str(max(solution.machines, key=lambda m: m.task_num).task_num)))
        return solution

    def test_LPT(self):
        self.LPT_solution(easy_input())
        self.LPT_solution(hard_input())
        self.LPT_solution(even_input())
        self.LPT_solution(uneven_input())
        return True


if __name__ == '__main__':
    unittest.main()
