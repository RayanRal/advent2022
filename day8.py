from dataclasses import dataclass
from typing import List, Optional, Dict

from utils import read_input

input_path = "./input/day8"


# ==== PART 1 ====

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
        for col_idx in range(len(row)):
            if is_visible(row_idx, col_idx, forest):
                visible_count += 1
    return visible_count


# ==== PART 2 ====

def get_left_count(row: int, col: int, forest: List[List[int]]) -> int:
    current_tree = forest[row][col]
    cur_idx = col - 1
    lower_trees = 0
    while cur_idx >= 0:
        lower_trees += 1
        if current_tree <= forest[row][cur_idx]:
            break
        cur_idx -= 1
    return lower_trees


def get_right_count(row: int, col: int, forest: List[List[int]]) -> int:
    current_tree = forest[row][col]
    cur_idx = col + 1
    lower_trees = 0
    while cur_idx < len(forest):
        lower_trees += 1
        if current_tree <= forest[row][cur_idx]:
            break
        cur_idx += 1
    return lower_trees


def get_top_count(row: int, col: int, forest: List[List[int]]) -> int:
    current_tree = forest[row][col]
    cur_idx = row - 1
    lower_trees = 0
    while cur_idx >= 0:
        lower_trees += 1
        if current_tree <= forest[cur_idx][col]:
            break
        cur_idx -= 1
    return lower_trees


def get_bottom_count(row: int, col: int, forest: List[List[int]]) -> int:
    current_tree = forest[row][col]
    cur_idx = row + 1
    lower_trees = 0
    while cur_idx < len(forest):
        lower_trees += 1
        if current_tree <= forest[cur_idx][col]:
            break
        cur_idx += 1
    return lower_trees


def get_scenic_score(row: int, col: int, forest: List[List[int]]):
    if row == 0 or col == 0:
        return 0
    if row == len(forest) - 1 or col == len(forest) - 1:
        return 0

    left_count = get_left_count(row, col, forest)
    right_count = get_right_count(row, col, forest)
    top_count = get_top_count(row, col, forest)
    bottom_count = get_bottom_count(row, col, forest)
    return left_count * right_count * top_count * bottom_count


def get_scenic_scores(input_path: str) -> List[List[Optional[int]]]:
    lines: List[str] = read_input(input_path)
    forest_str: List[List[str]] = [list(l) for l in lines]
    forest: List[List[int]] = [[int(c) for c in r] for r in forest_str]
    scores = [[None for _ in r] for r in forest_str]
    for row_idx, row in enumerate(forest):
        for col_idx in range(len(row)):
            score = get_scenic_score(row_idx, col_idx, forest)
            scores[row_idx][col_idx] = score
    return scores


#  ==== MAIN ====

if __name__ == '__main__':
    visible_count = get_visible_count(input_path)
    print(f"Visible trees: {visible_count}")

    scenic_scores = get_scenic_scores(input_path)
    top_scenic_score = max([score for row in scenic_scores for score in row])
    print(f"Highest scenic score: {top_scenic_score}")
