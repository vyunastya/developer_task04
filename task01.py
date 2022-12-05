#1 Вычислить число c заданной точностью d
import math
d = input('Введите точность: ')
print(f'{math.pi:.{len(d)-2}f}')