import csv

with open("input_4.txt", "r") as fin:
    reader = csv.reader(fin, delimiter=",")

    sum_ = 0
    sum_2nd_part = 0
    for row in reader:
        left = [int(i) for i in row[0].split("-")]
        right = [int(i) for i in row[1].split("-")]

        if left[0] > right[0]:
            if left[1] < right[1]:
                sum_ += 1

        elif left[0] < right[0]:
            if left[1] > right[1]:
                sum_ += 1

        if left[0] == right[0] or left[1] == right[1]:
            sum_ += 1

        # 2nd part
        if left[0] < right[0]:
            if left[1] >= right[0]:
                sum_2nd_part += 1
        if left[0] > right[0]:
            if left[0] <= right[1]:
                sum_2nd_part += 1

        if left[0] == right[0]:
            sum_2nd_part += 1

print(sum_)
print(sum_2nd_part)
