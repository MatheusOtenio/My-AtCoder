import sys

input = sys.stdin.readline

def main():
    line1 = input().split()
    n = int(line1[0])
    m = int(line1[1])

    conflitos_count = [0] * (n + 1)

    for _ in range(m):
        pair = input().split()
        u = int(pair[0])
        v = int(pair[1])
        
        conflitos_count[u] += 1
        conflitos_count[v] += 1

    ans = []

    for i in range(1, n + 1):
        k = n - 1 - conflitos_count[i]

        if k < 3:
            ans.append(0)
        else:
            combinacoes = (k * (k - 1) * (k - 2)) // 6
            ans.append(combinacoes)

    print(*ans)

if __name__ == "__main__":
    main()
