N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

num_water = N - K
current_sum = 0
ans = -1

for i in range(num_water, N):
    current_sum += A[i]
    if current_sum >= X:
        ans = i + 1
        break

print(ans)