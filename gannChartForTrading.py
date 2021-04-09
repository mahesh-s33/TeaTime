import math

def gann_chart(x):
    table = [[0 for i in range(x)] for j in range(x)]
    row, column = get_start_cell_no(x)
    sequence = [-1, -1, 1, 1]  #[left,up,right,down]
    order = 0

    pattern = generate_pattern(x)
    counter = 0
    pattern_value_position = 0

    for i in range(1, x*x + 1):
        pattern_value = pattern[pattern_value_position]
        table[row][column] = i
        counter = counter + 1
        if order % 2 == 0:
            column = column + sequence[order % 4]
        else:
            row = row + sequence[order % 4]
        if counter == pattern_value:
            order = order + 1
            counter = 0
            if order < len(pattern):
                pattern_value_position = pattern_value_position + 1

    return table

def get_start_cell_no(x):
    return int(x/2), int(x/2)

def generate_pattern(x):
    pattern = []
    value = 1
    while(x > value):
        for i in range(2):
            pattern.append(value)
        value = value + 1
    pattern.append(value-1)
    print(pattern)
    return pattern

print(gann_chart(20))