TEST = False


def process_row(row: str, offset=4):
    i = 0
    while i < len(row) - offset:
        if len(set(row[i : i + offset])) == offset:
            return i + offset

        i += 1


with open("input_6{}.txt".format("_test" if TEST else ""), "r") as fin:
    rows = fin.readlines()


for row in rows:
    print(process_row(row, offset=4))
    print(process_row(row, offset=14))
    print("-" * 10)
