"""Модуль для работы с управляющими конструкциями."""

"""1. Специальные операторы pass и ... 
Задание: 
Создайте функцию todo() с pass, а затем замените pass на реальную реализацию 
(например, возвращение строки "Готово!"). 
Аналогично — сделайте класс с методом, где пока стоит ....
"""

class Pass:
    """Класс для работы с pass."""
    def todo(self):
        """Создание функции с pass."""
        pass

print("\n№1")
my_pass = Pass()
result = my_pass.todo()
print(f"Результат с pass: {result}")


class Pass:
    """Класс для работы без pass."""
    def todo(self):
        """Создание функции с реализацией."""
        return "Без pass!"


my_pass = Pass()
result = my_pass.todo()
print(f"Результат: {result}")


class ThreePoints:
    """Класс для работы c ...."""
    def process_task(self):
        """Создание функции с ...."""
        ...

my_points = ThreePoints()
result = my_points.process_task()
print(f"Результат c ...: {result}")


class ThreePoints:
    """Класс для работы без ...."""
    def process_task(self):
        """Создание функции без ...."""
        return "Без ...!"


my_points = ThreePoints()
result = my_points.process_task()
print(f"Результат: {result}")


"""2. Консольный ввод/вывод 
Задание: 
Напишите программу, которая спрашивает имя и возраст пользователя, а затем печатает: 
Привет, <имя>, через 5 лет тебе будет <возраст+5>. 
"""

class InputOutputOfConsole:
    """Класс для консольного ввода/вывода."""
    def main(self):
        """Реализация ввода/вывода.

        Атрибуты:
        name - имя пользователя
        age - возраст
        age_after_5_year - возраст пользователя через 5 лет
        flag - флаг для корректного выходы из while после ввода корректного
        возраста
        """
        name = input("Введите имя: ")
        flag = '';
        while flag != "X":
            try:
                age = int(input("Введите возраст: "))
                flag = 'X'
            except ValueError:
                print("Введите число, а не буквы!")

        if age < 0:
            print("Возраст не может быть отрицательным! Повторите ввод!")
        elif age > 100:
            print("Введен слишком большой возраст! Повторите ввод!")

        age_after_5_year = age + 5
        print(f"Пользователю с именем {name}, через 5 лет исполнится {age_after_5_year}")

print("\n№2")
my_io = InputOutputOfConsole()
my_io.main()


"""3. Роль отступов 
Задание: 
Скопируйте код с неправильным отступом и исправьте его. 
Например: 
if True: 
print("Hello") 
Сделайте так, чтобы код работал корректно.
"""

class SpacesRole:
    """Класс для работы с отступами."""
    def main(self):
        """Просто правильный код."""
        if True:
            print("Верно!")

print("\n№3")
my_class_spaces_role = SpacesRole()
my_class_spaces_role.main()


"""4. Условный оператор и булева логика 
Задание: 
Напишите программу, которая принимает число и выводит: 
• "positive" — если больше нуля 
• "zero" — если равно нулю 
• "negative" — если меньше нуля 
Дополнительно: реализуйте проверку "делится ли число на 2 и на 3 одновременно" с 
помощью and.
"""

class NumberInput:
    """Класс для работы с условным оператором и булевой логикой."""
    def main(self):
        """Метод для работы с условным оператором и булевой логикой.

        Атрибуты:
        flag - для выхода из цикла
        number - введенное число
        flag - выход из цикла
        """
        flag = '';
        while flag != 'X':
            try:
                number = int(input("Введите число: "))
                flag = 'X'
            except ValueError:
                print("Введите число, а не буквы!")

        if number < 0:
            print("negative")
        elif number == 0:
            print("zero")
        else:
            print("positive")


print("\n№4")
my_number = NumberInput()
my_number.main()


"""5. Операции сравнения 
Задание: 
Напишите программу, которая спрашивает число и проверяет, входит ли оно в диапазон 
[10, 20]. 
Используйте цепочку сравнений (10 <= x <= 20). 
Дополнительно: напишите проверку x is None для переменной, в которую может 
записаться None.
"""

class RangeNumberCheck:
    """Класс для проверки принадлежности числа диапазону."""
    def main(self):
        """Метод для проверки принадлежности числа диапазону."""
        # Дальше не пойдем, пока не введут число
        flag = '';
        while flag != 'X':
            try:
                number = int(input("Введите число: "))
                flag = 'X'
            except ValueError:
                print("Введите число, а не буквы!")

        # Проверка на вхождение в диапазон [10, 20]
        if 10 <= number <= 20:
            print(f"Число {number} входит в интервал [10, 20] !")
        else:
            print(f"Число {number} не входит в интервал [10, 20] !")


print("\n№5")
my_number = RangeNumberCheck()
my_number.main()


"""6. match/case 
Задание: 
Напишите программу, которая принимает от пользователя строку: "start", "stop", 
"pause". 
Используйте match/case, чтобы напечатать: 
• "Запуск" 
• "Остановка" 
• "Пауза" 
• "Неизвестная команда" (если введено что-то другое).
"""

