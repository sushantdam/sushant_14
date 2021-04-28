

students=[]
marks=[]
for i in range(5):
    n=input("Enter name of students: ")
    m=int(input("Enter marks of students:"))

    students.append(n)
    marks.append(m)
h=max(marks)
l=min(marks)
for i in range(5):
    if h==marks[i]:
        print("max marks student name is: ",students[i])
    if l==marks[i]:
        print("min marks student name is: ",students[i])
