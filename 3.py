from string import ascii_letters


with open("input_3.txt", "r") as fin:
    rows = fin.readlines()


sum_ = 0
mapping = {el: idx for idx, el in enumerate(ascii_letters, 1)}
rows[-1] = rows[-1] + "\n"

prev_set = None

sum_ = 0
sum_2nd_task = 0
sets_ = []
cnt = 0
for i, row in enumerate(rows):
    row = row[:-1]
    idx = len(row) // 2
    l, r = row[:idx], row[idx:]
    cur_set = set(l).intersection(set(r))
    sum_ += mapping[cur_set.pop()]

    sets_ += [set(row)]
    # 2nd part
    if len(sets_) == 3:
        a, b, c = sets_
        sum_2nd_task += mapping[a.intersection(b).intersection(c).pop()]
        sets_ = []
        continue

print(sum_)
print(sum_2nd_task)
