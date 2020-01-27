import sys


def second_lowest_grade():
    physic_students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        physic_students.append([name, score])
    
    physic_students = sorted(physic_students, key=lambda x: (x[1], x[0]))

    second_lowest_grade = 0
    for i in physic_students:
        if i[1] != physic_students[0][1]:
            second_lowest_grade = i[1]
            break
    
    for i in physic_students:
        if i[1] == second_lowest_grade:
            print(i[0])

def main():
    second_lowest_grade()

if __name__ == '__main__':
    sys.exit(main())

    
