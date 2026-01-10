
N = int(input())

placar = [0] * (N + 1)

x = 1
while x * x < N:
    y = x + 1
    while True:
        soma = x*x + y*y
        if soma > N:
            break
        placar[soma] += 1
        y += 1   
    x +=1
    
resp = []
for i in range(1, N+1):
    if placar[i] == 1:
        resp.append(i)
        
print(len(resp))
print(*resp)
