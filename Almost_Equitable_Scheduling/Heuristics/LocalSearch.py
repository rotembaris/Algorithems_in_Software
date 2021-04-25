from Almost_Equitable_Scheduling.Solution import Solution
from Almost_Equitable_Scheduling.Naive_Solutions.LPT import LPT
from Almost_Equitable_Scheduling.Machine import Machine
import copy
import itertools
import time


class LocalSearch(Solution):

    def __init__(self, tasks: [tuple], machine_num: int, loop_num: int = 2):
        super().__init__(tasks, machine_num)
        self.machines = LPT(self.tasks, self.machineNum).machines
        self.n = int(len(tasks) / machine_num)
        self.loopNum = loop_num
        self.start_time = time.time()
        solution = self.loop_search_secondary()
        # solution = self.local_search()
        self.end_time = time.time()
        print(str(self.end_time - self.start_time))
        self.machines = solution

    @staticmethod
    def task_iterator(machines: [Machine]) -> ([Machine], [tuple]):
        for machine in machines:
            for task in machine.Tasks:
                yield machine, task

    def local_search(self) -> [Machine]:
        search_area = 1
        machines = [copy.copy(mach) for mach in self.machines]
        while search_area <= self.loopNum:
            loop_iter = self.loop_search(search_area, machines)
            for change in loop_iter:
                if self.square_value(change) < self.square_value(self.machines):
                    if max(change).weight - min(change).weight <= 1:
                        return change
                    self.machines = change
                    return self.local_search()
            search_area += 1
        return self.machines

    def local_search_secondary(self):
        for change in self.loop_search_secondary():
            if self.square_value(change) < self.square_value(self.machines):
                    if max(change).weight - min(change).weight <= 1:
                        return change
                    self.machines = change
                    return self.local_search()

    def loop_search_secondary(self):
        search_area = 1
        machines = [copy.copy(mach) for mach in self.machines]
        while search_area <= self.loopNum:
            task_iter = self.task_iterator(machines)
            combinator = itertools.combinations(task_iter, search_area)
            for task_combination in sorted(combinator, key=lambda m: m[0][1][1], reverse=True):
                for old_machine, task in task_combination:
                    old_machine.remove_task(task[0])
                options = [list(zip(x, task_combination)) for x in itertools.permutations(machines, len(task_combination))]
                for option in options:
                    flag = True
                    for (new_machine, (old_machine, task)) in option:
                        if new_machine != old_machine and new_machine.is_legal_amount(self.n - 1):
                            new_machine.add_task(task)
                        else:
                            flag = False
                            break
                    if flag \
                            and self.square_value(machines) < self.square_value(self.machines) \
                            and min(machines, key=lambda m: m.taskNum).is_legal_amount(self.n):
                        print(task)
                        print(new_machine)
                        print("->")
                        print(old_machine)
                        self.machines = machines
                        return self.loop_search_secondary()

                    for (new_machine, (old_machine, task)) in option:
                        if new_machine != old_machine and new_machine.has_task(task[0]):
                            new_machine.remove_task(task[0])
                for orig_machine, task in task_combination:
                    orig_machine.add_task(task)
            search_area += 1

    def loop_search(self, search_area: int, machines: [Machine]) -> [Machine]:
        tasks = []
        remove_iter = self.remove_tasks(search_area, machines, tasks)
        for tasks, solutions in remove_iter:
            copy_tasks = [(copy.copy(tm[0]), tm[1]) for tm in tasks]
            add_iter = self.add_tasks(copy_tasks, solutions)
            for sol in add_iter:
                yield sol

    def remove_tasks(self, search_area: int, machines: [Machine], tasks: [tuple] = []) -> ([tuple], [Machine]):
        task_iter = self.task_iterator(machines)
        combinator = itertools.combinations(task_iter, search_area)
        for task_combination in sorted(combinator, key=lambda m: m[0][1][1], reverse=True):
            for machine, task in task_combination:
                machine.remove_task(task[1])
                tasks.append((task, machine))
            yield tasks, machines
            for machine, task in task_combination:
                machine.add_task(task)
                tasks.remove((task, machine))

    def add_tasks(self, tasks: [tuple], machines: [Machine]) -> [Machine]:
        for task in tasks:
            for machine in sorted(machines):
                if task[1] != machine and machine.is_legal_amount(self.n - 1):
                    machine.add_task(task[0])
                    tasks.remove(task)
                    if len(tasks) > 0:
                        add_iterator = self.add_tasks(tasks, machines)
                        for sub_solution in add_iterator:
                            yield sub_solution
                    else:
                        if min(machines, key=lambda m: m.taskNum).is_legal_amount(self.n):
                            yield machines
                    machine.remove_task(task[0][0])
                    tasks.append(task)

    @staticmethod
    def square_value(machines: [Machine]) -> int:
        square_weight = 0
        for machine in machines:
            square_weight += machine.weight ** 2
        return square_weight
