if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    records.sort(key = lambda x: (x[1], x[0]))
    min = records[0][1]
    sec_min = -1
    
    for i in records:
      if i[1] > min:
        sec_min = i[1]
        break
    for i in records:
      if i[1] == sec_min:
        print(i[0])
   