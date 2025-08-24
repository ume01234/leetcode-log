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
ただこれは、効率的な観点で最適解ではない。


## ✔︎ Insights from Discussion
.popによる操作は操作対象の要素の、後続の要素全てをスライドさせるので、時間計算量が多くなる。pop(i)でO(n-i)になる。  
2ポインタ法(上書きして前詰め)を利用した方法が最適解である。これは各要素を1回だけ読むので、時間計算量O(n)である。
この問題は先頭からk個だけが正しい列になっていれば合格なので、リスト全てを完成させる必要はない。

## ✔︎ Key Points
- 時間計算量の最適化のため、必要最低限の変更で回答することが望ましい。
