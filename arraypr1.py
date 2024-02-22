# Function to maximize the sum of chosen numbers
def maximize_sum(n, k, array):
    # Sort the array in non-increasing order
    array.sort(reverse=True)
    
    # Initialize variables for the sum and count of distinct integers chosen
    total_sum = 0
    distinct_set = set()
    
    # Iterate through the sorted array and choose the first k distinct integers
    for num in array:
        if len(distinct_set) < k and num not in distinct_set:
            total_sum += num
            distinct_set.add(num)
    
    return total_sum

# Input number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input size of array and maximum number of distinct integers allowed
    n, k = map(int, input().split())
    
    # Input array of integers
    array = list(map(int, input().split()))
    
    # Calculate and print the maximum sum of chosen numbers
    print(maximize_sum(n, k, array))
