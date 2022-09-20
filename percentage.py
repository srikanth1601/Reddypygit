if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total=0
    for j in range(len(student_marks[query_name])):
        total=total+student_marks[query_name][j]
    avg=total/len(student_marks[query_name])
print("%.2f"%avg)
