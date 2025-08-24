# Merge two sorted lists (LeetCode #21)

**Date solved:** 2025-08-20   
**Time spent:**  min  
**Difficulty:** Easy   

## ✔︎ Problem Summary
二つの整列ずみリストノードを合成して一つの整列ずみリストを返す問題。同じ数字の場合はどちらの要素から追加しても構わない。

## ✔︎ My Thinking
はじめ、入力がリストノードではなく単なるリストだと誤認して解いた。その場合のコードが以下である。：
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
二つのリストの長さについてのwhile文を回し、小さい方をリストに追加し、追加した方のカウントを増やすというロジックである。片方の要素が先になくなった時、while文を抜けて残りのリストの要素を追加するように、whileの条件文はandを用いた。


## ✔︎ Insights from Discussion
ロジックそれ自体は正しかったが、リストとリストノードでは処理の書き方が違う。
ポインタ進めながら処理をするというのが基本方針。
一つ一つの要素を箱に入れて、次の要素に進むことで参照するため、リストのようなランダムな参照ができない。具代的には、node.nextで次のノード、node.valで今のノードの値を参照する。
先頭のノードも他のノードと同様に扱うために、ダミーノードを使用する。

## ✔︎ Key Points
- リストノードに対する処理は、一つ一つの要素を辿ることで参照する
