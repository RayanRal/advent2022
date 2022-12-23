from dataclasses import dataclass
from typing import List, Optional, Dict

from utils import read_input

input_path = "./input/day8"


def is_visible_from_left(row: int, col: int, forest: List[List[int]]) -> bool:
    idx = 0
    target = forest[row][col]
    while idx < col:
        if target <= forest[row][idx]:
            return False
        idx += 1
    return True


def is_visible_from_right(row: int, col: int, forest: List[List[int]]) -> bool:
    idx = len(forest) - 1
    target = forest[row][col]
    while idx > col:
        if target <= forest[row][idx]:
            return False
        idx -= 1
    return True


def is_visible_from_bottom(row: int, col: int, forest: List[List[int]]) -> bool:
    idx = len(forest) - 1
    target = forest[row][col]
    while idx > row:
        if target <= forest[idx][col]:
            return False
        idx -= 1
    return True


def is_visible_from_top(row: int, col: int, forest: List[List[int]]) -> bool:
    idx = 0
    target = forest[row][col]
    while idx < row:
        if target <= forest[idx][col]:
            return False
        idx += 1
    return True


def is_visible(row: int, col: int, forest: List[List[int]]) -> bool:
    if row == 0 or col == 0:
        return True

    if row == len(forest) - 1 or col == len(forest) - 1:
        return True

    is_from_left = is_visible_from_left(row, col, forest)
    is_from_right = is_visible_from_right(row, col, forest)
    is_from_top = is_visible_from_top(row, col, forest)
    is_from_bottom = is_visible_from_bottom(row, col, forest)
    return is_from_left or is_from_right or is_from_top or is_from_bottom


def get_visible_count(input_path: str) -> int:
    lines: List[str] = read_input(input_path)
    forest_str: List[List[str]] = [list(l) for l in lines]
    forest: List[List[int]] = [[int(c) for c in r] for r in forest_str]
    visible_count = 0
    for row_idx, row in enumerate(forest):
        for column in range(len(row)):
            if is_visible(row_idx, column, forest):
                visible_count += 1
    return visible_count


if __name__ == '__main__':
    visible_count = get_visible_count(input_path)
    print(f"Visible trees: {visible_count}")
