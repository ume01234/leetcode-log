# Remove duplicates from sorted array  (LeetCode #26)

**Date solved:** 2025-08-21    
**Time spent:**  10min  
**Difficulty:** Easy  

## ✔︎ Problem Summary
昇順に並んだリストについて、重複する要素を削除した上で要素の数を返す問題。

## ✔︎ My Thinking
while文で要素を順に参照していき、一つ前の要素と一致したらリストから.popし、もう一度同じインデックスを参照する。という処理を書いた結果、正解した。それが以下のコードである。
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

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



## ✔︎ Insights from Discussion


## ✔︎ Key Points