from math import pow, sqrt, factorial

class Calculator:

    def plus(self, a, b):
        result = a + b
        return result 
    
    def minus(self, a, b):
        result = a - b
        return result 
    
    def multi(self, a, b):
        result = a * b
        return result 
    
    def devi(self, a, b):
        result = a / b
        return result

class EngineerCalculator(Calculator):

    def cube(self, a, b):
        result = pow(a, b)
        return result
    
    def core(self, a):
        result = sqrt(a)
        return result

    def fact(self, a):
        result = factorial(a)
        return result

# создадим калькулятор индекса массы тела как объект класса инженерного калькулятора 

imt_calculator = EngineerCalculator()

def calculate_imt():
    weight = int(input("Введите ваш вес: "))
    height = int(input("Введите ваш рост: ")) / 100
    imt = round(imt_calculator.devi(weight, imt_calculator.cube(height, 2)), 2)
    print(f'Индекс массы тела составляет: {imt}')
    if imt < 18.5:      
        print("Дефицит массы тела")
    elif 18.5 <= imt <= 25.0:
        print("Масса тела в норме")
    elif 25.0 < imt <= 30.0:
        print("Избыточная масса тела")
    elif 30.0 < imt <= 35.0:
        print("Ожирение 1 степени")
    elif 35.0 < imt <= 40.0:
        print("Ожирение 2 степени")
    else:
        print("Ожирение 3 степени")

imt_calculator.calculate_imt = calculate_imt

while True:
    imt_calculator.calculate_imt()










    






