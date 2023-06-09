"""
이진검색 (binary search) - 데이터가 sort 되어있어야 함, 선형 검색보다 빠름

오름차순/내림차순 정렬된 배열에서 효율적

맨 앞 인덱스 pl
맨 끝 인덱스 pr
중앙 인덱스 pc

검색 시
pl = 0
pr = n-1
pc = (n-1) // 2

1. a[pc] < key 일 때
검색 범위가 a[pc+1] ~ a[pr]
따라서 pl 값을 pc+1로 업데이트

2. a[pc] < key 일 때
검색 범위가 a[pl] ~ a[pc-1]
따라서 pr 값을 pc-1로 업데이트

이진검색의 종료 조건
- a[pc]와 key가 일치하는 경우
- 검색 범위가 더 이상 없는 경우

이진 검색 알고리즘은 반복할 때마다 검색 범위가 거의 절반으로 줄어들므로
=> 검색하는데 필요한 비교 횟숫는 평균 logn
검색에 실패할 경우 log(n+1)
검색에 성공할 경우 logn - 1

"""