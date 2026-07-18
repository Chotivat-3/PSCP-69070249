"""min"""
mx = float('inf')
n = int(input())
x = int(input())
n-=1
out = 0
if x <= mx:
    out = x
while n:
    x = int(input())
    if x <= out:
        out = x
    n -= 1
print(out)
