"""Reproducible integer checks of the cyclotomic-quotient support-gap law.

No symbolic algebra packages or external services are needed.
"""
from collections import Counter
from math import gcd


def divide_monic(f, g):
    """Exact Z[x] division by a monic integer polynomial, ascending coefficients."""
    h = f[:]
    v = [0] * max(len(f) - len(g) + 1, 0)
    if not g or g[-1] != 1:
        raise ValueError("monic divisor required")
    for i in range(len(v) - 1, -1, -1):
        v[i] = h[i + len(g) - 1]
        if v[i]:
            for j, c in enumerate(g):
                h[i + j] -= v[i] * c
    if any(h):
        raise AssertionError("nonexact polynomial division")
    while len(v) > 1 and not v[-1]:
        v.pop()
    return v


def cyclotomic(n):
    factors = {}
    for k in range(1, n + 1):
        a = [-1] + [0] * (k - 1) + [1]
        for h in range(1, k):
            if k % h == 0:
                a = divide_monic(a, factors[h])
        factors[k] = a
    return factors[n]


def word_data(m, r, f=None):
    f = cyclotomic(m) if f is None else f
    d = len(f) - 1
    numerator = [1] + [0] * (m - 1) + [-1]
    b = divide_monic(numerator, f)  # not monic? exact quotient is monic divisor, fine
    b += [0] * (m - len(b))
    assert len(b) == m
    words = [[sum(f[j] * b[(s + (i-j)*r) % m] for j in range(i+1))
              for s in range(m)] for i in range(d)]
    assert all(any(w) for w in words)
    return f, b, words


def cyc_hist(w):
    p = [j for j, c in enumerate(w) if c]
    assert p
    return Counter((v-u) for u,v in zip(p, p[1:])) + Counter({len(w)+p[0]-p[-1]:1})


def hist(seq):
    p = [i for i, c in enumerate(seq) if c]
    return Counter(v-u for u,v in zip(p, p[1:]))


def quotient_coefficients(m, t, f):
    num = [0]*(t*(len(f)-1)+1)
    for i,c in enumerate(f): num[i*t]=c
    return divide_monic(num,f)


def block_coefficients(m,t,ws):
    d = len(ws);res=[]
    for i,w in enumerate(ws):
        length = t if i<d-1 else t-d+1
        res.extend(w*(length//m)+w[:length%m])
    return res


def check_case(m,r,max_q=3):
    f,b,ws=word_data(m,r)
    d=len(ws)
    slopes=sum((cyc_hist(w) for w in ws),Counter())
    initial=hist(block_coefficients(m,m+r,ws))
    for q in range(1,max_q+1):
        t=m*q+r
        s=block_coefficients(m,t,ws)
        direct=quotient_coefficients(m,t,f)
        assert s==direct, ('coeff',m,r,q)
        h=hist(direct)
        expect={k:initial[k]+(q-1)*slopes[k] for k in set(h)|set(initial)|set(slopes)}
        assert all(h[k] == v for k,v in expect.items()),('hist',m,r,q,h,expect)
        assert sum(k*v for k,v in h.items())==d*(t-1)
        assert max(h)<=d,('bound',m,r,q,max(h),d)
    assert sum(k*v for k,v in slopes.items())==m*d
    return slopes,initial


def run():
    cases=0
    for m in range(2,21):
        for r in range(1,m):
            if gcd(r,m)==1:
                check_case(m,r,4)
                cases += 4
    for m in [21,30,35,45,60,105]:
        for r in [1,m-1,2,7,11]:
            if r<m and gcd(r,m)==1:
                check_case(m,r,3)
                cases += 3
    A_ref={
      1:[10,4,10,2,4,0,4,2],2:[42,16,2,0,0,4,0,2],
      4:[58,12,2,4,0,0,0,2],7:[50,6,14,0,0,0,0,2],
      8:[50,6,14,0,0,0,0,2],11:[58,12,2,4,0,0,0,2],
      13:[42,16,2,0,0,4,0,2],14:[10,4,10,2,4,0,4,2]}
    B_ref={
      1:[0,0,0,0,0,0,0,0],2:[4,2,0,0,0,0,0,0],
      4:[16,4,0,0,0,0,0,0],7:[22,4,6,0,0,0,0,0],
      8:[28,2,8,0,0,0,0,0],11:[42,8,2,4,0,0,0,0],
      13:[38,14,2,0,0,4,0,0],14:[10,4,10,2,4,0,4,0]}
    for r in A_ref:
        slopes, initial=check_case(15,r,6)
        assert [slopes.get(k,0) for k in range(1,9)]==A_ref[r]
        assert [initial.get(k,0)-slopes.get(k,0) for k in range(1,9)]==B_ref[r]
        cases+=6
    print(f"PASS: {cases} independent exact-division quotient instances; all 8 coefficient-gap spectra for m=15 and 6 multipliers each; degree, support, bound and mass checks")

if __name__=='__main__':run()
