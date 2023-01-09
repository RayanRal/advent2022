import math
from collections import Counter
from typing import List, Dict

from utils import read_input

input_path = "./input/day11"

NUM_ROUNDS = 20


class Monkey:
    def __init__(self, id, items, operation, divisible, target_true, target_false):
        self.id = id
        self.items = items
        self.operation = operation
        self.divisible_test = divisible
        self.target_true = target_true
        self.target_false = target_false


def parse_operation(line: str):
    op = line.split("=")[1].strip().split(" ")
    if "+" in op:
        if op[-1].isnumeric():
            constant = int(op[-1])
            return lambda x: x + constant
        if op[-1].isalpha():
            return lambda x: x + x
    if "*" in op:
        if op[-1].isnumeric():
            constant = int(op[-1])
            return lambda x: x * constant
        if op[-1].isalpha():
            return lambda x: x * x


def parse_monkey(lines: List[str], start_idx: int) -> Monkey:
    monkey_id = int(lines[start_idx].split(" ")[1][:-1])
    start_items = lines[start_idx + 1].split(" ")[2:]
    items = [int(i.strip(" ,")) for i in start_items]
    operation = parse_operation(lines[start_idx + 2])
    divisible = int(lines[start_idx + 3].split(" ")[3])
    target_true = int(lines[start_idx + 4].split(" ")[5])
    target_false = int(lines[start_idx + 5].split(" ")[5])
    return Monkey(id=monkey_id,
                  items=items,
                  operation=operation,
                  divisible=divisible,
                  target_true=target_true,
                  target_false=target_false)


def run_round(monkeys: Dict[int, Monkey], inspection_counts: Counter):
    for monkey_id, monkey in monkeys.items():
        print(f"Monkey {monkey_id}")
        while monkey.items:
            item = monkey.items.pop(0)
            inspection_counts[monkey_id] += 1
            print(f"    Monkey inspects item with worry level {item}")
            worry_level = monkey.operation(item)
            print(f"    Worry level becomes {worry_level}")
            worry_level /= 3
            worry_level = math.floor(worry_level)
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}")
            check_target = worry_level % monkey.divisible_test == 0
            if check_target:
                print(f"    Current worry level is divisible by {monkey.divisible_test}. Item with worry level {worry_level} is thrown to monkey {monkey.target_true}")
                monkeys[monkey.target_true].items.append(worry_level)
            else:
                print(f"    Current worry level is NOT divisible by {monkey.divisible_test}. Item with worry level {worry_level} is thrown to monkey {monkey.target_false}")
                monkeys[monkey.target_false].items.append(worry_level)



def create_monkeys(input_path: str) -> Dict[int, Monkey]:
    lines: List[str] = read_input(input_path)
    monkeys = {}
    for idx in range(0, len(lines) - 1, 7):
        monkey = parse_monkey(lines, idx)
        monkeys[monkey.id] = monkey
    return monkeys


if __name__ == '__main__':
    monkeys = create_monkeys(input_path)
    inspection_counts = Counter({k: 0 for k in monkeys.keys()})

    for r in range(NUM_ROUNDS):
        run_round(monkeys, inspection_counts)
        print(f"DEBUG: After round {r}, monkeys are holding: ")
        for monkey_id, monkey in monkeys.items():
            print(f"Monkey {monkey_id}: {monkey.items}")
    top_inspections = sorted(inspection_counts.values(), key=lambda x: -x)[:2]
    print(f"Top amount of was {top_inspections}")
    print(f"Result is {top_inspections[0] * top_inspections[1]}")