# Reverse String

from typing import List
import time

'''
Do not allocate extra spce for another array, you must do this by modifying the input
array in-place with O(1) extra memory
'''

'''
Input: ['h','e','l','l','o'] => because it iterates the entire array
Output: ['o','l','l','e','h'] => as for not creating new arrays

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        '''
        Do not return anyting, modify s in-place instead.
        '''
        left = 0
        right = len(s) - 1
        while left < right:
            hold = s[left]
            s[left] = s[right]
            s[right] = hold
            left += 1
            right -= 1

'''
Solution

Time Complexity O(N)
Space Complexicty O(1)

1. Use 2 Pointers one at the first position and one at the end
2. Swap the two letters
3. Advance the pointers
'''

'''
Hints: you cannot use reverse


'''

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

'''
The function my_function(x) has a time complexity of O(n), where n is the length of the input string x.

Explanation:
What the function does:

x[::-1] is Python's slicing notation, which creates a reversed copy of the string x. The slice [:: -1] means "start from the end towards the first element, taking every element one by one."
Time Complexity:

Reversing a string in Python using slicing (x[::-1]) requires creating a new string and copying all characters from the original string x in reverse order.
Since every character in the input string needs to be accessed exactly once to create the reversed string, the time complexity is O(n), where n is the length of the input string.
Space Complexity:

The space complexity of this function is also O(n) because a new string of size n (the reversed version of x) is created.
'''

# TEST

# Testing the Solution
if __name__ == "__main__":
    # Function to measure execution time
    def measure_execution_time(func, *args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        return end_time - start_time

    # Test case 1
    test_case_1 = ['h', 'e', 'l', 'l', 'o']
    print(f"Original: {test_case_1}")
    execution_time = measure_execution_time(Solution().reverseString, test_case_1)
    print(f"Reversed: {test_case_1}")  # Expected: ['o', 'l', 'l', 'e', 'h']
    print(f"Execution Time: {execution_time:.10f} seconds")

    # Test case 2
    test_case_2 = ['a', 'b', 'c', 'd']
    print(f"\nOriginal: {test_case_2}")
    execution_time = measure_execution_time(Solution().reverseString, test_case_2)
    print(f"Reversed: {test_case_2}")  # Expected: ['d', 'c', 'b', 'a']
    print(f"Execution Time: {execution_time:.10f} seconds")

    # Test case 3
    test_case_3 = []
    print(f"\nOriginal: {test_case_3}")
    execution_time = measure_execution_time(Solution().reverseString, test_case_3)
    print(f"Reversed: {test_case_3}")  # Expected: []
    print(f"Execution Time: {execution_time:.10f} seconds")