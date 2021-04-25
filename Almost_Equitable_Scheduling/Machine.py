import copy

class Machine:

    def __init__(self):
        self.Tasks = []
        self.TaskIndex = []
        self.weight = 0
        self.taskNum = 0

    def has_task(self, index: int) -> bool:
        return index in self.TaskIndex

    def get_task(self, index: int) -> tuple:
        for task in self.Tasks:
            if task[0] == index:
                return task
        return None

    def add_task(self, task: [tuple]):
        self.Tasks.append(task)
        self.TaskIndex.append(task[0])
        self.add_weight(task[1])
        self.taskNum += 1

    def remove_task(self, index: int):
        if self.has_task(index):
            task = self.get_task(index)
            self.Tasks.remove(task)
            self.remove_weight(task[1])
            self.TaskIndex.remove(task[0])
            self.taskNum -= 1
            return task
        else:
            return None

    def is_legal_amount(self, n: int) -> bool:
        return abs(len(self.Tasks) - n) <= 1

    def add_weight(self, weight: float):
        self.weight += weight

    def remove_weight(self, weight: float):
        self.weight -= weight

    def __str__(self):
        return ("weight = {WEIGHT}, task num = {TASK_NUM}. "
                "\ntasks = {TASKS}"
                .format(WEIGHT=str(self.weight), TASK_NUM=str(self.taskNum),TASKS=str(self.Tasks)))

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
        for task in self.Tasks:
            machine_copy.add_task(task)
        return machine_copy

