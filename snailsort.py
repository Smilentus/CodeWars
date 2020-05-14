# My implementation
def snail(snail_map):
    res = []
    if len(snail_map) == 0:
        return res
    row_begin = 0
    row_end = len(snail_map) - 1
    col_begin = 0
    col_end = len(snail_map[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end+1):
            res.append(snail_map[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end+1):
            res.append(snail_map[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(snail_map[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(snail_map[i][col_begin])
        col_begin += 1

    return res

print(snail([]))

# Best Solution
def snail_steal(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a