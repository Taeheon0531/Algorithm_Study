# 입력받은정수의 부호 (양수, 음수, 0) 출력하기

n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')

"""
흐름이 3개로 분기됨
1. n이 양수
2. 음수
3. 0
"""