def student_1(name="Ekaterina", age="21", gr="K-45"):
    return name + " " + age + " " + gr

def count_sred_ball(OOP, *numbers):
    i = 1
    result = OOP
    for n in numbers:
        result += n
        i += 1
    return result / i

def main():
    student_1("Ekaterina", "21", "K-45")
    OOP = float()
    OOP=8
    print("информация о студенте:")
    print(student_1('Ekaterina', '21', 'K-45'))
    print("средний балл студента:")
    print(count_sred_ball(OOP, 78, 98))

main()
