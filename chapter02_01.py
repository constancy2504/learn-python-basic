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


#format 사용 (d : 3, s : 'python' , f : 3.141592)

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
