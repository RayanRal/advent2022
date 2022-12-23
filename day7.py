from dataclasses import dataclass
from typing import List, Optional, Dict

from utils import read_input

input_path = "./input/day7"

DIRECTORIES = []
TRESHOLD = 100000

@dataclass
class FileInfo:
    name: str
    size: int


@dataclass
class Directory:
    files: List[FileInfo]
    directories: Dict[str, "Directory"]
    parent_directory: Optional["Directory"]

    def get_total_size(self):
        dirs_sizes = [d.get_total_size() for d in self.directories.values()]
        dirs_size = sum(dirs_sizes)
        files_size = sum([f.size for f in self.files])
        return dirs_size + files_size


def is_cd_command(line):
    return line.startswith("$ cd")


def process_cd(command: str, current_dir: Directory) -> Directory:
    if command == "$ cd ..":
        return current_dir.parent_directory
    else:
        target_directory = command.split(" ")[2]
        return current_dir.directories[target_directory]


def add_info(lines: List[str], cur_line_idx: int, dir: Directory) -> int:
    cur_line_idx += 1  # skip ls part
    while cur_line_idx < len(lines) and not (line := lines[cur_line_idx].strip()).startswith("$"):
        if line.startswith("dir"):
            new_directory_name = line.split(" ")[1]
            new_directory = Directory(files=[], directories={}, parent_directory=dir)
            DIRECTORIES.append(new_directory)
            dir.directories[new_directory_name] = new_directory
        else:
            file_size, filename = line.split(" ")
            dir.files.append(FileInfo(filename, int(file_size)))
        cur_line_idx += 1
    return cur_line_idx


def scan_all_directories(input_path: str) -> Optional[int]:
    lines = read_input(input_path)
    root_dir = Directory(files=[], directories={}, parent_directory=None)
    DIRECTORIES.append(root_dir)
    current_dir = root_dir
    line_idx = 1  # skip going to root
    while line_idx < len(lines):
        if is_cd_command(lines[line_idx]):
            current_dir = process_cd(lines[line_idx], current_dir)
            line_idx += 1
        else:
            line_idx = add_info(lines, line_idx, current_dir)

    return line_idx


if __name__ == '__main__':
    end_position = scan_all_directories(input_path)
    sizes_under_treshold = [dir_size for directory in DIRECTORIES if (dir_size := directory.get_total_size()) < TRESHOLD]
    print(sum(sizes_under_treshold))
