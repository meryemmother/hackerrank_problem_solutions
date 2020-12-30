if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

x = student_marks[query_name]
x = list(x)

islem = (x[0] + x[1] + x[2]) / 3

formatfloatted = "{:.2f}".format(islem)
print(formatfloatted)