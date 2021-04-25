from json import dump, load
from Almost_Equitable_Scheduling.Solution import Solution
from Almost_Equitable_Scheduling.Machine import Machine
from Almost_Equitable_Scheduling.Private import path
import os


class IOModule:
    input_file = path + "/Almost_Equitable_Scheduling/IO/Input_{INPUT_NAME}.json"
    output_file = path + "/Almost_Equitable_Scheduling/IO/Output_{OUTPUT_NAME}.txt"

    def __init__(self):
        self.file_arrays = []

    def create_input_file(self, inputs: [tuple]):
        i = self.input_file.format(INPUT_NAME=inputs[2])
        with open(i, "a") as f:
            dump(inputs, f)
        f.close()
        self.file_arrays.append(inputs[2])

    @staticmethod
    def load_input(file: str) -> [tuple]:
        n = IOModule.input_file.format(INPUT_NAME=file)
        with open(n, "r") as i:
            arr = load(i)
        i.close()
        return arr

    @staticmethod
    def save_output(solution: [Machine], file: str, solname: str):
        sol_str = "\n" + solname + "\n{SOLUTION}\ngoal function: {MIN_WEIGHT}\n"\
            .format(SOLUTION=str(solution), MIN_WEIGHT=str(min(solution.machines).weight))
        f = IOModule.output_file.format(OUTPUT_NAME = file)
        with open(f, "a+") as i:
            i.write(sol_str)
        i.close()
