"""Exact checks for the open equal-bond antiferromagnetic delta chain.

Run with Python 3 (standard library only). This script checks finite instances;
the all-size statements require the combinatorial proof in RESULT.md.
"""
from itertools import product
from fractions import Fraction


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def proposed(m, x):
    """Return (twice energy/J, degeneracy) for rational x=h/J."""
    x = Fraction(x)
    n = 2 * m + 1
    if x == 0:
        return 2 * (-m), 2 * 3**m
    if x >= 4:
        return 2 * (3*m - x*n), fibonacci(m+1) if x == 4 else 1
    if m % 2 == 0:
        return 2 * (-m - x * (m+1)), 1
    if x < 2:
        return 2 * (-m - x * m), m+2
    if x == 2:
        return 2 * (-m - 2*m), (3*m+5)//2
    return 2 * (4-m - x*(m+2)), (m+1)//2


def transfer_dp(m, x):
    """Independent two-state exact energy and count transfer."""
    x = Fraction(x)
    d = {s: (-x*s, 1) for s in (-1, 1)}
    for _ in range(m):
        nxt = {}
        for s, (e0, count) in d.items():
            for t, w in product((-1,1), repeat=2):
                e = e0 + s*t+s*w+t*w-x*(t+w)
                if t not in nxt or e < nxt[t][0]:
                    nxt[t] = (e, count)
                elif e == nxt[t][0]:
                    nxt[t] = (e, nxt[t][1]+count)
        d = nxt
    ground = min(e for e, c in d.values())
    return 2*ground, sum(c for e,c in d.values() if e == ground)


def direct_enumeration(m, x):
    x = Fraction(x)
    n = 2*m+1
    edges = [(i, i+1) for i in range(m)]
    for i in range(m):
        edges += [(i,m+1+i),(i+1,m+1+i)]
    best = None; cnt = 0
    for spins in product((-1,1), repeat=n):
        en = sum(spins[a]*spins[b] for a,b in edges)-x*sum(spins)
        if best is None or en < best: best, cnt = en, 1
        elif en == best: cnt += 1
    return 2*best, cnt


def main():
    xs = [Fraction(j,2) for j in range(11)]
    nchecks = 0
    for m in range(2, 46):
        for x in xs:
            assert proposed(m,x) == transfer_dp(m,x), (m,x,'transfer')
            nchecks += 1
    for m in range(2,8):
        for x in xs:
            assert proposed(m,x) == direct_enumeration(m,x), (m,x,'direct')
            nchecks += 1
    # Check exact weighted base-string minimizer coefficients independently.
    for L in range(3,75):
        for weight in (1,2):
            p0,p1 = {0:1},{1:1}
            for _ in range(1,L):
                n0={};n1={}
                for k,c in p0.items(): n0[k+1]=n0.get(k+1,0)+weight*c
                for k,c in p1.items(): n0[k]=n0.get(k,0)+c
                for pol in (p0,p1):
                    for k,c in pol.items(): n1[k+1]=n1.get(k+1,0)+c
                p0,p1=n0,n1
            exponent=min(min(p0),min(p1))
            lead=p0.get(exponent,0)+p1.get(exponent,0)
            expected=1 if L%2 else ((L+1) if weight==1 else (3*L//2+1))
            assert exponent==L//2 and lead==expected, (L,weight,exponent,lead,expected)
            nchecks += 1
    print('OPEN_DELTA_EXACT_CHECKS_PASSED',nchecks)


if __name__=='__main__':
    main()
