from typing import List, Tuple

from utils import read_input

input_path = "./input/day4"


def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    t1, t2 = line.strip().split(",")
    start1, end1 = [int(x) for x in t1.split("-")]
    start2, end2 = [int(x) for x in t2.split("-")]
    return (start1, end1), (start2, end2)


def is_contained(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> bool:
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > start2:
        return is_contained(interval2, interval1)
    return end1 >= end2 or start1 == start2


def is_overlaps(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> bool:
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > start2:
        return is_overlaps(interval2, interval1)
    return end1 >= start2


def get_overlaps(input: str) -> Tuple[int, int]:
    lines = read_input(input)
    overlaps, contained = 0, 0
    for line in lines:
        p1, p2 = parse_line(line)
        if is_contained(p1, p2):
            contained += 1
        if is_overlaps(p1, p2):
            overlaps += 1
    return contained, overlaps


if __name__ == '__main__':
    num_contains, num_overlaps = get_overlaps(input_path)
    print(num_contains)
    print(num_overlaps)