class MatchCase:
    """Класс для проверки какую строку ввел пользователь."""
    def main(self):
        """Класс для проверки какую строку ввел пользователь "start", "stop",
        "pause".
        """
        # Для введенной строки уберем пробелы и приведем к строчным буквам
        user_string = input("Введите 'start' или 'stop' или 'pause': ").strip().lower()

        match user_string:
            case "start":
                print("Запуск")
            case "stop":
                print("Остановка")
            case "pause":
                print("Пауза")
            case _:
                print("Неизвестная команда")


print("\n№6")
my_string = MatchCase()
my_string.main()


"""7. Циклы for и while 
Задание: 
1. Используя for, выведите квадраты чисел от 1 до 5. 
2. Используя while, попросите пользователя ввести пароль до тех пор, пока он не 
введет "1234". 
3. Добавьте else к циклу, чтобы вывести "Успешный вход". 
"""

class ForWhile:
    """Класс для работы с циклами for и while."""
    def loop_for(self):
        """Метод для вывода квадратов чисел от 1 до 5. """
        print("Вывод квадратов чисел от 1 до 5:")
        for i in range(1, 6):
            square = i ** 2
            print(f"Квадрат числа {i} = {square}")

    def loop_while(self):
        """Метод для просит пользователя ввести пароль до тех пор, пока он не
        введет "1234".
        """
        password = ''
        while password != '1234':
            password = input("\nВведите пароль: ")
            if password != '1234':
                print("Пароль не подходит! Повторите ввод!")
        else:
            print("Успешный вход!")

    def main(self):
        """Метод для вызова методов loop_for и loop_while"""
        self.loop_for()
        self.loop_while()


print("\n№7")
my_loops = ForWhile()
my_loops.main()


"""8. Исключения 
Задание: 
Напишите программу, которая делит число 10 на ввод пользователя. 
Обработайте случай, если введен 0 или строка вместо числа. 
Используйте try/except, а также finally для вывода "Программа завершена". 
"""

class MyException:
    """Класс для работы с исключениями."""
    def main(self):
        """Метод делит число 10 на ввод пользователя.
        Обработывает случай, если введен 0 или строка вместо числа.
        Используется try/except, а также finally для вывода "Программа
        завершена".

        Атрибуты:
        number - введенное число на которое будет разделено число 10
        flag - выход из цикла
        user_input - число введенное пользователем
        result - результат деления 10 на user_input
        """
        # Проверим пользователя, ввел ли он действительно число
        flag = '';
        while flag != 'X':
            try:
                user_input = float(input("На какое число хотите разделить число 10?: "))
                if user_input == 0:
                    print("На 0 делить нельзя! Повторите ввод!")
                else:
                    flag = 'X'
            except ValueError:
                print("Введите число, а не буквы!")

        result = 10 / user_input
        print(f"10 / {user_input} = {result}")


print("\n№8")
my_exception = MyException()
my_exception.main()


"""9. Модули и __name__ 
Задание: 
1. Создайте файл mymodule.py с функцией hello(), которая печатает "Hello from 
module". 
2. В mymodule.py измените код так, чтобы функция печатала сообщение только когда 
модуль запускается напрямую. 
3. Попробуйте запустить mymodule.py напрямую и импортировать его в другом файле. 
4*(Опционально). - Создать директорию (mypackage) с файлами __init__.py и mymodule.py - Создать newmodule.py на уровне созданной директории 
Должно получиться: 
mypackage/ 
|__   __init__.py 
|__   mymodule.py 
newmodule.py 
Скопировать в mymodule.py: 
def add(a, b): 
return a + b 
Скопировать в newmodule.py: 
from mypackage import add 
print(add(1, 2)) 
Не меняя код в newmodule.py нужно исправить ошибку импорта в этом файле.  
"""

print("\n№9")


"""10. Дополнительно 
Задания: 
1. Используя тернарный оператор, напишите проверку: "even" если число четное, 
иначе "odd". 
2. Реализуйте проверку строки с моржовым оператором: пусть вводится строка, и 
если она число — напечатать "Это число". 
"""

class Operations:
    """Класс для поиска четного числа и проверки строки на наличие цифр."""
    def ternary_operator(self):
        """Метод дял проверки четного числа.

        Атрибуты:
        numbers_set - набор четных и нечетных чисел
        i - интератор цикла for
        result - значение 'even' или 'odd'
        """
        numbers_set = [2, 5, 10, 17]
        for i in numbers_set:
            result = 'even' if i % 2 == 0 else 'odd'
            print(f"{i} - {result}")

    def walrus_operator(self):
        """Метод для проверки строки на наличие цифр."""
        if (user_input := input("Ведите строку: ").isdigit()):
            print("Это число!")

    def main(self):
        """Вызов методов ternary_operator и walrus_operator."""
        self.ternary_operator()
        self.walrus_operator()


print("\n№10")
my_operation = Operations()
my_operation.main()
