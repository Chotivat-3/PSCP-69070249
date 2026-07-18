"""Min"""
mn = float('inf')
n = int(input())
out = 0
if n <= mn :
    out = n
n = int(input())
if n <= out :
    out = n
n = int(input())
if n <= out :
    out = n
print(out)
