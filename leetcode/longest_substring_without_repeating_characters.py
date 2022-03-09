def solution(s: str) -> int:
    ans = 0
    l_cursor = 0
    used = {}
    for r_cursor, char in enumerate(s):
        if char in used and l_cursor <= used[char]:
            l_cursor = used[char] + 1
        else:
            ans = max(ans, r_cursor - l_cursor + 1)
        used[char] = r_cursor
    return ans

