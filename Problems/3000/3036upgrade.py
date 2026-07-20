"""Castle"""
N = int(input())
def castle(n=N):
    """welcome to my castle"""
    n_sol = 0
    lim_order = 10000000
    out = 0
    for i in range (lim_order):
        n_end = i**2
        n_flo = i
        if n_end >= n:
            break
    lim = n_flo - 1
    #print(lim)
    while lim :
        n_sol += 2
        lim -= 1
    #print(n_sol)
    if not n_flo % 2:
        if not n%2:
            out = n_sol
        else:
            out = n_sol - 1
    else:
        if not n%2:
            out = n_sol - 1
        else:
            out = n_sol
    print(out)
castle()
