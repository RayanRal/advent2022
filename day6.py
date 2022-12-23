from typing import List, Tuple, Optional

from utils import read_input

input_path = "./input/day6"

# WINDOW_SIZE = 4  # pt 1
WINDOW_SIZE = 14  # pt 2


def is_unique(window: List[str]) -> bool:
    return len(set(window)) == len(window)


def get_end_position(input_path: str) -> Optional[int]:
    input_stream = list(read_input(input_path)[0])
    window = []
    end_idx = 0
    while end_idx < WINDOW_SIZE:
        window.append(input_stream[end_idx])
        end_idx += 1

    assert len(window) == WINDOW_SIZE
    while end_idx < len(input_stream):
        if is_unique(window):
            return end_idx

        window.pop(0)
        end_idx += 1
        window.append(input_stream[end_idx])
    return None


if __name__ == '__main__':
    end_position = get_end_position(input_path)
    print(end_position + 1)
