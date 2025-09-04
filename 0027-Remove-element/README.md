# Remove element (LeetCode #27)

**Date solved:** 2025-08-22   
**Time spent:**  min  
**Difficulty:** Easy  

## ✔︎ Problem Summary
This problem is to delete the specific number called val from the list.

## ✔︎ My Thinking
```
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
```


## ✔︎ Insights from Discussion


## ✔︎ Key Points
- 

