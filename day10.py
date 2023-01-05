from collections import OrderedDict
from typing import List, Dict

from utils import read_input

input_path = "./input/day10"


# need to record strength DURING cycle
def process_line(line: str, cycle_signal: OrderedDict[int, int]):
    last_cycle = next(reversed(cycle_signal))
    last_signal = cycle_signal[last_cycle]
    if line == "noop":
        cycle_signal[last_cycle + 1] = last_signal
    else:
        op, amount = line.split(" ")
        cycle_signal[last_cycle + 1] = last_signal
        cycle_signal[last_cycle + 2] = last_signal + int(amount)


def get_signal_registers(input_path: str) -> Dict[int, int]:
    lines: List[str] = read_input(input_path)
    cycle_signal = OrderedDict()
    cycle_signal[1] = 1
    for line in lines:
        process_line(line, cycle_signal)
    return cycle_signal


def is_sprite_on_screen(cycle: int, signal: int) -> bool:
    return (cycle - 1) % 40 in [signal - 1, signal, signal + 1]


if __name__ == '__main__':
    cycles = [20, 60, 100, 140, 180, 220]
    cycle_registers = get_signal_registers(input_path)
    signal_strengths = [cycle_registers[cycle] * cycle for cycle in cycles]
    print(sum(signal_strengths))

    for cycle, signal in cycle_registers.items():
        symbol = "#" if is_sprite_on_screen(cycle, signal) else "."
        print(symbol, end="")
        if cycle % 40 == 0:
            print()
