"""Dvine_10"""
n = int(input())
n = n//10
n = n*10
out = ""
while n >= 0 :
    out += str(n)
    out += " "
    n -= 10
print(out.strip())
