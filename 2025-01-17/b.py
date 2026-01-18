
N, M = map(int, input().split())
S = set(input())
T = set(input())
Q = int(input())

for _ in range(Q):
    w = input()
    w_chars = set(w)
    
    is_takahashi = w_chars.issubset(S)
    is_aoki = w_chars.issubset(T)
    
    if is_takahashi and not is_aoki:
        print("Takahashi")
    elif is_aoki and not is_takahashi:
        print("Aoki")
    else:
        print("Unknown")
