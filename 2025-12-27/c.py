import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

stack=[]
for x in a:
    if stack and stack[-1][0]==x:
        stack[-1][1]+=1
        if stack[-1][1]==4:
            stack.pop()
    else:
        stack.append([x,1])

print(sum(c for _,c in stack))
