def read_input(path):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
        return lines
