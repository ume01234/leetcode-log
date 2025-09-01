# Remove duplicates from sorted array  (LeetCode #26)

**Date solved:** 2025-08-21    
**Time spent:**  10min  
**Difficulty:** Easy  

## ✔︎ Problem Summary
This problem asks to return the number of elements in an ascending order list after removing the duplicates.  

## ✔︎ My Thinking
I corrected the process so that if the next element is a duplicate, it is removed from the list, and I continue referencing the same index while checking the subsequent elements.  
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                nums.pop(i)
                i += 0
            else:
                i += 1
        
        k = len(nums)
        return k
```
However, it is not the best practice.  


## ✔︎ Insights from Discussion
Operating with .pop increases the time complexity because this operation shifts all the elements after the target.  
In the case of .pop(i), the complexity is O(n−i).  
The best practice is to use the two-pointer method (overwrite and move forward).  
This method reads all elements only once, so the time complexity is O(n).  
For this problem, the requirement is that the first k elements are in the correct order; it is not necessary to update all the elements in the list.  

## ✔︎ Key Points
- To optimize time complexity, it is better to provide an answer with the minimum necessary changes.  
