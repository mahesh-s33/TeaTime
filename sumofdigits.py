def sumofdigits(n):
    if n>9:
        return n%10 + sumofdigits(n//10)
    else:
        return n
    pass

if __name__ == '__main__':
    print(sumofdigits(123))