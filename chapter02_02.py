#Chapter02-2

# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300) 
print(int(300))


# 예2)
# n -> 7777

n = 7777
print(n, type(n))
print()

m = n
print(m, n)
print(type(m), type(n))


#id(indentity)확인 : 객체의 고유값 확인 (C로 치면 메모리 주소값)

m = 800
n = 800

print(id(m))
print(id(n))
print()

print(id(m) == id(n))
print(m == n)


# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates 파이썬에서 변수선언 시 많이 사용함
# ex) student_grade = 3

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8


# 1AGE = 9 # error


# 예약어는 변수명으로 불가능
# ex) for, as, class,    python reserved words 
