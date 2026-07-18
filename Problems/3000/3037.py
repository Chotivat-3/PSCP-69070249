"""Top one"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
out = 0
if n1 >= n2 and n1 >= n3:
    out = n1
elif n2 >= n1 and n2 >= n3:
    out = n2
elif n3 >= n2 and n3 >= n1:
    out = n3
print(out)
