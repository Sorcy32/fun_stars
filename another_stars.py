x = int (input("Введите количество рядов звезд: "))

for i in range(x):
    print('%s%s' % (' ' * (x-i-1), '*' * (i*2+1)))
