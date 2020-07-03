my_list = ['winter', 'spring', 'summer', 'autumn']
my_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
m = int(input("Введите номер месяца от 1 до 12 "))

if m == 1 or m == 2 or m == 12:
    print(my_dict.get(1), "Значение по множеству")
    print(my_list[0], "Значение по списку")

elif m == 3 or m == 4 or m == 5:
    print(my_dict.get(2), "Значение по множеству")
    print(my_list[1], "Значение по списку")

elif m == 6 or m == 7 or m == 8:
    print(my_dict.get(3), "Значение по множеству")
    print(my_list[2], "Значение по списку")

elif m == 9 or m == 10 or m == 11:
    print(my_dict.get(4), "Значение по множеству")
    print(my_list[3], "Значение по списку")

