from utils import read_input

input_path = "./input/day1"


def get_top_calories(input: str, top_limit: int = 3):
    lines = read_input(input)
    calories = []
    current_elf_calories = 0
    for line in lines:
        if line == "\n":
            calories.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)
    calories = sorted(calories, reverse=True)[:top_limit]
    return calories


if __name__ == '__main__':
    top_calories = get_top_calories(input_path)
    print(sum(top_calories))
