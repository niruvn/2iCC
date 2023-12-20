def ccounting_sum_pairs(arr, X):

    left, right = 0, len(arr) - 1
    count = 0

    while left < right:
        totalSum = arr[left] + arr[right]

        if totalSum == X:
            # Pair is found, move on to next
            count += 1
            left += 1
            right -= 1
        elif totalSum < X:
            left += 1
        else:
            right -= 1

    return count

# Input from the user
arr = list(map(int, input("Enter the array of integers in Ascending order ").split(',')))
X = int(input("Enter the total sum (X): "))

# Call the function
result = ccounting_sum_pairs(arr, X)
print(f"Output: {result}")
