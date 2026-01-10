import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, w = map(int, input().split())
    c = list(map(int, input().split()))

    ciclo = [0] * (2 * w)
    
    for i in range(n):
        posicao = i % (2 * w)
        ciclo[posicao] += c[i]
    
    ciclo = ciclo + ciclo
    
    soma_atual = sum(ciclo[:w])
    menor_custo = soma_atual
    
    for i in range(2 * w - 1):
        soma_atual = soma_atual - ciclo[i] + ciclo[i + w]
        if soma_atual < menor_custo:
            menor_custo = soma_atual
            
    print(menor_custo)
