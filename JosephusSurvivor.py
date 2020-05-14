# My implementation
def josephus_survivor(n,k):
    arr = [i for i in range(1, n + 1)]
    ptr = k - 1
    while (len(arr) > 1):
        if ptr >= len(arr):
            ptr = ptr % len(arr)
        print('ptr -> ' + str(ptr))
        print('arr: ' + str(arr[ptr]))
        del arr[ptr]
        ptr += k - 1
        print(arr)
    return arr[0]

print(josephus_survivor(7, 3))

# Best Solution
def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1