import functools
import json
from enum import Enum
from typing import List, Tuple

from utils import read_input

input_path = "./input/day13"


class CheckResult(Enum):
    CORRECT = 1
    WRONG = 2
    CONTINUE = 3


def read_line_pairs(input_path):
    inp = read_input(input_path)
    pairs = []
    while len(inp) >= 2:
        l1, l2 = inp.pop(0), inp.pop(0)
        if inp:
            inp.pop(0)
        pairs.append((l1, l2))
    return pairs


def create_list(line: str):
    return json.loads(line)


def isList(l):
    return isinstance(l, list)


def is_correct_order(l1, l2) -> CheckResult:
    idx1, idx2 = 0, 0
    while idx1 < len(l1) and idx2 < len(l2):
        if isList(l1[idx1]) and isList(l2[idx2]):
            check_result = is_correct_order(l1[idx1], l2[idx2])
            if check_result != CheckResult.CONTINUE:
                return check_result
            else:
                idx1 += 1
                idx2 += 1
                continue

        if isList(l1[idx1]) or isList(l2[idx2]):
            if isList(l1[idx1]):
                l2[idx2] = [l2[idx2]]
                continue
            elif isList(l2[idx2]):
                l1[idx1] = [l1[idx1]]
                continue

        if l1[idx1] < l2[idx2]:
            return CheckResult.CORRECT
        if l1[idx1] > l2[idx2]:
            return CheckResult.WRONG
        idx1 += 1
        idx2 += 1

    if idx1 == len(l1) and idx2 == len(l2):
        return CheckResult.CONTINUE
    if idx1 == len(l1):
        return CheckResult.CORRECT
    else:
        return CheckResult.WRONG


if __name__ == '__main__':
    list_pairs: List[Tuple[str, str]] = read_line_pairs(input_path)
    ordered_pairs = []
    for idx, pair in enumerate(list_pairs, start=1):
        l1 = create_list(pair[0])
        l2 = create_list(pair[1])
        order = is_correct_order(l1, l2)
        if order == CheckResult.CORRECT:
            ordered_pairs.append(idx)
    print(sum(ordered_pairs))

    # part 2
    all_lines = [create_list(x) for p in list_pairs for x in [p[0], p[1]]]
    all_lines += [[[2]], [[6]]]

    sort_key = functools.cmp_to_key(lambda x, y: 1 if is_correct_order(x[:], y[:]) == CheckResult.WRONG else -1)
    sorted_lines = sorted(all_lines, key=sort_key)

    i1 = sorted_lines.index([[[[2]]]]) + 1
    i2 = sorted_lines.index([[[[6]]]]) + 1
    print(i1 * i2)
