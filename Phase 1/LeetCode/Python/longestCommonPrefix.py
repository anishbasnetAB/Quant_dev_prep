# 14. Longest Common Prefix
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_common_prefix(strs):
    if not strs:
        return ""
    print( strs[1:])
    # Check each letter one by one
    for i in range(len(strs[0])):
        letter = strs[0][i]
        for word in strs[1:]:
            # If index i is too far or letter doesn't match, return the prefix so far
            if i >= len(word) or word[i] != letter:
                return strs[0][:i]
    
    return strs[0]

print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))     # ""