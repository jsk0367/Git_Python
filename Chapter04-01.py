#파이썬 심화
#일급함수(일급객체)
#파이썬 함수 특징
#1.런타임 초기화
#2.변수 등에 할당 가능
#3.함수 인수 전달 가능
#4.함수 결과로 반환 가능
#함수 객체 예제

def factorial(n):
    '''Factorial Function n:int'''
    if n == 1: # n < 2
        return 1
    return n*factorial(n-1)

class A:
    pass

print('EX1-1-',factorial(10))
print('EX1-2-',factorial.__doc__)
print('EX1-3-',type(factorial),type(A))
print('EX1-4-',dir(factorial))
print()
print('EX1-5-',set(dir(factorial))-set(dir(A)))
print('EX1-5-',factorial.__name__)
print('EX1-5-',factorial.__code__)

#함수를 변수에 할당
var_func = factorial
print('EX2-1-',var_func(5))
print('EX2-1-',map(var_func, range(1,6)))
print('EX2-1-',list(map(var_func, range(1,6))))