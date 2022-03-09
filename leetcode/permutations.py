import itertools
from typing import List


def solution(nums: List[int]) -> List[List[int]]:
    prev_elements = []
    result = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result


def solution2(nums: List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))


if __name__ == '__main__':
    print(solution2([1, 2, 3]))
