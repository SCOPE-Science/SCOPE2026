"""Separate finite checks for the exact-three-substitution sphere theorem.
Run: python verify.py. Python standard library only.
"""
from itertools import product
from math import comb, factorial


def closed(n, q, d):
    assert n >= 6 and q >= 3 and 1 <= d <= 6
    return {
        1: (n-2)*(n-1)*(q-2)*(q-1)**2 // 2,
        2: (n-2)*(q-1)*(n*(q-1)+q*q-7*q+7),
        3: (q-2)*(6*n*(q-1)+q*q-22*q+22),
        4: 6*(n*(q-1)+2*q*q-12*q+12),
        5: 30*(q-2),
        6: 20,
    }[d]


def coefficient(n, q, d):
    # Directly from the three types of differing-coordinate outputs.
    total = 0
    for c in range(4):
        a = d-3+c
        b = 6-2*c-d
        if min(a, b) < 0 or c > n-d or 2*a+b != d:
            continue
        ways = factorial(d)//(factorial(a)**2 * factorial(b))
        total += comb(n-d,c)*(q-1)**c * ways*(q-2)**b
    return total


def positivity(n, q):
    r, s = q-3, n-6
    a = 4+4*r+r*r
    upper = {
        3: ((18,15,5,1), (19,11,7,3)),
        4: ((18,27,11,1), (20,32,16,4)),
        5: ((30,33,11,1), (26,38,28,4)),
        6: ((30,33,11,1), (36,68,28,4)),
    }
    def poly4(c):return sum(v*r**i for i,v in enumerate(c))
    for d, (lin, const) in upper.items():
        gap = a*s*s + poly4(lin)*s + poly4(const)
        assert closed(n,q,2)-closed(n,q,d) == gap
        assert gap > 0
    if q == 3:
        assert closed(n,q,2)-closed(n,q,1) == 2*(n-2)*(n-4)
    else:
        assert 2*(closed(n,q,1)-closed(n,q,2)) == (n-2)*(q-1)*((n-6)*(q-1)*(q-4)+3*q*q-13*q+8)


def brute(n, q):
    center=(0,)*n
    scores=[0]*7
    for z in product(range(q),repeat=n):
        if sum(z_i!=0 for z_i in z)!=3:continue
        for d in range(1,7):
            if sum(z[i]!=(1 if i<d else 0) for i in range(n)) == 3:
                scores[d]+=1
    for d in range(1,7):
        assert scores[d] == closed(n,q,d), (n,q,d,scores[d],closed(n,q,d))
    return scores[1:]


def run():
    for n in range(6,31):
        for q in range(3,15):
            positivity(n,q)
            for d in range(1,7):
                assert closed(n,q,d) == coefficient(n,q,d)
                best = 2 if q==3 else 1
                assert closed(n,q,best)>closed(n,q,d) or d==best
    cases = ((6,3),(7,3),(6,4),(6,5))
    for n,q in cases:
        scores=brute(n,q)
        print('n=%d q=%d intersection_by_distance=%s' % (n,q,scores))
    print('PASS: algebra, positivity, optimizer uniqueness, and direct word enumeration')

if __name__=='__main__':run()
