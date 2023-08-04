#Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.

def has_pair_with_sum(arr, target_sum):
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)

    return False

# Example usage:
arr = [1, 4, 8, 3, 10, 5]
target = 13
result = has_pair_with_sum(arr, target)

if result:
    print("There are two integers whose sum is equal to the target value.")
else:
    print("There are no two integers whose sum is equal to the target value.")
