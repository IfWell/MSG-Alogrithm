#문제(1) ppt의 6번 문제 
# """로 둘러싸인 코드들은 없는 걸로 처리됨. 지우고 사용할 것

'''
for i in range(1, 1001):             #i에 1 ~ 100의 수가 순서대로 대입됨 
    for j in range(2, i+1):         #j는 i가 1과 자기자신(i) 이외의 수로 나눠지는지 확인하는 변수, j에 2부터 i까지 대입
        if(i % j == 0):             #i가 j로 나눠지면 
            break                   #반복문 탈출
    if(j == i):                     #반복문을 나온 시점에서 j가 i로 나눠지면 i는 i보다 작은 2이상의 수들로 모두 안나눠진다는 것
        print(i)                    #그런 조건을 만족하는 i 출력
'''

for i in range(1, 1001):             #i에 1 ~ 100의 수가 순서대로 대입됨 
    num = 0
    for j in range(1, i+1):         #j는 i가 1과 자기자신(i) 이외의 수로 나눠지는지 확인하는 변수, j에 2부터 i까지 대입
        if(i % j == 0):             #i가 j로 나눠지면 
            num+=1                  #num을 1 증가시킴
    if(num == 2):                   
        print(i)                    #그런 조건을 만족하는 i 출력
