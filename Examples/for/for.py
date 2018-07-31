vowels = 0
consonants = 0

for alp in "abcdefghijklmnopqrsuvwxyz":
    if alp.lower() in "aeiou":
        vowels = vowels + 1
    elif alp == "":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
