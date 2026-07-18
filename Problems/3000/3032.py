"""Top Test"""
def who ():
    """who is The top"""
    n = int(input())
    all_score = []
    while n  :
        score = int(input())
        all_score.append(score)
        n -= 1
    m_score = max(all_score)
    n_m = all_score.count(m_score)
    print(m_score)
    print(n_m)
who()
