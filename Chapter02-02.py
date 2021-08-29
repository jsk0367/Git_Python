#매직 메소드 기초 설명
#__init__ 과 같이 __두개로 시작하는 속성

#기본형
print(int)

#모든 속성 및 메소드 출력
print(dir(int))

print()

n = 100

#사용
print('EX1-1-',n + 200) #와 밑에 출력은 같은 의미
print('EX1-2-',n.__add__(200))
print('EX1-3-',n.__doc__)
print('EX1-4-',n.__bool__(),bool(n)) #참과 거짓
print('EX1-5', n * 100, n.__mul__(100))

print()

#클래스 예제1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {} , {}'.format(self._name, self._height)

    def __ge__(self,x):
        print('Called >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self,x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__Method.')
         

#인스턴스 생성
s1 = Student('James',181)
s2 = Student('Mie',165)

#매직 메서드 출력
print('EX2-1-', s1 >= s2)
print('EX2-2-', s1 <= s2)

print('EX2-3-', s1 - s2)
print('EX2-4-', s2 - s1)
print('EX2-5-', s1)
print('EX2-6-', s2)

print()

#벡터(Vector)
class Vector(object):
    def __init__(self,*args):
        '''Create a Vector, example : v = Vector(1,2)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else: 
            self._x, self._y = args #언팩킹이 되서 알아서 값을 대입해줌

    def __repr__(self):
        '''returns the Vector Information'''
        return 'Vector(%r, %r)'%(self._x, self._y)

    def __add__(self, other):
        '''Returns the vector addittion of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))

#Vector인스턴스 생성
v1 = Vector(3,5)
v2 = Vector(15,20)
v3 = Vector()

#매직 메소드 출력
print('EX3-1-',Vector.__init__.__doc__)
print('EX3-2-',Vector.__repr__.__doc__)
print('EX3-3-',Vector.__add__.__doc__)
print('EX3-4-',v1,v2,v3)
print('EX3-5-',v1 + v2)
print('EX3-6-',v1 * 4)
print('EX3-7-',v2 * 10)
print('EX3-8-',bool(v1), bool(v2))
print('EX3-9-',bool(v3))