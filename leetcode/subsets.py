from typing import List
# https://leetcode.com/problems/subsets/

def solution(nums: List[int]) -> List[List[int]]:
    results = []

    def dfs(result, start_idx):
        results.append(result[:])

        for i in range(start_idx, len(nums)):
            result = result[:]
            result.append(nums[i])
            dfs(result, i + 1)
            result.pop()

    dfs([], 0)
    return results


def solution2(nums: List[int]) -> List[List[int]]:
    results = []

    def dfs(path, start_idx):
        results.append(path)

        for i in range(start_idx, len(nums)):
            dfs(path+[nums[i]], i + 1)


    dfs([], 0)
    return results


if __name__ == '__main__':
    print(solution2([1, 2, 3]))
