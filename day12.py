from collections import deque
from typing import List, Tuple

from utils import read_input

input_path = "./input/day12"

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def create_map(input_path: str) -> List[List[str]]:
    return [list(line) for line in read_input(input_path)]


def get_coordinates(map: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    for row_idx in range(len(map)):
        for col_idx in range(len(map[row_idx])):
            if map[row_idx][col_idx] == "S":
                start = (row_idx, col_idx)
            elif map[row_idx][col_idx] == "E":
                end = (row_idx, col_idx)
    return start, end


def get_starts(map: List[List[str]]) -> List[Tuple[int, int]]:
    starts = []
    for row_idx in range(len(map)):
        for col_idx in range(len(map[row_idx])):
            if map[row_idx][col_idx] in ("S", "a"):
                starts.append((row_idx, col_idx))
    return starts


def create_visited(map: List[List[str]]) -> List[List[int]]:
    return [[-1] * len(map[x]) for x in range(len(map))]


def is_valid_step(map: List[List[str]], current: Tuple[int, int], new: Tuple[int, int]) -> bool:
    max_rows = len(map)
    max_cols = len(map[0])
    is_in_map = 0 <= new[0] < max_rows and 0 <= new[1] < max_cols
    if not is_in_map:
        return False

    new_letter = map[new[0]][new[1]]
    current_letter = map[current[0]][current[1]]

    if new_letter == "E":
        new_letter = "z"
    if current_letter == "S":
        current_letter = "a"
    is_correct_diff = ord(new_letter) - ord(current_letter) <= 1
    return is_correct_diff


def is_less_steps(visited: List[List[int]], coords: Tuple[int, int], count: int) -> bool:
    return visited[coords[0]][coords[1]] == -1 or visited[coords[0]][coords[1]] > count


def traverse_map(map: List[List[str]], visited: List[List[int]], start: Tuple[int, int]):
    next_steps = deque([(start, 0)])
    next_coords = {start}
    visited[start[0]][start[1]] = 0
    while next_steps:
        current, current_count = next_steps.popleft()

        for move in MOVES:
            next_row, next_col = current[0] + move[0], current[1] + move[1]
            if is_valid_step(map, current, (next_row, next_col)) and \
                    is_less_steps(visited, (next_row, next_col), current_count + 1) \
                    and not (next_row, next_col) in next_coords:
                visited[next_row][next_col] = current_count + 1
                next_coords.add((next_row, next_col))
                next_steps.append(((next_row, next_col), current_count + 1))
    return


if __name__ == '__main__':
    map = create_map(input_path)
    start, target = get_coordinates(map)
    visited = create_visited(map)
    traverse_map(map, visited, start)
    for line in visited:
        print(line)
    print(visited[target[0]][target[1]])

    # part 2
    starts = get_starts(map)
    target_steps = []
    for start in starts:
        visited = create_visited(map)
        traverse_map(map, visited, start)
        if visited[target[0]][target[1]] != -1:
            target_steps.append(visited[target[0]][target[1]])
    print(min(target_steps))
