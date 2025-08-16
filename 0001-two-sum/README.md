# Two Sum (LeetCode #1)

**Date solved:** 2025-06-04
**Time spent:** about 20min  
**Difficulty:** Easy

## ✔︎ Problem Summary
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.  

## ✔︎ My Thinking
At first, I thought of a brute-force approach using two loops.　As below.   
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
```
This was not an error, and the result was correct, but it was computationally inefficient and could potentially take an extremely long time to run if scaled up.  

## ✔︎ Insights from Solution
The answer used a hash search method, which is a more efficient method.  
when iterating through the elements of a given array, it searches a hash map(dictionary) to see if there is an element with a step count that satisfies the target.  
if not, it repeatedly adds that element.  
the search time for a hash map is O(1) on average, which is shorter than the O(n^2) average for brute force searching.  
the built-in function *enumerate()* can retrieve the element and index simultaneously when looping with a for statement, etc.   

## ✔︎ Key Points
- Use Hash Map for quick complement lookup.  
- Use `enumerate()` to access both index and value when iterating.  
