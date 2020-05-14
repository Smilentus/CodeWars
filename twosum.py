# My implementation
def two_sum(numbers, target):
    for n1 in range(len(numbers)):
        for n2 in range(len(numbers)):
            if n1 == n2: continue;
            if numbers[n1] + numbers[n2] == target:
                return [n1, n2]

# Best Solution
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]