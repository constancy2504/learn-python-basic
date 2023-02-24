# Chapter 03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서x)

# 선언
a = set()
b = set([1,2,3,4,4,4])  # 중복된 데이터 허용하지 않음
c = set([1,5,6,7])      
d = set([1,2,'Pen', 'Cap','Plate'])
e = {'foot','bar','baz','foo','qux'}
f = {42,'foo',(1,2,3), 3.14159}

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)
print('e : ', type(e), e)
print('f : ', type(f), f)
print()

print('a : ', 2 in a) # 값 있는지 여부

print()
# 튜플 변환(set => tuple)
t = tuple(b)
print('t : ', type(t), t)
print('t : ', t[0], t[1:3])
print()

# 리스트 변환(set -> List)
l = list(c)
l2 = list(e)

print('l : ', l)
print('l2 : ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('s1 & s2', s1 & s2) # 교집합
print('s1 & s2', s1.intersection(s2)) # 교집합

print('s1 & s2', s1 | s2) # 합집합
print('s1 & s2', s1.union(s2)) # 합집합

print('s1 & s2', s1 - s2) # 차집합
print('s1 & s2', s1.difference(s2)) # 차집합

# 중복 원소 확인
print('s1 & s2 :' , s1.isdisjoint(s2)) # 교집합이 있으면 False, 없으면 True / dis 가 붙었기때문에 반대로 나온다.
print()

s3 = set([4,5,6])
s4 = set([4,5,6,7,8,9])
# 부분 집합 확인
print('부분집합 : ', s3.issubset(s4))
print('부분집합 : ', s4.issuperset(s3))
print()


# 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print('s1 : ', s1);


# s1.remove(2)
print('s1 :', s1)
# s1.remove(7) # 없는 원소를 지우면 에러 예외처리 발생

s1.discard(3)
print('s1 :', s1)
s1.discard(7) # discard로 삭제 시 예외처리 발생하지 않음

s1.clear() # 전부 삭제
print('s1 :', s1)


