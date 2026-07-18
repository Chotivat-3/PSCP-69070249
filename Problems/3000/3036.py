"""Castle"""
fl_1 = [1]
fl_2 = [2,3,4]
fl_3 = [5,6,7,8,9]
fl_4 = [10,11,12,13,14,15,16]
fl_5 = [17,18,19,20,21,22,23,24,25]
N = int(input())
def flo_2 (n=N):
    """Floor_2"""
    if n%2 :
        print(1)
    else:
        print(2)
def flo_3 (n=N):
    """Floor_3"""
    if not n%2 :
        print(3)
    else:
        print(4)
def flo_4 (n=N):
    """Floor_4"""
    if n%2 :
        print(5)
    else :
        print(6)
def flo_5 (n=N):
    if not n%2 :
        print(7)
    else :
        print(8)
def main (n=N):
    if n in fl_1:
        print(0)