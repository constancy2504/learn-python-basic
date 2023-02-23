# Chapter03-2
# 파이썬 문자형

##### 문자형 중요 ######

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''


print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I', Boy

"""
자주 사용되는 Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""

print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')

print('a \t b')
print('a\nb')
print('a\"\"b')

escape_str1 = "Do you have a  \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check"

print(t_s1)
print(t_s2)
print()


# Row String
# 앞에 소문자r을 붙여주고 홑따옴표로 시작하면 된다
# 이스케이프 문자열을 사용하지 않기 위해 앞에 r을 붙여준 것
row_s1 = r'D:\python\test'

print(row_s1)
print()

# 멀티라인 입력 - 가독성을 위해 멀티라인으로 문자열을 입력하는 방법
# 역슬래시를 입력해주고 다음 라인에서 입력, 
multi_str = \
'''
sdfsdfs
dfffffffffff
ffffffffffff
fffffffffffffffffffffffffff'''

print(multi_str)
print()

multi_str2 = \
'asfasfasfasf'\
'asfsafsafasf'

print(multi_str2)
print()

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('z' in str_o1)
print('p' not in str_o2)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize())  # 첫글자를 대문자로 변환

print("endswith? : ", str_o2.endswith('s')) # 마지막 문자가 무엇인지? True/False 반환

print("replace", str_o1.replace("thon", 'Good')) # 앞의 문자열을 찾아서 뒤로 변경, (없으면 변경하지 않음)

print("sorted: ", sorted(str_o1)) # 하나하나씩 분리하여 리스트로 반환 (순서 아스키코드순)

print("split: " , str_o4.split(' ')) # 매개변수값을 기준으로 문자열 분리하여 리스트로 반환


# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # 해당 변수가 갖고있는 함수를 나열

for i in im_str:
    print(i)



# 슬라이싱
str_sl = "Nice Python"

print(len(str_sl))
# 슬라이싱 연습
print(str_sl[0:3])  # 0 ~ (3 - 1) 까지 나옴
print(str_sl[5:len(str_sl)])
print(str_sl[:len(str_sl)])
print(str_sl[5:])   # 생략하면 끝까지 출력
print(str_sl[1:9:2])    # 1~(9-1) 까지 2칸씩 건너뛰어서 가져와라
print(str_sl[-5:])
print(str_sl[1:-2])     # - 가 붙으면 무조건 뒤에서 시작
print(str_sl[::2])      # 처음부터 끝까지 2칸 간격으로 가져와라
print(str_sl[::-1])      # - 가 붙었으니 반대방향으로 1개씩 가져옴

 
# 아스키 코드
a = 'z'

print(ord(a)) # 값을 아스키 코드로
print(chr(122)) # 아스키코드를 값으로

