# 튜플의 스캔
'''
x = [] 를 x = () 로 수정하는 것만으로 스캔 가능
'''

# 이터러블 (반복 가능)
"""
문자열, 리스트, 튜플, 집합, 딕셔너리 등의 자료형 객체는 모두 이터러블
이터러블 객체는 원소를 하나씩 꺼내는 구조
이터러블 객체를 내장함수인 iter() 의 인수로 전달하면 그 객체에 대한 어터레이터(반복자)를 반환
이터레이터는 데이터의 나열을 표현하는 객체
이터레이터의 __next__ 함수를 호출하거나
내장함수인 next() 함수에 이터레이터를 전달하면 원소를 순차적으로 꺼낼 수 있음
꺼낼 원소가 더 이상 없는 경우에는 StopIteration 으로 예외 발생
"""

