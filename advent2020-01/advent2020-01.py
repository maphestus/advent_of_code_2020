
expense = open("advent2020-01-input.txt", "r")

expense_list = []

for line in expense:
    strip_line = line.strip()
    # print(strip_line)
    expense_list.append(int(strip_line))

# PART 1 START
for i in expense_list:
    for a in expense_list:
        if a != i:
            if a + i == 2020:
                print(a, "+", i, "= 2020!!!")
                calculated = a * i
                print(a, "*", i, "=", calculated)
# PART 1 END

# PART 2 START
        for b in expense_list:
            if a != b != i:
                if a + b + i == 2020:
                    print(a, "+", b, "+", i, "= 2020!")
                    triple_calc = a * b * i
                    print(a, "*", b, "*", i, "=", triple_calc)
# PART 2 END
