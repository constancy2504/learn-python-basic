# Chapter03-3
# 파이썬 List
# 자료구조에서 중요
# 다른 언어에선 배열

# 리스트 자료형(순서0, 중복0, 수정0, 삭제0)

# 선언
a = []
b = list()
c = [70,75,80,85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captain'] # 서로 다른 자료형을 한 리스트 안에 담을 수 있다.
e = [1000, 1000, ['Ace', 'Base', 'Captine']] # list 안에 list를 담을 수 있음
f = [21.42, 'footbar', 3, 4, False, 3.14159]


# 인덱싱
print('>>>>>')
print('d : ', type(d) , d)
print('d : ', d[1])
print('d : ', d[0] + d[1] + d[1])
print('d : ', d[-1])
print('d : ', e[-1][1])
print('d : ', list(e[-1][1]))   # 문자를 배열로 분해해서 가져옴

# 슬라이싱
print('>>>>>')
print('d : ', d[1:3])
print('d : ' , d[2:])
print('e : ' , e[-1][1:3])


# 리스트 연산
print('>>>>>')
print('c + d', c + d);
print('c * 3', c * 3) # 배열의 원소를 3번 출력
print("'Test' + c[0]", 'Test' + str(c[0]))


# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))


# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c : ', c)
c[1:2] = ['a','b','c'] # 리스트 안에 리스트가 아닌, 리스트에 리스트의 값들이 추가
c[1:2] = [['a','b','c']] # 리스트 안에 리스트 추가

print(c)
print()
c[1] = ['a','b','c'] # 리스트 안에 리스트 추가
print(c)


c[1:3] = [] # 배열 값 제거
print(c)

del c[2] # 배열 값 제거
print('c : ', c);


# 리스트 함수
a = [5,2,3,1,4]
print('a : ', a)
a.append(10)
print('a : ', a)

a.sort()    # 오름차순 정렬
print('a : ' , a) 
a.reverse() # 반대로 구조를 변경
print('a : ' , a) 

print('a : ', a.index(3), a[3]) # 인덱스 번호로 값 가져오기

a.insert(2, 7) # 2번째 인덱스에 7 삽입
print('a : ', a)

a.reverse()
print('a : ', a)

# del a[6]
# print('a : ', a)
a.remove(10)    # 특정 값 제거
print('a : ', a)
print('a : ', a.pop()) # 기존 리스트에서 마지막 

print('a : ', a.count(4)) # list 에서 4가 몇개인지 

ex = [8,9]
a.extend(ex)    # 배열 연장
print('a : ', a)


# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)


