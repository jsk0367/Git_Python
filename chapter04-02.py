#파이썬 심화
#일급함수(일급객체)
#Decorator & Closure
#파이썬 변수 범위(global)

def func_v1(a):
    print(a)
    print(b)

#예외 
#func_v1(5)

b = 10
def func_v2(a):
    print(a)
    print(b)

func_v2(5) #b는 내부에 없기때문에 전역 영역에 있는 값을 가져와서 출력함

#예제3

b = 10
def func_v3(a):
    print(a)
    #print(b)
    b = 5 #로컬변수 b는 값이 할당되기 전에 출력되므로 에러발생 그때 전역 스코프는 참조되지 않는다

#func_v3(10)

from dis import dis

print('EX1-1-')
print(dis(func_v3)) 

#closure(클로저)
#반환되는 내부 함수에 대해서 선언된 연결을 가지고 참조하는 방식
#반환당시 함수 유효 범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다

a = 10
#스코프 범위가 독립적
print('EX2-1', a + 10)
print('EX1-2', a + 100)


#결과 누적
print('EX2-3', sum(range(1,51)))
print('EX2-4', sum(range(51,101)))

#클래스 이용
#더할때마다 누적되는 객체 생성

class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

#인스턴스 생성
avg_cls = Averager()

#누적 확인
print('EX3-1-', avg_cls(15))
print('EX3-1-', avg_cls(35))
print('EX3-1-', avg_cls(40))

#클로저 사용(Closure)
#함수안에 함수 사용
#전역변수 사용 감소
#디자인 패턴 적용

def closure_avg1():
    #free variable
    series =[]
    #클로저 영역
    def averager(v):
        #series =[] 유지불가 
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager #closure  함수리턴

avg_closure1 = closure_avg1()
print('EX4-1-',avg_closure1)
print('EX4-2-', avg_cls(15))
print('EX4-3-', avg_cls(35))
print('EX4-4-', avg_cls(40))


print()
print()
print('EX5-1', dir(avg_closure1))
print()
print('EX5-2', dir(avg_closure1.__code__))
print()
print('EX5-3', avg_closure1.__code__.co_freevars)
print()
print('EX5-4', dir(avg_closure1.__closure__[0].cell_contents))
print()
print()

#잘못된 클로저 사용 예

# def closure_avg2():
#     #free variable
#     cnt = 0
#     total = 0
#     #클로저 영역
     
#     def averager(v):
#         nonlocal cnt, total#주석 해제후 실행
#         #자유변수와 로컬 변수가 같음을 알려주는 예약어, 외부 자유 변수를 내부에서 쓰겠다
#         cnt += 1
#         total += v
#         print('def2 >>> {} / {}'.format(total, cnt))
#         return total /cnt
#     return averager

# avg_closure2 = closure_avg2()
# print('EX5-5-', avg_closure2(15))
# print('EX5-6-', avg_closure2(35))
# print('EX5-7-', avg_closure2(40))

#데코레이터 실습
#1. 중복 제거, 코드 간결
#2. 클로저보다 문법 간결
#3. 조합해서 사용 용이

#단점
#1. 디버깅이 어려움
#2. 에러의 모호함

#함수를 실행하는데 걸린 시간과 그 함수에서 사용 되었던 모든 매개변수를 출력해주는 함수를 실행해보자
import time

def perf_clock(func):#fuction 받음, 밖에서 실행할 함수
    def perf_clocked(*args):#측정이 완료됨(튜플형태로 받음)
        #시작 시간
        st = time.perf_counter()
        result = func(*args) #받은 함수 넣기
        # 종료 시간
        et = time.perf_counter() - st
        #함수 명
        name = func.__name__
        #매개변수
        args_str = ','.join(repr(arg)for arg in args)#콤마로 리스트 형태로 반환하는 매개변수 지정
        #출력
        print('result : [%0.5fs]%s(%s) ->%r' % (et, name, args_str, result))
        return result #= func
    return perf_clocked

@perf_clock         
def time_func(seconds):
    time.sleep(seconds)

@perf_clock 
def sum_func(*numbers):
    return sum(numbers)

@perf_clock 
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)
    #n이 2보다 작으면 1을 리턴하고 하니면  n * fact_func(n-1)을리턴

#데코레이션 미사용

non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

print('EX7-1-',non_deco1, non_deco1.__code__.co_freevars)
print('EX7-2-',non_deco1, non_deco2.__code__.co_freevars)
print('EX7-3-',non_deco1, non_deco3.__code__.co_freevars)

#함수가 실행할때 원하는 것을 꾸며줘서 부가적으로 함수가 동작될때마 계속 실행하게 하는것
# print('*'*40 ,'Called non deco -> time-func')
# print('EX7-4-')
# non_deco1(2)
# print('*'*40 ,'Called non deco -> sum-func')
# print('EX7-5-')
# non_deco2(100,200,300,500)
# print('*'*40 ,'Called non deco -> fact-func')
# print('EX7-6-')
# non_deco3(3)

print()

#데코레이터 사용
print('*'*40 ,'Called deco -> time-func')
print('EX7-7-')
time_func(2)

print('*'*40 ,'Called deco -> sum-func')
print('EX7-8-')
sum_func(10,20,30,40)

print('*'*40 ,'Called deco -> fact-func')
print('EX7-9-')
fact_func(100)