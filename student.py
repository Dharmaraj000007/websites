names=input()
students_names=[]
def add_student(names):
    students_names.append(names)
print(names)

marks=[60,80,60,60,60]
def calculate_average(marks):
    return sum(marks)/len(marks)
calculations=calculate_average(marks)
print(calculations)