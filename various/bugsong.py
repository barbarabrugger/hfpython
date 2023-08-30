word = "bugs"

for bugs_num in range(99, 0, -1):
    print(bugs_num, word, "of bugs in the code.")
    print(bugs_num, word, "of bugs.")
    print("Take one down.")
    print("Fix it around.")
    
    if bugs_num == 1:
        print("No more bugs in the code.")
    else:
        new_num = bugs_num -1
        if new_num == 1:
            word = "bug"
        print(new_num, word, "of bugs in the code.")
    print()