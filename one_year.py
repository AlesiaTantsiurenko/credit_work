import openpyxl
import requests
import csv


def one_year(k: str, t: str, n_1: int) -> str:
    """ Функция нахождения данных про учреждения по году """
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
            list(filter(lambda x: x['registration_year'] == str(n_1), universities))]
        # Сортируем учебные заведения по году и записываем в файл значения ключей "Имя","Адресс","Индекс","Год",
        # учитывая предыдущее задание
        with open('filter_one_year.csv', mode='w', encoding='cp1251', newline='') as f:
            try:
                writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            except Exception as ex:
                return f"Нет доступа к учреждениям  года {n_1}"
            writer.writeheader()
            writer.writerows(filtered_data)
        return "Данные успешно записаны в файл filter_one_year.csv!"
    else:
        return "Такого региона не существует!"


def main():
    pass


if __name__ == '__main__':
    main()
