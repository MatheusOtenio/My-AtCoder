n,m=map(int,input().split())
s=input().strip()
t=input().strip()
best=10**9
for i in range(n-m+1):
    cur=0
    for j in range(m):
        a=int(s[i+j])
        b=int(t[j])
        cur+= (a-b) % 10
    if cur<best: best=cur
print(best)
