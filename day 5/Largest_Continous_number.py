# Find the largest continuous sequence in an array which sums to zero.
#Example:
#: {1 ,2 ,-2 ,4 ,-4}
#: {2 ,-2 ,4 ,-4}
# : If there are multiple correct answers, return the sequence which occurs first in the array,
def largest_continuous_sequence(arr):
    cumulative_sum_map = {0: -1}  # Initialize with a cumulative sum of zero at index -1
    max_length = 0
    start_index = 0

    cumulative_sum = 0
    for i, num in enumerate(arr):
        cumulative_sum += num

        if cumulative_sum in cumulative_sum_map:
            current_length = i - cumulative_sum_map[cumulative_sum]
            if current_length > max_length:
                max_length = current_length
                start_index = cumulative_sum_map[cumulative_sum] + 1

        if cumulative_sum not in cumulative_sum_map:
            cumulative_sum_map[cumulative_sum] = i

    return arr[start_index:start_index + max_length]

# Example usage:
arr = [1, 2, -2, 4, -4]
result = largest_continuous_sequence(arr)
print(result)
