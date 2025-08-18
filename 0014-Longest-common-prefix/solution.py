from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for j in range(len(strs[0])):          # 先頭単語の文字を1つずつ
            char = strs[0][j]
            for i in range(1, len(strs)):         # 他の単語を走査
                if j >= len(strs[i]) or strs[i][j] != char:
                    return result                 # 不一致が出たら即終了
            result += char                        # 全部一致したら追加
        return result