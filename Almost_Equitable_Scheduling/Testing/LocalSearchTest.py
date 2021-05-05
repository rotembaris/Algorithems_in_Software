import random
import unittest

from Almost_Equitable_Scheduling.Heuristics.LocalSearch import LocalSearch
from Almost_Equitable_Scheduling.IO_module import IOModule
from Almost_Equitable_Scheduling.Testing.LPTTest import LPTTest
import logging
import time

def random_input():
    arr = []
    m = random.randrange(7, 50)
    n = int(1000/m)
    nums = {}
    while len(arr) < n*m:
        num = random.random()
        num = int(1/num)
        if not num in nums:
            nums[num] = 1
            arr.append((len(arr) + 1, num))
        else:
            if nums[num] < m:
                arr.append((len(arr) +1, num))
                nums[num] += 1
    return arr, m, "{M}_{N}".format(M=m, N=n)

def lea_input_1():
    arr=[]
    for _ in range(30):
        arr.append((len(arr) +1, 3))
    for _ in range(10):
        arr.append((len(arr) +1, 2))
        arr.append((len(arr) +1, 4))
        arr.append((len(arr) +1, 6))
    return arr,6,"6_10"

def lea_input_2():
    arr = []
    for _ in range(6):
        arr.append((len(arr) +1,7))
        arr.append((len(arr) +1, 5))
        arr.append((len(arr) +1, 22))
    for _ in range(5):
        arr.append((len(arr) +1, 14))
    for _ in range(8):
        arr.append((len(arr) +1,10))
    for _ in range(3):
        arr.append((len(arr) +1,20))
    for _ in range(4):
        arr.append((len(arr) +1,4))
        arr.append((len(arr) +1, 1))
    m = int(len(arr)/6)
    return arr, 6, "7_7"

def lea_input_3():
    arr = [(i+1, i+11) for i in range(71)]
    return arr, 2, "2_35"

def lea_input_4():
    arr = []
    for _ in range(12):
        arr.append((len(arr) +1,7))
        arr.append((len(arr) +1, 5))
    for _ in range(11):
        arr.append((len(arr) +1, 1))
    return arr, 7, "7_5"

def lea_input_5():
    arr = []
    for _ in range(24):
        arr.append((len(arr) +1, 3))
        arr.append((len(arr) +1, 4))
    for _ in range(8):
        arr.append((len(arr) +1, 1))
    return arr, 14, "14_4"

def lea_input_6():
    arr = []
    for _ in range(12):
        arr.append((len(arr) +1, 3))
    for _ in range(3):
        arr.append((len(arr) +1, 4))
    for _ in range(6):
        arr.append((len(arr) +1, 8))
    return arr, 7, "7_3"

def lea_input_7():
    arr = []
    for _ in range(200):
        num = random.randrange(31,80,2)
        arr.append((len(arr) +1,num))
    return arr, 10, "10_20"

def lea_input_8():
    arr = []
    for _ in range(300):
        num = random.randrange(21,40,2)
        arr.append((len(arr) +1,num))
    return arr, 20, "20_15"

def lea_input_9():
    arr = []
    for _ in range(80):
        num = random.randrange(16,46)
        arr.append((len(arr) +1,num))
    return arr, 4, "4_20"

def lea_input_10():
    arr = []
    for _ in range(180):
        num = random.randrange(11,90)
        arr.append((len(arr) +1,num))
    return arr, 4, "4_45"




class LocalSearchTest(unittest.TestCase):

    def LocalSearch_solution(self, input):
        logger = logging.getLogger(input[2])
        tasks, machines = input[0], input[1]
        solution = LocalSearch(tasks, machines, 3)
        start_time = time.time()
        solution.local_search()
        end_time = time.time()
        logger.info(f"\ntime = {round((end_time - start_time), 2)} seconds\n")
        print("\nLocal Search {INPUT_NAME}"
              "\n{SOLUTION}"
              "\ngoal function: {MIN_WEIGHT}"
              "".format(
                INPUT_NAME=input[2], SOLUTION=str(solution),
                MIN_WEIGHT=str(min(solution.machines).weight),
                MIN_TASK=str(min(solution.machines, key=lambda m: m.task_num).task_num),
                MAX_TASK=str(max(solution.machines, key=lambda m: m.task_num).task_num)))
        return solution

    def test_LocalSearch(self):
        self.io = IOModule()
        for i in range(1):
            self.io.create_input_file(lea_input_1())
            self.io.create_input_file(lea_input_2())
            self.io.create_input_file(lea_input_3())
            self.io.create_input_file(lea_input_4())
            self.io.create_input_file(lea_input_5())
            self.io.create_input_file(lea_input_6())
            self.io.create_input_file(lea_input_7())
            self.io.create_input_file(lea_input_8())
            self.io.create_input_file(lea_input_9())
            self.io.create_input_file(lea_input_10())
            self.io.create_input_file(random_input())


        for file in self.io.file_arrays:
            i = self.io.load_input(file)
            self.logger = logging.getLogger(file)
            self.logger.info(f"tasks = {i[0]}")
            self.io.save_output(LPTTest.LPT_solution(i), file, "LPT "+i[2])
            self.io.save_output(self.LocalSearch_solution(i), file, "Local Search "+i[2])
        return True


if __name__ == '__main__':
    unittest.main()
