"""Gift"""
pit = input().split(" ")
R = float(pit[0])
H = float(pit[1])
G = float(pit[2])
def cal (r=R,h=H,g=G):
    """Packaging"""
    p = 3.14
    w = (r*2)+h
    w = round(w,2)
    w = f"{w:.2f}"
    l = (2*p*r)+g
    l = round(l,2)
    l = f"{l:.2f}"
    print(f"{w} {l}")
cal()
