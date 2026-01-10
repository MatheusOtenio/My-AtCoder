import sys

data = sys.stdin.read().split()
N = int(data[0])
lista_cavalos = []

for i in range(N):
    tempo = int(data[i + 1])
    numero_cavalo = i + 1
    lista_cavalos.append((tempo, numero_cavalo))
lista_cavalos.sort()
print(lista_cavalos[0][1], lista_cavalos[1][1], lista_cavalos[2][1])