# Palindrome Number (LeetCode #9)

**Date solved:** 2025-08-15  
**Time spent:** about 20min  
**Difficulty:** Easy  

## ✔︎ Problem Summary
Given an integer `x`, return `true` if `x` is a *palindrome*, and `false` otherwise.
A `palindrome` is an integer that is the same whether read from right to left or right to left.

## ✔︎ My Thinking
I came up with a method to convert the input x from an integer to a string, and use an index to match the first and last elements in order.  
At first, I tried setting `left = 0`, `right = -1` and updating it each time the first match was completed, but I got stuck because I couldn't determine whether it was finished.I got the correct solution by setting `right = len(x) - 1` and determining whether it was finished when `left` and `right` matched.  

## ✔︎ Insights from Disscssion
We've figured out that the most efficient solution without converting to a string is to reverse only the right half of the input x.  
This works by building up the numbers of the input x read from the bottom up in the variable `rev` and comparing it with the numbers from the top.  
We can also further increase efficiency by excluding only negative numbers and multiples of 10 other than 0 before the loop starts.  

Here is a more optimal version:  
```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10
```

## ✔︎ Key Points
- Eliminating exceptions before entering the loop can improve efficiency.
- Reversing part of the number provides a way to check whether it is a palindrome.

