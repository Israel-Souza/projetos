import Coelhos1
    
def fib(n):
    a , b =  0 , 1
    Z = [a , b]
    while b < n:
        a , b = b , a + b
        Z.append(b)
    return Cubosfib(Z)

def Cubosfib(Z):
    for i in Z:
        print("A área é :      " , 6 * (i ** 2))
        if  i > 0 :
            X = i ** 3
            print(" O cubo terá volume de:         " ,  X , " m ** 3 ")
            print()
        elif i == 0:
            print(": - ( ")
            print()
            

