from typing import List, Tuple

from utils import read_input

input_path = "./input/day5"

AMOUNT_IDX = 1
FROM_IDX = 3
TO_IDX = 5


def get_initial_boxes(schema: List[str]) -> List[List[str]]:
    boxes = [[] for _ in range(9)]
    for line in schema:
        schema_idx = 0
        while line:
            box = line[:4].strip()
            line = line[4:]
            if box:
                boxes[schema_idx].append(box[1:2])
            schema_idx += 1

    return boxes


def parse_operation(line: str) -> Tuple[int, int, int]:
    parts = line.split(" ")
    amount = int(parts[AMOUNT_IDX])
    fro = int(parts[FROM_IDX]) - 1
    to = int(parts[TO_IDX]) - 1
    return amount, fro, to


def update_boxes(boxes: List[List[str]], amount: int, fro: int, to: int) -> List[List[str]]:
    assert len(boxes[fro]) >= amount
    for p in range(amount):
        lifted_box = boxes[fro].pop(0)
        boxes[to] = [lifted_box] + boxes[to]
    return boxes


def get_boxes_schema(input_path: str) -> List[List[str]]:
    lines = read_input(input_path)
    boxes = get_initial_boxes(lines[:8])
    for operation in lines[10:]:
        amount, fro, to = parse_operation(operation)
        boxes = update_boxes(boxes, amount, fro, to)
    return boxes


def get_top_boxes(boxes_schema: List[List[str]]) -> List[str]:
    return [pile[0] for pile in boxes_schema]


if __name__ == '__main__':
    boxes_schema = get_boxes_schema(input_path)
    top_boxes = get_top_boxes(boxes_schema)
    print("".join(top_boxes))
