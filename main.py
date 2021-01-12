import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

T = float(input('Введіть температуру газу в цельсіях: '))
P = float(input('Введіть тиск газу: '))
V = float(input('Введіть об\'єм газу: '))
Vm = (8.314 * (T + 273.15)) / P
#порахувала молярний об'єм, бо для молярної масси потрібна масса або густина газу якого в нас не має
print('Молярний обєм газу', Vm)
printTimeStamp('Anastasiia Kordonska')