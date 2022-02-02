"""
주어진 문자열을 거꾸로 뒤집은 문자열을 만드는 함수를 작성하라.

예) hello => olleh
예) happy new year => reay wen yppah

"""


def solution1(char_list):
    return "".join(reversed(char_list))


def solution2(char_list):
    return char_list[::-1]


if __name__ == '__main__':
    print(solution2("happy new year"))
