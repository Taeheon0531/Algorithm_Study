# 1부터 n까지 정수의 합 구하기 1 (while문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

"""
반복 구조(repetition structure) : 어떤 조건이 성립하는 동안 반복해서 처리하는 것 (loop)

while 문 :
실행하기 전에 반복을 계속할 것인지를 판단 -> 판단 반복 구조
조건식의 평가 결과가 참인 동안 프로그램의 명령문이 반복
while 조건식: 명령문
명령문 = 루프 본문
"""

print(f'i값은 {i}입니다.')
"""
n값이 5일 때 i 값은 6
i : 카운터용 변수
"""