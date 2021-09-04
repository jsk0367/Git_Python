#파이썬 심화
#객체 참조 중요한 특징들
#python object reference

print('EX1-1-')
print(dir())

#id vs __eq__ (==) 증명
x = {'name':'kim','age':33,'city':'seoul'}
y = x
print('EX2-1-',id(x), id(y))
print('EX2-2', x == y) #x,y의 값이 같은지
print('EX2-3', x is y) #x,y의 id 값이 같은지, 같은 객체인지
print('EX2-4', x,y)

x['class'] = 10
print('EX2-5-',x,y)

print()
print()

z = {'name':'kim','age':33,'city':'seoul','class': 10}
print('EX2-6-',x,z)
print('EX2-6-',x is z) #둘은 아이디 값이 다르기때문에 false ,같은 객체인지
print('EX2-6-',x is not z) 
print('EX2-6-',x == z) #값이 같은가 true

#객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__)는 값 비교

print()
print()

#튜플 불변형의 비교
tuple1 = (10, 15, [100,1000])
tuple2 = (10, 15, [100,1000])

print('EX3-1-', id(tuple1), id(tuple2)) #값은 같지만 id는 다른 객체 
print('EX3-1-', tuple1 is tuple2)
print('EX3-1-', tuple1 == tuple2)
print('EX3-4-', tuple1.__eq__(tuple2))

print()
print()

#copy, deepcopy(깊은 복사, 얕은 복사)

#copy
tl1 = [10, [100, 105],(5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1-', tl1 == tl2)
print('EX4-2-', tl1 is tl2)
print('EX4-3-', tl1 == tl3) #값이 같다 리스트 생성자로 선언했기 때문에
print('EX4-4-', tl1 is tl3) 

#증명

tl1.append(1000)
tl1[1].remove(105)

print('EX4-5-', tl1)
print('EX4-6-', tl2)
print('EX4-7-', tl3)

print()
print(id(tl1[2]))
tl1[1] += [110,120]
tl2[2] += (110,120)

print('EX4-9-', tl1)
print('EX4-10-', tl2) #튜플 재할당(객체 새로 생성)
print('EX4-11-', tl3)

print()
print()

#deep copy

#장바구니
class Basket:
    def __init__(self, products = None): #아무것도 담지 않았을때는 non, 기본값
        if products is None:
            self._products = [] #상품을 안넣었을 경우 출력
        else:
            self._products = list(products) #list로 아이디 새로 할당
            #상품을 넣었을 경우 출력
        #기본값을 넣었을때는 []로 시작 값이 있을때는 초기화
    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple','Bag','TV','Snack','Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1-',id(basket1),id(basket2),id(basket3))
print('EX5-1-',id(basket1._products),id(basket2._products),id(basket3._products))
# EX5-1- 2132544974800 2132544974608 2132544973648
# EX5-1- 2132544995072 2132544995072 2132546781824
# 일반 카피는 인스턴스는 서로 다른 주소를 가리키고 있지만 프로덕트값은 동일
# 딥 카피는 세플 프로덕트 리스트 까지도 복사

print()

basket1.put_prod('Orange')
basket1.del_prod('Snack')

print('EX5-3-', basket1._products)
print('EX5-4-', basket2._products)
print('EX5-5-', basket3._products)

print()
print()

#함수 매개변수 전달 사용법

def mul(x,y):
    x += y
    return x

x = 10
y = 5

print('EX6-1-',mul(x,y))
print()

a = [10,100]
b = [5,10]

print('EX6-2-', mul(a, b), a, b)#가변형 a -> 원본 데이터 변경

c = (10, 100)
d = (5, 10)

print('EX6-2-', mul(c,d), c, d)#불변형 c -> 원본 데이더 변경 안됨

# 파이썬 불변형 예외
# str, bytes, frozenset, tuple : 사본생성 x -> 참조 반환

tt1 = (1,2,3,4,5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1-', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2-', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10,20,30,40,50)
tt5 = (10,20,30,40,50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3-', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4-', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))