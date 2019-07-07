#insertion sort
#cf1. https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html
#cf2. https://seongjaemoon.github.io/python/2017/12/16/pythonSort.html

import random

a = random.sample(range(1,101),50) #1부터 100까지 숫자 중 50개 랜덤추출

print(a) #정렬 전의 a

for i in range(1, len(a)): #i는 a의 길이만큼 반복된다.
    for j in range(i, 0, -1): #본격적인 삽입정렬
        #ex)i가 1일때 0번째 값과 1번째 값을 비교하여 큰 값을 뒤에
        #ex)i가 2일때 1번째 값과 2번째 값을 비교하여 큰 값을 뒤에,
        #그 후 i-1인 1번째 값과 0번째 값을 비교하여 큰 값을 뒤에

        if a[j-1] > a[j]: #값 비교
            a[j-1], a[j] = a[j], a[j-1] #큰 숫자가 뒤에 오도록
        else : break #만약 해당하지 않으면 if 빠져나옴

print(a) #정렬 후의 a
