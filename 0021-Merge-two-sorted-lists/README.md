# Merge two sorted lists (LeetCode #21)

**Date solved:** 2025-08-20   
**Time spent:**  20min  
**Difficulty:** Easy   

## ✔︎ Problem Summary
This problem is to return one sorted list from two list nodes.
It doesn’t matter which one is added first if the two numbers are the same.

## ✔︎ My Thinking
At first, I misunderstood that the input was not a list node but simply a list.
The incorrect code is below:
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
I used a while loop about the lengths of the two lists. If the smaller one was added to the list, then its counter was increased by 1.
I used and in the while loop because when one of them finished, it escaped from the while loop and added the rest of the list to the result.

## ✔︎ Insights from Discussion
I corrected the logic itself, but the coding is not the same between a list and a list node.
The basic policy is to process while moving the pointer.
When using a pointer, it cannot reference randomly like a list, because it references by putting each element in a box and moving to the next element.
In particular, node.next references the next node and node.val references the current node.
This code uses a dummy node to handle the front node like the other nodes.

## ✔︎ Key Points
- To process a list node, it traverses the elements one by one.
