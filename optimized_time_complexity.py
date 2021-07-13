
items=[0]
for i in range(int(input())):
    query=list(map(int, input().split()))
    if query[0]==1:
        items.append(max(query[1], items[-1]))
    elif query[0]==2:
        items.pop()
    else:
        print(items[-1])
