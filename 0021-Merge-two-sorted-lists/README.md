# Merge two sorted lists (LeetCode #21)

**Date solved:** yyyy-mm-dd   
**Time spent:**  min  
**Difficulty:** Easy   

## ✔︎ Problem Summary


## ✔︎ My Thinking

```
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        out = []
        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                out.append(list1[i])
                i += 1
            else:
                out.append(list2[j])
                j += 1
            
        out.extend(list1[i:])
        out.extend(list2[j:])
        return out
```


## ✔︎ Insights from Discussion


## ✔︎ Key Points
- 
- 
