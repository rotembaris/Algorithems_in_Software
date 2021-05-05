from Almost_Equitable_Scheduling.Machine import Machine
import copy


class Solution:

    def __init__(self, tasks: [tuple], machine_num: int):
        self.tasks = tasks
        self.machines = [Machine() for _ in range(machine_num)]
        self.machineNum = machine_num

    def __str__(self):
        return "".join(f'{i+1}: {machine}\n ' for i, machine in enumerate(self.machines))

    def value(self):
        value = min(self.machines)
        return value

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
