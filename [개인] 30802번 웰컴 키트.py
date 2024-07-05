N = int(input())
T_shirt = list(map(int, input().split()))
T, P = map(int, input().split())
for i in range(6):
    if T_shirt[i]%T == 0:
        T_shirt[i] = T_shirt[i]//T
    else:
        T_shirt[i] = T_shirt[i]//T+1
print(sum(T_shirt))
print(N//P, N%P)