# Remove element (LeetCode #27)

**Date solved:** 2025-08-22   
**Time spent:**  min  
**Difficulty:** Easy  

## ✔︎ Answer

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
