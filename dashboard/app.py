from collections import deque

# Creating a deque
fib = deque([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

# Appending data to deque
fib.append(89) # Adding to the right
print(fib)

# Remove data from deque
fib.popleft() # Removing from the left
print(fib)

length_of_fib = len(fib)
fib.clear() # Removes everything from deque

# Using max length for deque
fib_2 = deque([1, 1, 2, 3], maxlen=5)

# Simulate updataing the sequence with new values
fib_2.append(fib_2[-1]+fib_2[-2])
print(fib_2)

fib_2.append(fib_2[-1]+fib_2[-2])
print(fib_2)
