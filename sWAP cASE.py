def swap_case(s):
    newStr = ''
    for letter in s:
        if letter.isupper():
            newStr += letter.lower()
        else:
            newStr += letter.upper()
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)