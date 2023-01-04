from typing import List, Tuple, Optional, Set

from utils import read_input

input_path = "./input/day9"

def parse_line(line: str) -> List[str]:
    op, count = line.split(" ")
    count_parsed = int(count)
    return [op] * count_parsed


def update_head_position(head_position: Tuple[int, int], op: str) -> Tuple[int, int]:
    x, y = head_position
    if op == "D":
        return x, y - 1
    elif op == "U":
        return x, y + 1
    elif op == "L":
        return x - 1, y
    elif op == "R":
        return x + 1, y


def update_tail_position(tail_position: Tuple[int, int], head_position: Tuple[int, int]) -> Tuple[int, int]:
    tail_x, tail_y = tail_position
    head_x, head_y = head_position
    delta_x, delta_y = head_x - tail_x, head_y - tail_y
    if abs(delta_x) <= 1 and abs(delta_y) <= 1:
        return tail_position

    # vertical move
    if abs(delta_x) < abs(delta_y):
        tail_x, tail_y = head_x, head_y - delta_y // abs(delta_y)
    # horizontal move
    elif abs(delta_x) > abs(delta_y):
        tail_x, tail_y = head_x - delta_x // abs(delta_x), head_y
    # diagonal move
    else:
        tail_x, tail_y = head_x - delta_x // abs(delta_x), head_y - delta_y // abs(
            delta_y
        )
    return tail_x, tail_y


def get_visited_places(input_path: str) -> Set[Tuple[int, int]]:
    lines: List[str] = read_input(input_path)
    tail_places = {(0, 0)}
    head_position = (0, 0)
    tail_position = (0, 0)
    for line in lines:
        operations = parse_line(line)
        for op in operations:
            head_position = update_head_position(head_position, op)
            tail_position = update_tail_position(tail_position, head_position)
            tail_places.add(tail_position)
    return tail_places


if __name__ == '__main__':
    visited = get_visited_places(input_path)
    print(len(visited))
