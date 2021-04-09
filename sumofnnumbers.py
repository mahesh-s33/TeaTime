def sumofnnumbers(n):
    if n>0:
        n += sumofnnumbers(n-1)
    return n

if __name__ == '__main__':
    print(sumofnnumbers(5))
