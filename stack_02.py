def solution(input_list):
    stack = []
    result = 0
    for i, v in enumerate(input_list):
        if v == '(':
            stack.append((i, v))
        elif v == ')':
            temp = stack.pop()
            if i - temp[0] == 1:
                result += len(stack)
            else:
                result += 1

    return result


if __name__ == '__main__':
    print(solution("(((()(()()))(())()))(()())"))
