# Write a function to find the longest common prefix string amongst an array of strings. what this.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"] 
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            while not s.startswith(prefix):
                # Shorten the prefix until it matches
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix