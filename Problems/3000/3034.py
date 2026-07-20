"""Pot"""
pit = input().split(" ")
N = int(pit[0])
K = int(pit[1])
def cal (k=K,n=N):
    """cal_passenger"""
    remain = 0
    n_k = k
    while n :
        r = int(input())
        n_k -= remain
        n_k -= r
        if n_k < 0 :
            remain -= n_k
        elif n_k > 0 :
            remain += n_k
        n_k = k
        n -= 1
    print(remain)
cal()
