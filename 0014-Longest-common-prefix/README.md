# Longest Common Prefix (LeetCode #14)

**Date solved:** 2025-08-18   
**Time spent:**  30min  
**Difficulty:** Easy   

## ✔︎ Problem Summary
Output the longest common prefix from a given array of strings.   

## ✔︎ My Thinking
I put the first word from the array of strings into "first_word".  
I made a logic that is a double loop, containing a word loop outside and a letter loop inside, and if the two letters are the same, it adds the letter to "result".  
That code is below:  

```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        first_word = strs[0]

        for i in range(1, len(strs)): 
            limit = min(len(first_word), len(strs[i]))
            for j in range(limit):
                if strs[i][j] == first_word[j]:
                    result += strs[i][j]
            return result

        return result
```
However, it leads to mistakes.  
This problem needs matching in all words in the array. My code can check just matching between "first_word" and the others.  
In addition, if the condition in the if statement is “add when equal,” the code will only gather partial matches from each word, and it cannot guarantee that all words are equal at the same position (column).   
As a result, the prefix of the first word, or sometimes of another word, may be returned incorrectly.  

## ✔︎ Insights from Discussion
The correct logic is that the outer loop should be characters and the inner loop should be words.   
The if statement inside should be the condition for stopping the loop, and the loop ends when a mismatch is found.  
This means we check each character of the first word, but the comparison is whether all words in the array have the same character at that position.     
Adding is correct, but it should be done only when all words match.  
When the outer loop is words and the inner loop is characters, we need to confirm correctness across all words before adding.   
Because of that, the logic becomes a bit more complicated.   
Also, I found that running the code without storing the first_word made the execution time slightly faster, although the readability might be lower.  

## ✔︎ Key Points
- To find the common part across all elements, it is important to look at each character of the first word and check the same position of all words.   
- In other words, we need a column-first perspective.  

