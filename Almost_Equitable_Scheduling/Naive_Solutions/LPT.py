from Almost_Equitable_Scheduling.Solution import Solution
from Almost_Equitable_Scheduling.Machine import Machine


class LPT(Solution):

    def __init__(self, tasks, machine_num):
        tasks = sorted(tasks, key=lambda t: t[1])
        super().__init__(tasks, machine_num)

    def LPT_solution(self) -> [Machine]:
        n = 0
        m = self.machineNum
        while len(self.tasks) > 0:
            task = self.tasks.pop()  # will pop heaviest task
            n += 1
            dev = int(n / m)  # rounded downwards
            min_machine = min(self.machines, key=lambda mach: mach.task_num)
            if not min_machine.is_legal_amount(dev):  # is the machine with the least tasks legal
                min_machine.add_task(task)  # if not make it legal
            else:
                for machine in sorted(self.machines):
                    if machine.is_legal_amount(dev-1):
                        machine.add_task(task)
                        break  # continue to next task
        return self.machines

