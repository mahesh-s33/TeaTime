def check(str):
    dict = {'{':'}','[':']','(':')'}
    closeParenthesis = []
    for s in str:
        if s in dict:
            closeParenthesis.append(dict[s])
        elif s in closeParenthesis:
            closeParenthesis.remove(s)
    return closeParenthesis == []

if __name__ == '__main__':
    print(check('{}[]{{}}[{{()}]'))