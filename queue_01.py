from collections import deque


def solution(n, k):
    temp = deque([i for i in range(1, n+1)])
    while len(temp) > 1:
        for i in range(k):
            if i != k-1:
                temp.append(temp.popleft())
            else:
                temp.popleft()
    return temp.pop()


if __name__ == '__main__':
    print(solution(8, 3))
