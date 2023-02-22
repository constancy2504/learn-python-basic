# Chapter02-1
# 파이썬 완전 기초
# Print 사용법

# 기본출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Hi! """)
print()


#seperator 옵션 매우 중요한 기초
print('P', 'Y', 'T', 'H','O','N', sep='')
print('010','7777','1234', sep='-')
print('python', 'google.com', sep='@')


print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션
import  sys
print('Learn Python', file=sys.stdout)
print()





# format 함수
# (d : 3, s : 'python' , f : 3.141592)

print('%s %s' % ('one', 'two'))
print('{0} {1}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s

# 10자리 확보하고 출력
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
print()
print('{:10}'.format('nice'))
print('%-10s' % ('nice'))

# _ 로 공백 채우기
print('{:_>10}'.format('nice'))
# 가운데 정렬
print('{:^10}'.format('nice'))

# 특정 자리까지만 출력 (절삭)
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
# 공간 10개 잡지만 왼쪽부터 5개만 출력해라
print('{:10.5}'.format('pythonstudy'))


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d' %(42))
print('{:4d}'.format(42))


# %f

print('%1.10f' % (3.1444242414))
print('{:f}'.format(42))

# 6자리가 나오고 소수는 2개만 나오게 했으니 3.14까지 나오고 나머지는 0으로 채움
print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))