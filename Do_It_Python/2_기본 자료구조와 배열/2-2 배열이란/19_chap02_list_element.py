# 자료형을 정하지 않은 리스트 원소 확인하기

x = [15, 64, 7, 3.14, [32, 55], 'ABC']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

"""
리스트의 원소와 복사

* 리스트를 복사할 때 사용하는 copy() 함수는 주의해서 사용해야함
- 리스트를 복사한 후 원솟값을 변경하면 복사된 원솟값까지 변경될 수 있음

x = [[1,2,3],[4,5,6]]
y = x.copy()    # x를 y로 얕은 복사
x[0][1] = 9

x >>> [[1,9,3],[4,5,6]]
y >>> [[1,9,3],[4,5,6]]

얕은복사 (shallow copy)이기 때문
"""

"""
깊은 복사(deep copy)를 이용하면됨

import copy     # deepcopy를 사용하기 위한 copy 모듈을 임포트
x = [[1,2,3],[4,5,6]]
y = copy.deepcopy(x)        # x를 y로 깊은 복사
x[0][1] = 9

x >>> [[1,9,3],[4,5,6]]     # 대입된 9가 출력됨
y >>> [[1,2,3],[4,5,6]]     # y 배열은 영향을 받지 않음
"""
