def solution(postfix):
    stack = []
    for p in postfix:
        if p.isdecimal():
            stack.append(int(p))
        else:
            second = stack.pop()
            first = stack.pop()
            if p == "+":
                stack.append(first + second)
            elif p == '-':
                stack.append(first - second)
            elif p == '*':
                stack.append(first*second)
            elif p == '/':
                stack.append(first/second)
    return stack.pop()



if __name__ == '__main__':
    print(solution("352+*9-"))
