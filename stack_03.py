def solution(infix):
    postfix = ""
    stack = []
    for i in infix:
        if i.isdecimal():
            postfix += i
        else:
            if i == '(':
                stack.append(i)
            elif i in ['*', '/']:
                while stack and (stack[-1] in ['*', '/']):
                    postfix += stack.pop()
                stack.append(i)
            elif i in ['+', '-']:
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
    while stack:
        postfix += stack.pop()
    return postfix


if __name__ == '__main__':
    print(solution("3*(5+2)-9"))
