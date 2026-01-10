# happy number

N = int(input())

visitados = set()

while N != 1: 
    visitados.add(N)
    soma_q = 0
    soma_str = str(N)
    
    for digito in soma_str:
        d = int(digito)
        soma_q += d * d
        
    N = soma_q
    
    if N in visitados:
        print("No")
        exit()
        
print("Yes")       