def uniquechars(str):
    mylist = [x for x in str]
    myset = set(mylist)
    return len(myset) == len(mylist)

if __name__ == '__main__':
    print(uniquechars('abcdefg'))
