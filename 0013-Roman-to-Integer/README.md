# problem name (LeetCode #13)

**Date solved:** 2025-08-16  
**Time spent:** 35min  
**Difficulty:** Easy  

## ✔︎ Problem Summary
The problem is to convert a Roman numeral string s, composed of the characters I, V, X, L, C, D, M, into an integer.  
In principle, this can be done by summing up the corresponding integer values, but depending on the order of the characters, subtraction is required instead.  

## ✔︎ My Thinking
At first, I solved it by creating branches with while and if statements to cover all possible patterns.   
Although the result was correct, the solution ended up being very poor due to having too many branches.  
A part of my answer below :  
```
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if s[i]=="V":
                    total += 5
                    i += 1  
            elif s[i]=="I":
                if i + 1 < len(s) and s[i+1]=="V":
                    total += 4
                    i += 2
                elif i + 1 < len(s) and s[i+1]=="X":
                    total += 9
                    i += 2
                else:
                    total += 1
                    i += 1
```

## ✔︎ Insights from Discussion
Through this process, I realized that the key is whether to add or subtract depending on the order of the numerals.  
With this perspective, the solution becomes much more concise.  
Furthermore, by using a dictionary to map each Roman numeral to its corresponding value, the code becomes more efficient.  

## ✔︎ Key Points
- Recognizing patterns in problem statements often leads to simpler solutions.  
- I use a lookahead guard (i + 1 < len(s)) so that when i is at the last character, the code won’t access s[i+1] and raise an IndexError.  
