# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o) - json 과 비슷함


# 선언
a = {
    'name' : 'Kim',
    'phone' : '01033337777',
    'birth': '870514'
    }
b = { 0 : 'Hello Python'} # key는 숫자로도 선언 가능
c = {'arr': [1,2,3,4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}


# 흔하지 않은 방식
# e = dict([
#     ('Name' , 'Niceman')
#     ('City' , 'Seoul')
# ])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)
# print('e : '. type(e), e)
print('f : ', type(f), f)
print()

# 출력
# print(' a : ', a['name1']) # 존재하지 않는 키 접근시 에러남
print('a : ', a.get('name1')) # 존재하지 않는 키 접근시 None을 리턴

print('b :', b[0])
print('b :', b.get(0))
print('f : ', f.get('City'))
print('f : ', f.get('Age'))