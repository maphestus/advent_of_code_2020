
password_file = open("advent2020-02-input-ex.txt", "r")

tot_valid = 0

for password in password_file:
    li = password.split()
    pass_range = li[0].split("-")
    low_bound = int(pass_range[0])
    up_bound = int(pass_range[1])
    letter = li[1].strip(":")
    corrupt = li[2]
    tot_letter = 0
    for le in corrupt:
        if le == letter:
            tot_letter = tot_letter + 1
    if low_bound <= tot_letter <= up_bound:
        print(corrupt, "is valid!")
        tot_valid = tot_valid + 1

print("Total valid passwords:", tot_valid)
