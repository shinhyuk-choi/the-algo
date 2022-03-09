from typing import List


# https://leetcode.com/problems/combination-sum/
def solution(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(items):
        if sum(items) == target:
            result.append(items[:])
        if sum(items) >= target:
            return

        for i in candidates:
            items = items[:]
            if items and items[-1] > i:
                continue
            items.append(i)
            dfs(items)
            items.pop()

    dfs([])
    return result


def solution2(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(items, start):
        if sum(items) == target:
            result.append(items[:])
        if sum(items) >= target:
            return

        for i in range(start, len(candidates)):
            items = items[:]
            items.append(candidates[i])
            dfs(items, i)
            items.pop()

    dfs([], 0)
    return result


def solution3(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


if __name__ == '__main__':
    print(solution3([2, 3, 6, 7], 7))
