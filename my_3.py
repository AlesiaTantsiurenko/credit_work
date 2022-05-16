import openpyxl
import requests
import csv


def convert(k: str, t: str) -> str:
    """ Функция нахождения данных про ЗВО по указанному региону """
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
    if k in ls:
        r = requests.get(f'https://registry.edbo.gov.ua/api/universities/?ut={t}&lc={k}&exp=json')
        try:
            universities: list = r.json()
        except Exception as ex:
            return f"Не удалось получить доступ к учреждениям регина {k}"
        filtered_data = [
            {k: row[k] for k in ['university_name', 'university_address', 'post_index', 'registration_year']} for row in
            list(filter(lambda x: 1999 > int(x['registration_year'] or 0) > 1950, universities))]
        # Сортируем учебные заведения по году и записываем в файл значения ключей "Имя","Адресс","Индекс","Год",
        # учитывая предыдущее задание
        with open('registration_year_filter.csv', mode='w', encoding='cp1251', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            writer.writeheader()
            writer.writerows(filtered_data)
        return "Данные успешно записаны в файл registration_year_filter.csv!"
    else:
        return "Такого региона не существует!"


def main():
    print("Добро пожаловать в программу сортьолвки учебных заведений по году между 1950 и 1999 и записываем данные: "
          "название, адресс и почтовый индекс и год по региону!")
    print(
        "Дан следующий список кодов регионов: 01, 05, 07, 12, 14, 18, 21, 23, 26, 32, 35, 44, 46, 48, 51, 53, 56, 59, "
        "61, 63, 65, 68, 71, 73, 74, 80, 85")
    print(
        "Учреждения могут быть таких типов: 1 - Заведения высшего образования, 2 - Заведения профессионального ("
        "профессионально-технического) образования, 9 - Заведения профессионального высшего образования")
    choice = None
    while choice != "0":
        print(
            """
                0 - Выйти
                1 - Найти данные учреждений по региону и типу
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
            while True:
                try:
                    type_ = input("Введите тип учреждения: ")
                    if type_ in ['1', '2', '9']:
                        break
                    else:
                        print(f"Учреждения с типом {type_} не существует!")
                except ValueError:
                    print("Несоответствие типов!")
            print(convert(cod, type_))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
