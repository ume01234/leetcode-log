# Find the index of the first occurrence in a string (LeetCode #28)

**Date solved:** 2025-08-23   
**Time spent:**  min  
**Difficulty:** Easy   

## ✔︎ Answer

```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)

        for i, x in enumerate(haystack):
            if x == needle[0] and  haystack[i:i+m] == needle:
                return i 
        return -1
```