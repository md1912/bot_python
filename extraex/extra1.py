seats = [4,1,5,9]
students = [1,3,2,6]

seats.sort()
students.sort()
print(seats)
print(students)
result = 0
for i in range(len(students)):
    result += abs(seats[i] - students[i] )
print(result)