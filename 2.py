import csv
from itertools import permutations


# 1st question

# A — Rock
# B — Paper
# C — Scissors
scores = dict(
    A=dict(A=(3 + 1), B=(6 + 2), C=(0 + 3)),
    B=dict(A=(0 + 1), B=(3 + 2), C=(6 + 3)),
    C=dict(A=(6 + 1), B=(0 + 2), C=(3 + 3)),
)

scores_follow_up = dict(
    A=dict(Z=(6 + 2), Y=(3 + 1), X=(0 + 3)),
    B=dict(Z=(6 + 3), Y=(3 + 2), X=(0 + 1)),
    C=dict(Z=(6 + 1), Y=(3 + 3), X=(0 + 2)),
)

strategies = list(permutations(["A", "B", "C"]))
with open("input_2.txt", "r") as fin:
    reader = csv.reader(fin)
    rows = []

    for line in reader:
        rows += line

results = []
for strategy in strategies:
    sum_ = 0
    mapping = {k: v for k, v in zip(["X", "Y", "Z"], strategy)}
    for row in rows:
        a, b = row.split(" ")
        b = mapping[b]
        sum_ += scores[a][b]

    results += [sum_]

print("Results:\t", results)
print(f"Max sum:\t{max(results)}")

results = []
sum_ = 0
for row in rows:
    a, b = row.split(" ")
    sum_ += scores_follow_up[a][b]

print("Result:\t\t", sum_)


# follow-up question
