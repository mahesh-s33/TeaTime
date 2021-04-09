#!/bin/python3

import math
import os
import random
import re
import sys

"""
https://www.hackerrank.com/challenges/30-2d-arrays/problem

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""

if __name__ == '__main__':
    arr = []
    hourglasses = []


    def hourglass(row, column):
        sumhg = arr[row][column] + arr[row][column + 1] + arr[row][column + 2] + arr[row + 1][column + 1] + \
                arr[row + 2][column] + arr[row + 2][column + 1] + arr[row + 2][column + 2]
        return sumhg


    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for row in range(len(arr)):
        if row < len(arr) - 2:
            for column in range(len(arr[row])):
                if column < len(arr[row]) - 2:
                    hourglasses.append(hourglass(row, column))

    print(max(hourglasses))
