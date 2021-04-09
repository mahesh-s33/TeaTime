def missingelement(arr1, arr2):
    for x in arr2:
        arr1.remove(x)
    return arr1[0]

if __name__ == '__main__':
    print(missingelement([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))
