from financing_state import financing_state
from financing_private import financing_private
from diapazon import diapazon
from one_year import one_year


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
                1 - Найти данные заведений по региону и типу
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
            choice = None
            while choice != "0":
                print(
                    """
                        0 - Выйти
                        1 - Отфильтровать заведения по году
                        2 - Отфильтровать заведения по форме финансирования
                        """
                )
                choice = (input("Ваш выбор - "))
                print()
                if choice == "0":
                    print("До свидания!")
                elif choice == "1":
                    choice = None
                    while choice != "0":
                        print(
                            """
                                0 - Выйти
                                1 - Задать диапазон
                                2 - Филтр только по одному значению
                                """
                        )
                        choice = (input("Ваш выбор - "))
                        print()
                        if choice == "0":
                            print("До свидания!")
                        elif choice == "1":
                            while True:
                                try:
                                    number_1 = int(input("Введите нижнююю границу [1615:2022]: "))
                                    if 1615 <= number_1 <= 2022:
                                        break
                                    else:
                                        print("Число должно находиться в диапазоне [1615:2022]!")
                                except ValueError:
                                    print("Несоответствие типов!")
                            while True:
                                try:
                                    number_2 = int(input("Введите верхнюю границу [1615:2022]: "))
                                    if 1615 <= number_2 <= 2022:
                                        break
                                    else:
                                        print("Число должно находиться в диапазоне [1615:2022]!")
                                except ValueError:
                                    print("Несоответствие типов!")
                            print(diapazon(cod, type_, number_1, number_2))
                        elif choice == "2":
                            while True:
                                try:
                                    number_3 = int(input("Введите год [1615:2022]: "))
                                    if 1615 <= number_3 <= 2022:
                                        break
                                    else:
                                        print("Год должно находиться в диапазоне [1615:2022]!")
                                except ValueError:
                                    print("Несоответствие типов!")
                            print(one_year(cod, type_, number_3))
                        else:
                            print("Извините, в меню нет пункта ", choice, ".")
                elif choice == "2":
                    choice = None
                    while choice != "0":
                        print(
                            """
                                0 - Выйти
                                1 - Государственная
                                2 - Частная
                                """
                        )
                        choice = (input("Ваш выбор - "))
                        print()
                        if choice == "0":
                            print("До свидания!")
                        elif choice == "1":
                            print(financing_state(cod, type_))

                        elif choice == "2":
                            print(financing_private(cod, type_))
                        else:
                            print("Извините, в меню нет пункта ", choice, ".")
                else:
                    print("Извините, в меню нет пункта ", choice, ".")

        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
