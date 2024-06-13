# Prompt the user to enter a number
n = int(input())

# Iterate from 1 to n (inclusive)
for i in range(1, n+1):
    # Print the current number followed by a space
    print(i, end=" ")

    # Iterate from 0 to i-1 (inclusive)
    for j in range(i):
        # Print a '#' character for each iteration
        print("#", end="")

    # Print a new line after each iteration of the inner loop
    print()
