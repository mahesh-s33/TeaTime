def largestSum(arr):
    largestSum = 0
    sum = 0
    for x in arr:
        sum += x
        if sum > largestSum:
            largestSum = sum
    return largestSum

if __name__ == '__main__':
    print(largestSum([-1,1]))
