from typing import List, Tuple

from utils import read_input

input_path = "./input/day3"


# first half of the characters represent items in the first compartment,
# the second half of the characters represent items in the second compartment.

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def get_item_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def get_duplicate(comp1: List[str], comp2: List[str]) -> str:
    duplicate_items = set(comp1).intersection(set(comp2))
    return list(duplicate_items)[0]


def get_compartments(rucksack: str) -> Tuple[List[str], List[str]]:
    center_idx = len(rucksack) // 2
    comp1, comp2 = rucksack[:center_idx], rucksack[center_idx:]
    comp1, comp2 = list(comp1.strip()), list(comp2.strip())
    assert len(comp1) == len(comp2)
    return comp1, comp2


def get_duplicate_items_priorities(input: str) -> int:
    lines = read_input(input)
    duplicates = []
    for rucksack in lines:
        comp1, comp2 = get_compartments(rucksack)
        duplicate = get_duplicate(comp1, comp2)
        duplicates.append(duplicate)
    items_priorities = [get_item_priority(item) for item in duplicates]
    return sum(items_priorities)


def get_badge_priorities(input: str) -> int:
    lines = read_input(input)
    badges = []
    while lines:
        l1 = set(lines.pop(0).strip())
        l2 = set(lines.pop(0).strip())
        l3 = set(lines.pop(0).strip())
        badge_set = l1.intersection(l2).intersection(l3)
        badge = list(badge_set)[0]
        badges.append(badge)
    badge_priorities = [get_item_priority(item) for item in badges]
    return sum(badge_priorities)


if __name__ == '__main__':
    duplicate_priorities = get_duplicate_items_priorities(input_path)
    print(duplicate_priorities)
    badge_priorities = get_badge_priorities(input_path)
    print(badge_priorities)
