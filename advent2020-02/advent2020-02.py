
password_file = open("advent2020-02-input.txt", "r")

tot_valid = 0
tot_pt2 = 0
# PART 1 START
for password in password_file:
    li = password.split()
    pass_range = li[0].split("-")
    low_bound = int(pass_range[0])
    low_pt2 = int(pass_range[0])-1
    up_bound = int(pass_range[1])
    up_pt2 = int(pass_range[1])-1
    letter = li[1].strip(":")
    corrupt = li[2]
    tot_letter = 0
    for le in corrupt:
        if le == letter:
            tot_letter = tot_letter + 1
    if low_bound <= tot_letter <= up_bound:
        print(corrupt, "is valid for part 1!")
        tot_valid = tot_valid + 1
    # PART 2 START
    if (corrupt[low_pt2] == letter and corrupt[up_pt2] != letter) or (corrupt[up_pt2] == letter and corrupt[low_pt2] != letter):
        print(corrupt, "is valid for part 2!")
        tot_pt2 = tot_pt2 + 1
    # PART 2 END

print("Total valid passwords for part 1:", tot_valid)
print("Total valid passwords for part 2:", tot_pt2)

password_file.close()

# PART 1 END
