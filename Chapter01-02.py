#클래스 재선언
from typing import SupportsRound


class Student():
    '''
    Student class
    Aouthor : Kim
    Date : 2021.08.28
    '''
    #클래스 변수(모두다 쓸수있는 변수)
    Student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        #인스턴스 변수 -> 인스턴스 변수는 각 인스턴스화 된 이름으로만 접근가능
        self._name = name
        self._number = number 
        self._grade = grade
        self._details = details
        self._email = email

        Student.Student_count += 1 #클래스 변수 접근시 클래스 변수명 + .찍고 접근

    def __str__(self):
        return 'str {}'.format(self._name)
        
    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id :{}'.format(id(self)))
        print('Student Details : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.Student_count -= 1

#self의 의미
student1 = Student('cho',2,3,{'gender':'Male','score1':57,'score2':55})
student2 = Student('jang',4,1,{'gender':'Fmale','score1':99,'score2':75})
        
#Id 확인
print(id(student1))
print(id(student2))

print(student1._name == student2._name)
print(student1 is student2)

#dir & __dict__ 확인
print(dir(student1)) #넓고 전체적으로 확인하고 싶을때
print(student1.__dict__)

#Doctring
print(Student.__doc__)

#실행
student1.detail_info()
student2.detail_info()

#에러 
#Student.detail_infor()

Student.detail_info(student1)
Student.detail_info(student2)

#비교
print(student1.__class__,student2.__class__)
print(id(student1.__class__)== id(student2.__class__))

#인스턴스 변수
#직접접근(PEP문법적으로 권장x)

print(student1._name,student2._name)
print(student1._email,student2._email)

print()
print()

#클래스 변수(모두가 공유하는 변수)

#접근
print(student1.Student_count)
print(student2.Student_count)
print(Student.Student_count)

print()
print()

#공유 확인
print(Student.__dict__)#student_count 변수 있음
print(student1.__dict__)#student_cout 변수 없음

#인스턴스 네임스페이스에 없으면 스스로 상위에서 검색
#즉, 동일한 이름으로 변수 생성가능(인스턴스 검색후(없으면)-> 상위(클래스 변수,부모클래스 변수 검색))
#역은 성립하지않는다 -> 클래스 변수에없고 인스턴스 변수에 있는것은 클래스 변수로 출력불가

del student2

print(student1.Student_count)
print(Student.Student_count)
