"""Independent exact six-mask census by quadratic characters and Pfaffians.

Run with standard Python 3: python paley20_pfaffian.py
"""
from collections import Counter
from itertools import combinations
from math import comb

EXPECTED = {(0,1):1140, (3,9):6840, (4,1):13680,
            (5,25):6840, (6,49):7980, (6,81):2280}


def run():
    p = 19
    squares = {x*x % p for x in range(1,p)}
    s = [[0]*(p+1) for _ in range(p+1)]
    for j in range(1,p+1):
        s[0][j] = 1
        s[j][0] = -1
    for i in range(1,p+1):
        for j in range(i+1,p+1):
            s[i][j] = 1 if ((i-j) % p) in squares else -1
            s[j][i] = -s[i][j]
    pf4 = {}
    for a,b,c,d in combinations(range(20),4):
        pf4[a,b,c,d] = (s[a][b]*s[c][d] - s[a][c]*s[b][d]
                        + s[a][d]*s[b][c])
    hist = Counter()
    for six in combinations(range(20),6):
        k = sum(pf4[four]**2 == 9 for four in combinations(six,4))
        a = six[0]
        tail = six[1:]
        pf6 = sum((-1)**j * s[a][v] * pf4[tail[:j]+tail[j+1:]]
                  for j,v in enumerate(tail))
        hist[k,pf6*pf6] += 1
    assert hist == EXPECTED, hist
    assert sum(hist.values()) == comb(20,6)
    for label, num in sorted(hist.items()):
        print(label, num)
    print('PASS: 38760 masks, exact Pfaffian census.')


if __name__=='__main__':
    run()
