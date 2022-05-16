import openpyxl  # импортируем модуль работы с Ексель документами
import requests  # импортируем модуль работы с HTTP запросами
import csv  # импортируем модуль для записи данних в файл csv


def convert(k: str) -> str:
    """ Функция нахождения данных про ЗВО по указанному региону"""
    book = openpyxl.open('regions.xlsx',
                         read_only=True)  # открываем файл ексель на чтение( атрибут read_only) и сохраняем в
    # переменную book
    sheet = book.active  # не обязательная строка - переход на активный лист в книге (важно при большом количестве
    # листов в книге)
    ls = []
    for row in range(2,
                     sheet.max_row + 1):  # цикл по строкам начиная со второй и заканчивая автоматически вычесляемой
        # последней позицией строки (sheet.max_row+1, когда строк в документе много)
        number = sheet[row][0].value  # в переменную number сохраняем значение из первого столбца - номер региона
        ls.append(number)  # добавляем значение (строка) в список
    if k in ls:  # если введенное пользователем число есть в списке, тогда производим запрос
        r = requests.get(
            f'https://registry.edbo.gov.ua/api/universities/?ut=1&lc={k}&exp=json')  # производим запрос с помощью
        # метода get(), ut - 1 (ЗВО), lc = k - номер регион, формат json
        try:
            universities: list = r.json()  # получаем список словарей
        except Exception as ex:
            return f"Не удалось получить доступ к учреждениям регина {k}"
        with open('universities.csv', mode='w', encoding='cp1251',
                  newline='') as f:  # открываем на запись наш файл, устанавляваем кодироаку 'cp1251' для вменяемого
            # отображения кириллицы, именуем файл как f
            writer = csv.DictWriter(f, fieldnames=universities[
                0].keys())  # используем класс csv.DictWriter, в качестве заголовков берем ключи наших словарей
            writer.writeheader()  # запись заголовков
            writer.writerows(universities)  # запись данных
        with open(f'universities_{k}.csv', mode='w', encoding='cp1251', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=universities[0].keys())
            writer.writeheader()
            writer.writerows(universities)
        return f"Данные успешно записаны в файл universities.csv и universities_{k}.csv!"  # сообщение о том, что
        # запись данных прошла успешно
    else:
        return "Такого региона не существует!"  # сообщение о том, что региона с таким числом нету


def main():
    print(" Добро пожаловать в программу импортирования данных ЗВО по региону!")
    print(
        "Дан следующий список кодов регионов: 01, 05, 07, 12, 14, 18, 21, 23, 26, 32, 35, 44, 46, 48, 51, 53, 56, 59, "
        "61, 63, 65, 68, 71, 73, 74, 80, 85")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти данные ЗВО по региону
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    cod = input("Введите код региона: ")
                    break
                except ValueError:
                    print("Несоответствие типов!")
            print(convert(cod))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
