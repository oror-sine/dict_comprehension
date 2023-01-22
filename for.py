# 1부터 10까지의 짝수를 key, 그 제곱 값을 value로 가지는 딕셔러니를 만들어라
num_dict = {}
for i in range(1,11):
    if i%2==0:
        num_dict[i]=i**2
print(num_dict)

# 1부터 100까지의 짝수를 key, 그 제곱 값을 value로 가지는 딕셔러니를 만들어라
num_dict2 = {}
for i in range(1,101):
    if i%2==0:
        num_dict2[i]=i**2
print(num_dict2)