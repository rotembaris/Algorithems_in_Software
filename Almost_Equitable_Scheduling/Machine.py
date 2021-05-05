import copy


class Machine:

    def __init__(self):
        self.tasks = []
        self.weight = 0
        self.task_num = 0

    def has_task(self, task) -> bool:
        return task in self.tasks

    def find_task(self, task):
        low = 0
        high = self.task_num
        mid = 0
        while low < high:
            mid = (high + low) // 2
            compare = self.tasks[mid]

            if compare == task:
                return mid

            if self.first_task_is_larger(compare, task):
                low = mid + 1

            else:
                high = mid
        return low

    def add_task(self, task: [tuple]):
        index = self.find_task(task)
        self.tasks = self.tasks[:index] + [task] + self.tasks[index:]
        self.add_weight(task[1])
        self.task_num += 1

    def remove_task(self, task):
        index = self.find_task(task)
        self.tasks = self.tasks[:index] + self.tasks[index+1:]
        self.remove_weight(task[1])
        self.task_num -= 1
        return task

    def is_legal_amount(self, n: int) -> bool:
        return abs(self.task_num - n) <= 1

    def add_weight(self, weight: float):
        self.weight += weight

    def remove_weight(self, weight: float):
        self.weight -= weight

    def __str__(self):
        return ("weight = {WEIGHT}, task num = {TASK_NUM}. "
                "\ntasks = {tasks}"
                .format(WEIGHT=str(self.weight), TASK_NUM=str(len(self.tasks)), tasks=str(self.tasks)))

    def value(self) -> float:
        return self.weight

    """
    create full order on the machines, based on their weight
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
        machine_copy = Machine()
        machine_copy.tasks = copy.copy(self.tasks)
        machine_copy.weight = self.weight
        machine_copy.task_num = self.task_num
        return machine_copy

    def first_task_is_larger(self,task_1,task_2):
        return task_1[1] > task_2[1] or (task_1[1] == task_2[1] and task_1[0] > task_2[0])
