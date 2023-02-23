# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요 -> 리스트를 쓸지 튜플을 쓸지 스스로 결정할 수 있는 능력
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) #불변 -> 한번 선언해서 끝까지 써야 함, const , final 같은것

# 선언
a = ()
b = (1,) # 원소가 하나일땐 , 를 찍어놔야 한다. 그래야 튜플로 인식함
c= (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain')) # 중첩튜플 가능


#인덱싱
print('>>>>>')
print('d : ', d[1])
print('d : ', d[0] + d[1] + d[1])
print('d : ', d[-1])
print('e : ', list(e[-1][1]))
print('e : ', e[-1])


#수정 정말 안될까?
# d[0] = 1500   X 안됨.


# 슬라이싱
print('>>>>>')
print('d : ', d[0:3])
print('d : ', d[2:])
print('d : ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3 ', c * 3)


# 튜플 함수
a = (5,2,3,1,4)
print('a : ', a)
print('a : ', a.index(3))
print('a : ', a.count(2))
print()

# 팩킹 & 언팩킹(Packing, and Unpacking) 파이썬에서 굉장히 중요한 특징 중 하나이다.

# 팩킹
t = ('foo', 'bar', 'baz', 'qux') # 4개의 원소를 하나로 묶은 것
print(t)
print(t[0])
print(t[-1])


# 언팩킹1
(x1, x2, x3, x4) = t    # 각각의 변수로 풀어서 할당
print(type(x1),type(x2),type(x3),type(x4))
print(x1,x2,x3,x4) 
print()

# 팩킹 & 언팩킹
t2 = 1, 2, 3   # 괄호 없어도 투플
t3 = 4,    # 괄호 생략가능하지만 , 붙여주면 하나의 정수라도 튜플

x1, x2, x3 = t2 # 언팩킹
x4, x5, x6 = 4, 5, 6  #언팩킹
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)