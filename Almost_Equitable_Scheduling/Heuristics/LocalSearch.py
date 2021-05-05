from Almost_Equitable_Scheduling.Solution import Solution
from Almost_Equitable_Scheduling.Naive_Solutions.LPT import LPT
import itertools
import logging


class LocalSearch(Solution):

    def __init__(self, tasks: [tuple], machine_num: int, loop_num: int = 3):
        super().__init__(tasks, machine_num)
        self.n = int(len(tasks) / machine_num)
        self.m = machine_num
        self.search_area = loop_num
        self.log = logging.getLogger(f"{machine_num}_{self.n}")

    def local_search(self):
        self.machines = sorted(LPT(self.tasks, self.machineNum).machines, reverse=True)
        if self.machines[0].weight - self.machines[-1].weight <= 1:
            self.log.info("LPT solution is optimal")
            return self.machines
        area_index = 1
        while area_index <= self.search_area:
            option_iter = self.option_iterator(area_index)
            for option in option_iter:
                if self.try_option(option):
                    if self.accept_change(option):
                        return
                    area_index = 0
                    break
                else:
                    self.reverse_option(option)
            area_index += 1
        return

    def try_option(self, option):
        val = -(option[0][0].weight ** 2 + option[0][1].weight ** 2)
        for (new_machine, old_machine, task) in option:
            old_machine.remove_task(task)
            new_machine.add_task(task)
        val += (option[0][0].weight ** 2 + option[0][1].weight ** 2)
        return val < 0

    def reverse_option(self, option):
        for (new_machine, old_machine, task) in option:
            new_machine.remove_task(task)
            old_machine.add_task(task)

    def accept_change(self, option):
        msg = ("".join(f'\nmoved task: {task} : \nfrom machine {old_machine} \nto machine {new_machine}'
                       for (new_machine, old_machine, task) in option))
        self.log.debug(msg)
        self.machines = sorted(self.machines, reverse=True)
        return self.machines[0].weight - self.machines[-1].weight <= 1

    """
    iterators
    """

    def option_iterator(self, tasknum):
        if tasknum < 2:
            option_single_iterator = self.option_single_iter()
            for option in option_single_iterator:
                yield option
        else:
            tasknum_one = int(tasknum / 2)
            tasknum_two = tasknum - tasknum_one
            task_dif = tasknum_one - tasknum_two
            for i in range(self.m):
                first_machine = self.machines[i]
                for j in reversed(range(i + 1, self.m)):
                    second_machine = self.machines[j]
                    if (task_dif == 0 or (first_machine.is_legal_amount(self.n + task_dif)
                                          and second_machine.is_legal_amount(self.n - task_dif))):
                        com_iter = self.task_combination_iterator(first_machine, second_machine,
                                                                  tasknum_one, tasknum_two)
                        for task_com in com_iter:
                            yield task_com
                    if task_dif != 0 \
                            and first_machine.is_legal_amount(self.n - task_dif) \
                            and second_machine.is_legal_amount(self.n + task_dif):
                        sec_com_iter = self.task_combination_iterator(first_machine, second_machine,
                                                                      tasknum_two, tasknum_one)
                        for task_com in sec_com_iter:
                            yield task_com

    def option_single_iter(self):
        for i in range(self.m):
            machine = self.machines[i]
            weight = 0
            if machine.is_legal_amount(self.n + 1):
                for j in reversed(range(i + 1, self.m)):
                    second_machine = self.machines[j]
                    if second_machine.is_legal_amount(self.n - 1):
                        for task in machine.tasks:
                            prev_weight = weight
                            weight = task[1]
                            if weight != prev_weight:
                                yield [(second_machine, machine, task)]
                            if weight == machine.tasks[-1][1]:
                                break

    def task_combination_iterator(self, first_machine, second_machine, first_num, second_num):
        first_sum = 0
        for first_tasks in itertools.combinations(first_machine.tasks, first_num):
            prev_sum_1 = first_sum
            first_sum = sum([t[1] for t in first_tasks])
            if first_sum != prev_sum_1:
                second_sum = 0
                for second_tasks in itertools.combinations(reversed(second_machine.tasks), second_num):
                    prev_sum_2 = second_sum
                    second_sum = sum([t[1] for t in second_tasks])
                    if second_sum != prev_sum_2 and first_sum != second_sum:
                        yield [(first_machine, second_machine, task) for task in second_tasks] \
                              + [(second_machine, first_machine, task) for task in first_tasks]
