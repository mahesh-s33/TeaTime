def anagram(str1, str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ", "").lower()
    anagram = True
    counter1 = {}
    counter2 = {}
    for x in str1:
        if x not in counter1:
            counter1[x] = 1
        else:
            counter1[x] += 1
    for x in str2:
        if x not in counter2:
            counter2[x] = 1
        else:
            counter2[x] += 1
    if counter1 != counter2:
        anagram = False
    return anagram

if __name__ == '__main__':
    print(anagram('123','1 2'))
