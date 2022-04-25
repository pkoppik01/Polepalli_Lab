#checks if primer sequences are complementary

primer1 = input("Input your first primer sequence: ").upper()
primer2 = input("Input your second primer sequence: ").upper()

longest_comp_seq = 0
temp_comp_seq = 0
is_complementary = False
min_length = min(len(primer1), len(primer2))
for nums in range(min_length):
    if primer1[nums] == "C" and primer2[nums] == "G":
        is_complementary = True
    elif primer1[nums] == "G" and primer2[nums] == "C":
        is_complementary = True
    elif primer1[nums] == "A" and primer2[nums] == "T":
        is_complementary = True
    elif primer1[nums] == "T" and primer2[nums] == "A":
        is_complementary = True
    if is_complementary:
        temp_comp_seq += 1
        if temp_comp_seq > longest_comp_seq:
            longest_comp_seq = temp_comp_seq
    else:
        temp_comp_seq = 0
    is_complementary = False

print(longest_comp_seq)