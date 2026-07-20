"""Tiktok"""
pit = input().split(" ")
R = int(pit[0])
X = int(pit[1])
Y = int(pit[2])
def cal (r=R,x=X,y=Y):
    """cal in on out"""
    r = r**2
    d = x**2 + y**2
    if r < d :
        print("OUT")
    elif r == d :
        print("ON")
    elif r > d:
        print("IN")
cal()
