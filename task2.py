def lastStudent(teacherInput):
    input = [int(x) for x in teacherInput.split(' ')]

    currStudent = input[2]
    for i in range(input[1]-1):
        if (currStudent < input[0]):
            currStudent += 1
        else:
            currStudent = 1
    return currStudent

teacherInput = input()
print(lastStudent(teacherInput))