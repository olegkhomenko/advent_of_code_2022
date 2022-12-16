top_3 = []
with open("input_1.txt", "r") as fin:
    sum_ = 0
    max_sum = 0
    min_max = 0
    while row := fin.readline():
        if row == "\n":
            if sum_ > min_max or len(top_3) < 3:
                top_3.append(sum_)
                top_3 = sorted(top_3, reverse=True)
                top_3 = top_3[:3]
                min_max = min(top_3)
            sum_ = 0
            continue

        sum_ += int(row.replace("\n", ""))

print("Top 3:\t", top_3)
print("Sum Top:\t", sum(top_3))
