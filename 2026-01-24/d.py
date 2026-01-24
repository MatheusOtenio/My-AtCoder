
import sys

input = sys.stdin.readline

def main():
    line1 = input().split()
    N = int(line1[0])
    Q = int(line1[1])
    
    A = list(map(int, input().split()))
    
    for _ in range(Q):
        query = list(map(int, input().split()))
        tipo = query[0]
        
        if tipo == 1:
            x = query[1] - 1
            
            A[x], A[x+1] = A[x+1], A[x]
            
        elif tipo == 2:
            l = query[1] - 1
            r = query[2] 
            
            resposta = sum(A[l:r])
            print(resposta)

if __name__ == '__main__':
    main()
