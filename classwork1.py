def methods():
    level = int(input('Выберите уровень: '))
    text_1 = "пРиВеТ - МиР"
    text_2 = "Ботать это круто. Очень круто"
    text_3 = "1, 2, 3, 4"
    text_4a = "1234*&%^$"
    text_4b = "    abc1234  "
    if level == 1:
        print('Рассмотрим методы upper(), lower(), capitalize()')
        print(f'На вход программа получает строку: {text_1}')
        print('Вывод программы с применением соответствующего метода')
        print(f'upper(): {text_1.upper()}, lower(): {text_1.lower()}, capitalize(): {text_1.capitalize()}')
        test, operate = input('Введите тестовую строку: '), input('Выберите метод (без скобок): ')
        if operate == 'lower':
            print(f'На вывод получим: {test.lower()}')
        elif operate == 'upper':
            print(f'На вывод получим: {test.upper()}')
        elif operate == 'capitalize':
            print(f'На вывод получим: {test.capitalize()}')
        else:
            print('Такого метода нет на уровне')

    elif level == 2:
        print('Рассмотрим методы find(), replace(), count(), index()')
        print(f'На вход программа получает строку: {text_2}')
        print('Вывод программы с применением соответствующего метода')
        print(f'find("круто"): {text_2.find("круто")}, replace("круто", "классно"): {text_2.replace("круто", "классно")}, count("o"): {text_2.lower().count("о")}')
        print(f'index("ь"): {text_2.index("ь")}')
        test, operate = input('Введите тестовую строку: '), input('Выберите метод (без скобок): ')
        if operate == 'find':
            print(f'На вывод получим: {test.find(input('Введите, что хотите найти: '))}')
        elif operate == 'replace':
            print(f'На вывод получим: {test.replace(input('Введите, что хотите изменить: '), input('Введите, на что хотите изменить:'))}')
        elif operate == 'count':
            print(f'На вывод получим: {test.count(input('Введите, что хотите посчитать: '))}')
        elif operate == 'index':
            operator = input('Введите элемент, индекс которого хотите найти: ')
            if operator in test:
                print(f'На вывод получим: {test.index(input(operator))}')
            else:
                print('В вашей строке нет данного элемента')
        else:
            print('Такого метода нет на уровне')

    elif level == 3:
        print('Рассмотрим методы split(), join()')
        print(f'На вход программа получает строку: {text_3}')
        print('Вывод программы с применением соответствующего метода')
        print(f'split(","): {text_3.split(',')}, join(): {",".join(text_3.split(","))}')
        operate = input('Выберите метод: ')
        if operate == "join":
            operator = input('Введите символ, которым хотите разбить строку: ')
            test = input('Введите строку: ')
            print(f'На вывод получим: {' '.join(test)}')
        elif operate == "split":
            operator = input("Выберите символ, которым хотите разбить строку")
            test = input('Введите строки ч/з запятую: ')
            print(f'На вывод получим: {test.split(',')}')
        else:
            print("Такого метода нет на этом уровне")

    elif level == 4:
        print('Рассмотрим методы isdigit(), isalpha(), strip(), format()')
        print(f'На вход программа получает строки: {text_4a}, {text_4b}')
        print('Вывод программы с применением соответствующего метода')
        print('text_4a:')
        print(f'isdigit(): {text_4a.isdigit()}, isalpha(): {text_4a.isalpha()}, strip(): {text_4a.strip()}, format(): {format(text_4a)}')
        print('text_4b:')
        print(f'isdigit(): {text_4b.isdigit()}, isalpha(): {text_4b.isalpha()}, strip(): {text_4b.strip()}, ')
        operate =  input('Выберите метод (без скобок): ')
        if operate == 'isdigit':
            test = input('Введите тестовую строку: ')
            print(f'На вывод получим: {test.isdigit()}')
        elif operate == 'isalpha':
            test = input('Введите тестовую строку: ')
            print(f'На вывод получим: {test.isalpha()} ')
        elif operate == 'strip':
            test = input('Введите тестовую строку: ')
            print(f'На вывод получим: {test.strip()}')
        elif operate == 'format':
            print('Пусть нам нужно складывать разные числа:')
            print('(число 1) + (число 2) = ...')
            num1, num2 = int(input('Первое число: ')), int(input('Второе число: '))
            print('{} + {} = {}'.format(num1, num2, num1 + num2))
        else:
            print("Такого метода нет на этом уровне")
    elif level == 5:
        print('На этом уровне мы приведем вашу строку в нормальный вид')
        test = input('Введите строку, которую хотите улучшить: ')
        print(f'Так лучше: {test.strip().lower().capitalize()}')
    else:
        print('К сожалению пока что такого уровня не добавлено..(')

while True:
    methods()




