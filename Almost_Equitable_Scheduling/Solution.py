from Almost_Equitable_Scheduling.Machine import Machine
import copy


class Solution:

    def __init__(self, tasks: [tuple], machine_num: int):
        self.tasks = tasks
        self.machines = [Machine() for i in range(machine_num)]
        self.machineNum = machine_num

    def __str__(self):
        string = ""
        for i in range(self.machineNum):
            string += str(i+1) + ": " + str(self.machines[i]) + "\n"
        return string

    def value(self):
        value = min(self.machines)
        return value

    @staticmethod
    def is_better_solution(solution1, solution2):
        return solution1.value() > solution2.value()

    def set_machines(self, machines: [Machine]):
        self.machines = machines

    """
    create full order on the solutions, based on their value
    """

    def __eq__(self, other):
        return self.value() == other.value()

    def __ne__(self, other):
        return self.value() != other.value()

    def __lt__(self, other):
        return self.value() < other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __copy__(self):
        solution_copy = Solution(self.tasks, self.machineNum)
        solution_copy.machines = [copy.copy(machine) for machine in self.machines]
        return copy

