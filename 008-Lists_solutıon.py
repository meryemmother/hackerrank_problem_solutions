if __name__ == '__main__':
    N = int(input())

    li = []
    for _ in range(N):
        c = input().split()
        if c[0] == "insert":
            x1 = int(c[1])
            y1 = int(c[2])
            li.insert(x1, y1)
            # li.insert(c[1]),(c[2])
        elif c[0] == "remove":
            x1 = int(c[1])
            li.remove(x1)
        elif c[0] == "append":
            x1 = int(c[1])
            li.append(x1)
        elif c[0] == "pop":
            li.pop()
        elif c[0] == "sort":
            li.sort()
        elif c[0] == "print":
            print(li)
        elif c[0] == "reverse":
            li.reverse()

