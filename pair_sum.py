def pair_sum(arr, n):
    pair_sum = 0
    pairs = set()
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x]+arr[y] == n and (arr[x],arr[y]) not in pairs and (arr[y],arr[x]) not in pairs:
                pair_sum += 1
                pairs.add((arr[x],arr[y]))
    return pair_sum

if __name__ == '__main__':
    print(pair_sum([1,3,2,2],4))
