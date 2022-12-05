#Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.
n=int(input('Введите число: '))
my_list = []
divider = 2
while n !=1:
    while n%divider ==0:
        my_list.append(divider)
        n /= divider
    divider+=1
print(f'Список простых множителей числа: {my_list}')