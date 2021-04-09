def stringcompression(str):
    stringcompression = ""
    previousChar = ""
    counter = 1
    for x in range(len(str)):
        s = str[x]
        if x > 0 and s == previousChar:
            counter += 1
        elif previousChar:
            stringcompression += previousChar+f'{counter}'
            counter = 1
        previousChar = s
    stringcompression += previousChar + f'{counter}'
    return stringcompression

if __name__ == '__main__':
    print(stringcompression('AAABCCDDDDD'))
