#파이썬 심화
#시퀀스 형
#해시테이블(hashtable) ->적은 리소스로  많은 데이터를 효율적으로 관리
#Dict -> key 중복허용x, Set -> 중복허용x
#Dict 및 Set 심화

#Dict 구조
print('EX1-1-')
#print(__builtins__.__dict__)

print()

#Hash 값 확인
t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50])

print('EX1-2-',hash(t1))
#print('EX1-3-',hash(t2)) 리스트형은 가변이기때문에 해시가 확인할 필요성이 없다

#지능형 딕셔너리(Comprehending Dict)
import csv

#외부 csv to list of tuple
with open('./resources/test1.csv','r',encoding='UTF-8') as f:
    temp = csv.reader(f)
    #Header Skip
    next(temp)
    #변환
    NA_CODES = [tuple(x) for x in temp]

print('EX2-1',)
print(NA_CODES)

#위 문서를 딕셔너리 형태로 만들기
n_code1 = {country : code for country, code in NA_CODES}# 키: 밸류
n_code2 = {country.upper() : code for country, code in NA_CODES}#국가는 대문자로 표시
print()

print('EX2-2',)
print(n_code1)


print()


print('EX2-3',)
print(n_code2)

#Dict Setdefault 예제
#딕셔너리는 키가 중복될수없다
source = (('k1','val1'),
                ('k1','val2'),
                ('k2','val3'),
                ('k2','val4'),
                ('k2','val5'))

new_dict1 = {}
new_dict2 = {}

#no use setdefault

for k,v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k]=[v]

print('EX3-1-',new_dict1)

#Use setdefault

for k,v in source:
    new_dict2.setdefault(k,[]).append(v) #첫번째인자는 있으면 k를 사용하고 없으면 빈리스트

print('EX3-2-',new_dict2)

#사용자 정의 dict 상속(userdict 가능)

class UserDict(dict):
    def __missing__(self,key):
        print('Called: __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self,key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()


User_dict1 = UserDict(one=1, two=2)
User_dict2 = UserDict({'one': 1, 'two': 2})
User_dict3 = UserDict([('one', 1),('two', 2)])

print('EX4-1-',User_dict1)
print('EX4-2-',User_dict2.get('two'))
print('EX4-3-','one' in User_dict3)
#print('EX4-4-', User_dict3['three'])
print('EX4-5-', User_dict3.get('three'))
print('EX4-6-','three' in User_dict3)

print()
print()

#immutable Dict

from types import MappingProxyType

d ={'key':'TEST1'}

#Read only
d_frozen = MappingProxyType(d)
print('EX5-1-',d, id(d))
print('EX5-2-',d_frozen, id(d))
print('EX5-2-',d is d_frozen, d == d_frozen )

#수정불가
#d_frozen['key1']='TEST2'

d['key2'] = 'TEST2'
print('EX5-4-',d)
print()
#Set구조(Frozenset) 
#단일자료형
s1 = {'Apple','Orange','Apple','Orange','Kiwi'}
s2 = set(['Apple','Orange','Apple','Orange','Kiwi'])
s3 = {3}
s4 = set() #not {}
s5 = frozenset({'Apple','Orange','Apple','Orange','Kiwi'})

#추가
s1.add('Melon')

#s5.add('Melon')
print('EX6-1-',s1,type(s1))
print('EX6-2-',s2,type(s2))
print('EX6-3-',s3,type(s3))
print('EX6-4-',s4,type(s4))
print('EX6-5-',s5,type(s5))

#선언 최적화

from dis import dis
print(dis('{10}'))
print(dis('set([10])'))

#지능형 집합
from unicodedata import name
print('EX7-1-')
print({name(chr(i),'') for i in range(0,256)})