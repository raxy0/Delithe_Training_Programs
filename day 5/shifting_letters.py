#Shifting Letters says that we have given a string s and an array shifts.
#Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times. We have to return the final string after all shifts are applied.

###After Shifting the first 1 letter of s by 3, we have “dbc”.
#After shifting the first 2 letters of s by 5, we have “igc”.
#After shifting the first 3 letters of s by 9, we have “rpl”.
#Hence “rpl” is our final answer.   




def shifting_letters(s, shifts):
    cumulative_shift = 0
    result = ""

    for shift in reversed(shifts):
        cumulative_shift += shift
        index = len(s) - shifts.index(shift) - 1
        char_code = ord(s[index]) + cumulative_shift % 26
        if char_code > ord('z'):
            char_code -= 26
        result = chr(char_code) + result

    return result

# Example usage:
s = "abc"
shifts = [3, 5, 9]
result = shifting_letters(s, shifts)
print(result)  # Output: "rpl"
