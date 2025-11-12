# Словник студентів - виконав Сердюк Максим
students = {
    21: {
        "name": "Сердюк Максим Олександрович",
        "group": "КН-42/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 87,
            "Антикорупція та доброчесність": 94,
            "Програмування": 81
        }
    },
    22: {
        "name": "Бардакова Надія Володимирівна",
        "group": "КН-42/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 89,
            "Антикорупція та доброчесність": 90,
            "Програмування": 84
        }
    },
    23: {
        "name": "Колдомасов Максим Вікторович",
        "group": "КН-42/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 85,
            "Антикорупція та доброчесність": 97,
            "Програмування": 88
        }
    },
    24: {
        "name": "Помощнікова Наталія Андріївна",
        "group": "КН-42/1",
        "course": 2,
        "subjects": {
            "Алгоритми і структура даних": 86,
            "Антикорупція та доброчесність": 89,
            "Програмування": 90
        }
    },
    25: {
        "name": "Трапезніков Максим Валерійович",
        "group": "КН-42/2",
        "course": 1,
        "subjects": {
            "Алгоритми і структура даних": 88,
            "Антикорупція та доброчесність": 90,
            "Програмування": 85
        }
    },
}


def show_all(data):
    if not data:
        print("Словник порожній.")
    else:
        print("\n=== Словник студентів ===")
        for student_id, info in data.items():
            print(f"\nID студента: {student_id}")
            print(f"ПІБ: {info['name']}")
            print(f"Група: {info['group']}")
            print(f"Курс: {info['course']}")
            print("Предмети та оцінки:")
            for subject, grade in info['subjects'].items():
                print(f"   {subject}: {grade}")


#Пошук студентів за групою та курсом - Бардакова Надія
def find_students_by_group_and_course(data, group_name, course_number):
    found_students = {}
    for student_id, info in data.items():
        if info['group'] == group_name and info['course'] == course_number:
            found_students[student_id] = info
    return found_students


def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Переглянути весь словник студентів")
        print("2. Пошук студентів за групою та курсом")
        print("3. Рейтинг студентів за середнім балом")
        print("4. Редагування даних про студента")
        print("5. Додавання або видалення студента")
        print("0. Вихід")

        choice = input("\nВаш вибір: ")

        if choice == "1":
            show_all(students)

        elif choice == "2":
            group = input("Введіть назву групи: ")
            course = int(input("Введіть номер курсу: "))
            found = find_students_by_group_and_course(students, group, course)
            if found:
                print(f"\n=== Результати пошуку: Група {group}, Курс {course} ===")
                show_all(found)
            else:
                print(f"Студентів у групі {group} на курсі {course} не знайдено.")

        elif choice == "3":
            rating_by_average_grade(students)

        elif choice == "4":
            print("Редагування даних студента")

        elif choice == "5":
            print("Додавання або видалення студента")

        elif choice == "0":
            print("Роботу завершено.")
            break

        else:
            print("Некоректний вибір, спробуйте ще раз.")

#Функція рейтинг студентів за середнім балом - Помощнікова Наталія

def rating_by_average_grade(data):
    if not data:
        print("Словник порожній.")
        return

    averages = []
    for info in data.values():
        grades = list(info['subjects'].values())
        avg = sum(grades) / len(grades)
        averages.append((info['name'], avg))

    sorted_averages = sorted(averages, key=lambda x: x[1], reverse=True)

    print("\n=== Рейтинг студентів за середнім балом ===")
    for i, (name, avg) in enumerate(sorted_averages, start=1):
        print(f"{i}. {name} — середній бал: {avg:.2f}")

main()
