import sys
data = sys.stdin.read().split()

X = int(data[0])
Y = int(data[1])
print(X * (2**Y))