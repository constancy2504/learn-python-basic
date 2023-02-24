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
print()


# 딕셔너리 추가
a['address'] = 'seoul'
print('a : ' , a)
print()

a['rank'] = [1,2,3]
print('a : ' , a)

# 딕셔너리 키의 갯수 세기
print('a : ', len(a))
print('a : ', len(b))
print('a : ', len(c))
print('a : ', len(d))
print()

#dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a : ', list(a.keys()))
print('b : ', list(b.keys()))
print('c : ', c.keys())
print('d : ', d.keys())


print()

print('a :', a.values())
print('b :', b.values())
print('c :', c.values())

print()

print('a :', a.items())
print('b :', b.items())
print('c :', c.items())

print();

print('a :', list(a.items()))
print('b :', list(b.items()))
print('c :', list(c.items()))

print();

print('a : ', a)
print('a : ', a.pop('name'))
print('a : ', a)

print()

print('f : ' , f)
print('f : ', f.popitem()) # 아무거나 임의대로 꺼내옴 , 그리고 status는 없어짐
print('f : ' , f)
print('f : ', f.popitem()) # 아무거나 임의대로 꺼내옴 , 그리고 status는 없어짐
print('f : ' , f)

print()

print('a : ', 'birth' in a) # 해당 키가 존재하는지 여부 // True
print('a : ', 'birth2' in a) # 해당 키가 존재하는지 여부 // False
print('a : ', 'address' in a) # 해당 키가 존재하는지 여부 // True
print('a : ', 'Address' in a) # 대소문자 구분
print()

#수정 다른방법
print('a : ', a)

a.update(birth='910904');
temp = {'address': 'Busan'}
a.update(temp)
print('a : ', a)