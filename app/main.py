import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    file1, file2 = parts[1], parts[2]
    if file1 == file2 or not os.path.exists(file1):
        return

    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        for line in file_in:
            file_out.write(line)
