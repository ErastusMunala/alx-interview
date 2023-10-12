#!/usr/bin/python3
'''The minimum operations coding challenge.
'''

def minOperations(n):
    if n <= 1:
        return 0  # No operations needed for n <= 1

    operations = [0] * (n + 1)  # Initialize an array to store the number of operations

    for i in range(2, n + 1):
        # Initialize with a worst-case value
        operations[i] = i
        for j in range(2, i):
            if i % j == 0:
                # If i is divisible by j, it means we can copy j characters i/j times
                # and then paste them i/j times to get i characters
                operations[i] = min(operations[i], operations[j] + i // j)

    return operations[n]

# Example usage:
n = 9
print(minOperations(n))  # Output: 6

