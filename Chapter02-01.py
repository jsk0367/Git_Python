#파이썬심화 
#데이터 모델(Date Model)
#NamedTuple실습
#파이썬의 중요한 핵심 프레임워크 ->시퀀스(Sequence),반복(Iterator),함수(Function),클래스(Class)


#객체->파이썬의 데이터를 추상화
#모든 객체 -> id, type->value 
#파이썬 -> 일관성

#일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import pi, sqrt

line_leng1 = sqrt((pt2[0] - pt1[0])**2+(pt2[1] - pt1[1])**2)
print('ex -1-',line_leng1)

#namedtuple 사용
from collections import  namedtuple

#namedtuple 선언
#클래스 형태로 받아들일수 있다

Point = namedtuple('Point','x y')#클래스를 인스턴스로 생성

#두점선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

#계산
line_leng2= sqrt((pt2.x - pt1.x)**2+(pt2.y - pt1.y)**2)

#출력
print('ex -2-',line_leng2)
print('ex -3-',line_leng1 == line_leng2)

#네임드 튜플 선언방법
Point1 = namedtuple('Point',['x','y'])
Point2 = namedtuple('Point','x,y')
Point3 = namedtuple('Point','x y')
Point4 = namedtuple('Point','x y x class', rename=True) #Default = False

#출력
print('EX2-1 -',Point1,Point2,Point3,Point4)

#Dict to Unpacking
temp_dict = {'x':75,'y':55}

#객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)#중복이 되지 않으므로  3,4이름은 rename으로 알아서 이름을 바꿔서 출력해준다
p5 = Point3(**temp_dict)

#출력
print('EX2-2-',p1, p2, p3, p4,p5)

print()

#사용
print('EX3-1-',p1[0] + p2[1]) #Indext error주의
print('EX3-2-',p1.x + p2.y)#클래스 변수 접근 방식

#unpacking
x,y = p3
print('EX3-3-',x+y)

#rename test
print('EX3-4',p4)

print()

#네임드 튜플메소드
temp = [52, 38]

#_make(): 새로운 객체 생성
p4 = Point1._make(temp)
print('EX4-1-',p4)

#_field(): 필드 네임 확인

print('EX4-2-',p1._fields, p2._fields, p3._fields)

#_asdict() orderedDict정렬된 딕셔너리반환
print('EX4-3-',p1._asdict(),p2._asdict)
print(dict(p1._asdict()))

#_replace(): 수정된 '새로운' 객체 반환
print('EX4-4-',p2._replace(y=100))

print()

#실 사용실습
#학생전체 그룹생성
#반 20명,4개의 반->(A,B,C,D) 번호

#네임드 튜플 선언
Classes = namedtuple('Classes',['rank','number'])

#그룹리스트 선언 
numbers = [str(n) for n  in range(1, 21)]
#str함수에 n을 넣고 1이 n에 들어오고 1을 str(n)문자로 바꿔서 리스트로 집어 넣는다
print(numbers)

ranks = 'A B C D'.split()

#List Comprehension
students = [Classes(rank,number) for rank in ranks for number in numbers]
print('EX5-1-',len(students))
print('EX5-2-',students)
print()

#가독성x
students2 = [Classes(rank,number) for rank in 'A B C D '.split() for number in [str(n) for n in range(1,21)]]
print('EX6-1-',len(students2))
print('EX6-2-',students2)
print()

#출력
for s in students:
    print('EX7-1-',s)

