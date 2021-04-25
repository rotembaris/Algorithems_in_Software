from Almost_Equitable_Scheduling.Machine import Machine


class Task:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.machine = None

    def set_machine(self, machine: Machine):
        prev_mach = self.machine
        self.machine = machine
        return prev_mach
