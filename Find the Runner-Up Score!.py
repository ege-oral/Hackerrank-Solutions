if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    for i in arr:
        index = 0
        if index == 0:
            temp = i
            index += 1
        if temp < i:
            temp = i
    print(temp)
        
        
