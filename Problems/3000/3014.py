"""Milk"""
P = float(input())
CP = int(input())
S = int(input())
M = float(input())
def milk (p=P,cp=CP,s=S,m=M):
    """milk"""
    n_bot = m//p
    n_cp = n_bot
    if not cp:
        print(f"{n_bot:.0f}")
    else:
        n_total =  0
        n_total += n_bot
        while n_cp >= cp :
            n_newbot = (n_cp//cp)*s
            n_cp -= (n_cp-(n_cp%cp))-n_newbot
            n_total += n_newbot
        print(f"{n_total:.0f}")
milk()
