def get_cals(fin):
    with open(fin, "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]

    # gather the numbers by elves
    # an array of arrays. each array is one elf's calories
    # then we'll take the sum
    sums = []
    cur_sum = 0
    prev = ""
    seen_blank = False
    for cal in lines:
        if cal != "":
            seen_blank = False
            cur_sum += int(cal)
        # multiple blanks -- an elf with nothing
        elif cal == "" and prev == "" and not seen_blank:
            cur_sum = 0
            sums.append(cur_sum)
            seen_blank = True
        elif cal == "" and prev == "" and seen_blank:
            continue
        else:
            sums.append(cur_sum)
            cur_sum = 0
        prev = cal
    # add the last elf because it ends without an empty line
    sums.append(cur_sum)
    print(sums)

    return sums


def sum_top_3(sums):
    sorted_list = sorted(sums, reverse=True)
    return sum(sorted_list[:3])


def main(input):
    print("Getting the most cals: ")
    cals = get_cals(input)
    top_cal = max(cals)
    print(top_cal)

    print("Getting top 3 cals: ")
    print(sum_top_3(cals))

    return top_cal


r = main("example_input.txt")
print(r)
assert r == 24000

r = main("example2.txt")
print(r)
assert r == 12021092

r = main("example3.txt")
print(r)
assert r == 100000


# Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.
r = main("example4.txt")
print(r)
assert r == 6000

# test
print("For the test problem, the answer is:")
print(main("input.txt"))
