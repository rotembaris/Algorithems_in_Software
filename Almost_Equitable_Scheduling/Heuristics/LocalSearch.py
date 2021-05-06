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

    """
    main function for returning the local-search solution
    """
    def local_search_solution(self):
        if self.start_search():
            return
        area_index = 1
        while area_index <= self.search_area:
            option_iter = self.option_iterator(area_index)
            for option in option_iter:
                if self.try_option(option):
                    if self.is_optimal():
                        return
                    area_index = 0
                    break
            area_index += 1
        return

    """
    initiates the machines to the LPT solution
    if the LPT solution is optimal, returns True to signal for local_search_solution to stop searching
    """
    def start_search(self):
        lpt = LPT(self.tasks, self.machineNum)
        lpt.LPT_solution()
        self.machines = sorted(lpt.machines, reverse=True)
        if self.is_optimal():
            self.log.info("LPT solution is optimal")
            return True
        else:
            return False

    """
    """
    def try_option(self, option):
        val = -((option[0][0].weight ** 2) + (option[0][1].weight ** 2))
        self.apply_option(option)
        val += (option[0][0].weight ** 2) + (option[0][1].weight ** 2)
        if val < 0:
            self.accept_change(option)
            return True
        else:
            self.reverse_option(option)
            return False

    def apply_option(self, option):
        for (new_machine, old_machine, tasks) in option:
            for task in tasks:
                old_machine.remove_task(task)
                new_machine.add_task(task)

    def reverse_option(self, option):
        for (new_machine, old_machine, tasks) in option:
            for task in tasks:
                new_machine.remove_task(task)
                old_machine.add_task(task)

    def accept_change(self, option):
        msg = ("".join(f'\nmoved tasks: {tasks} : \nfrom machine {old_machine} \nto machine {new_machine}'
                       for (new_machine, old_machine, tasks) in option))
        self.log.debug(msg)
        self.machines = sorted(self.machines, reverse=True)

    def is_optimal(self):
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
            multi_task_iter = self.multi_task_iter(tasknum)
            for option in multi_task_iter:
                yield option

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
                                yield [(second_machine, machine, [task])]
                            if weight == machine.tasks[-1][1]:
                                break

    def multi_task_iter(self, tasknum):
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

    def task_combination_iterator(self, first_machine, second_machine, first_num, second_num):
        first_sum = 0
        for first_tasks in itertools.combinations(first_machine.tasks, first_num):
            prev_first_sum = first_sum
            first_sum = sum([t[1] for t in first_tasks])
            if first_sum != prev_first_sum:
                second_sum = 0
                for second_tasks in itertools.combinations(reversed(second_machine.tasks), second_num):
                    prev_second_sum = second_sum
                    second_sum = sum([t[1] for t in second_tasks])
                    if second_sum != prev_second_sum and first_sum != second_sum:
                        yield [(first_machine, second_machine, second_tasks)] \
                              + [(second_machine, first_machine, first_tasks)]
