from copy import deepcopy
N_STACKS = 9

stacks = [[] for _ in range(N_STACKS)]

with open("input_5.txt", "r") as fin:
    stacks_flag = 0
    for row in fin:
        if stacks_flag < 1:
            if row[1] == "1":
                stacks_flag = 1
                continue

            for i in range(N_STACKS):
                el = row[i*4 + 1:i*4 + 2]
                if el != " ":
                    stacks[i].append(el)

        elif stacks_flag == 1:  # skip empty line
            stacks = [s[::-1] for s in stacks]
            stacks_2 = deepcopy(stacks)
            stacks_flag += 1
            continue

        else:
            rs = row.split(" ")
            cnt, fr, to  = int(rs[1]), int(rs[3]) - 1, int(rs[5].replace("\n", "")) - 1
            print(cnt, fr, to)

            bot, top = stacks[fr][:-cnt], stacks[fr][-cnt:]
            stacks[fr] = bot
            stacks[to] += top[::-1]

            bot_2, top_2 = stacks_2[fr][:-cnt], stacks_2[fr][-cnt:]
            stacks_2[fr] = bot_2
            stacks_2[to] += top_2


print("".join([s[-1] for s in stacks]))
print("".join([s[-1] for s in stacks_2]))
    


