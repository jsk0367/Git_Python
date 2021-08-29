#파이썬 심화
#클래스 메서드,인스턴스 메서드,스테틱 메서드

#기본 인스턴스 메서드

class Student(object):
    '''
    Student Class
    Author : Kim
    Date :2021.08.28
    Description : Class,Static,Instance Method
    '''

    #Class Variable
    tuition = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    #Instance Method(self가있으면 인스턴스 메서드)
    #클래스 안에서 셀프라는 인자를 통해서 어떤 결과를 리턴해 주는 것을 인스턴스 메서드라고 함
    def full_name(self):
        return '{},{}'.format(self._first_name,self._last_name)# 아규먼트 넣기

    #Instance Method
    def detail_info(self):
        return 'Student Detail Info : {},{},{},{},{},{}'.format(self._id,self.full_name(),self._email,self._grade,self._tuition,self._gpa)
    
    #Instance Method 등록금 인상 전
    def get_fee(self):
        return 'Before Tuition -> Id: {}, fee : {}'.format(self._id,self._tuition)
    
    #Instance Method, 등록금 인상 후
    def get_fee_culc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id,self._tuition * Student.tuition)

    def __str__(self):
        return 'Student Info -> name : {} grade : {} email : {}'.format(self.full_name(),self._grade,self._email)

    #Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please enter 1 or more')
            return 
        cls.tuition = per
        print('Succed tuition increased.')

    #Class Method
    @classmethod #cls가 Student메소드 자체이기때문에
    def student_const(cls,id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id,first_name, last_name, email, grade, tuition * cls.tuition, gpa) 


    #스테틱 - 공통으로 누구나 사용할수 있는 메소드
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scnolarship recipient.'

    
#핛생 인스턴스
studnet_1 = Student(1,'Kim','sia','student1@naver.com','1',400,4.5)
studnet_2 = Student(2,'Lee','jadam','student2@naver.com','1',500 ,4.3)

#기본정보
print(studnet_1)
print(studnet_2)
    
print()

#전체정보
print(studnet_1.detail_info())
print(studnet_2.detail_info())

#학비정보(인상전)
print(studnet_1.get_fee())
print(studnet_2.get_fee())

print()

#학비 인상(클래스 메소드 미사용)
# Student.tuition = 1.2
# print(studnet_1.get_fee_culc())
# print(studnet_2.get_fee_culc()) 

Student.raise_fee(1.5)

print()
#클래스 메서드 인스턴스 생성 실습

student_3 = Student.student_const(3,'Park','Mingi','Student3@naver.com',3,550,4.5)
student_4 = Student.student_const(4,'Jeong','Mihue','Student4@naver.com',4,600,4.1)

#전체 정보
print(student_3.detail_info())
print(student_4.detail_info())

#학생 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)
print()

#장학금 혜택 여부(스테이틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scnolarship recipient.'

print(is_scholarship(studnet_1))
print(is_scholarship(studnet_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

print()

#장학금 혜택 여부(스테이틱 메소드 사용)

print(Student.is_scholarship_st(studnet_1))
print(Student.is_scholarship_st(studnet_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()

print(studnet_1.is_scholarship_st(studnet_1))