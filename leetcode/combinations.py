import itertools
from typing import List


def solution(n: int, k: int) -> List[List[int]]:
    result = []
    nums = [i for i in range(1, n + 1)]

    def dfs(combination: List[int]):
        if len(combination) == k:
            result.append(combination[:])
            return

        for i in nums:
            combination = combination[:]
            if i in combination or (combination and i < combination[-1]):
                continue
            combination.append(i)
            dfs(combination)
            combination.pop()

    dfs([])
    return result


def solution2(n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


def solution3(n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))


if __name__ == '__main__':
    print(solution3(4, 2))
