# 숫자로 구성된 배열이 주어졌을 때 그 배열에 중복된 숫자가 있는지 확인하는 함수를 작성하라.
# 중복된 숫자가 있다면 true 없다면 false.
# 예) 1 2 3 4 5 6 => false
# 예) 1 1 2 2 3 1 => true

def solution1(numbers):
    number_existence_dict = dict()
    for number in numbers:
        is_exist = number_existence_dict.get(number)
        if is_exist is None:
            number_existence_dict[number] = True
        if is_exist is True:
            return True
    return False

def solution2(numbers):
    numbers.sort()
    # numbers를 정렬하고 좌우 값을 비교
    # 정렬의 시간복잡도와 공간복잡도를 확인하기.
    # O(nlog(n))
    pass


def solution3(numbers):
    # 셋에 넣고 길이 비교
    # len()은 O(1), Set(numbers) 셋에 넣을 때 O(n)
    pass

if __name__ == '__main__':
    print(solution1([1, 1, 2, 3, 1]))
