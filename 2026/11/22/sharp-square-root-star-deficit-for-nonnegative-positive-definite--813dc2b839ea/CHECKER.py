"""Exact finite checks for the even-level Krawtchouk star construction.

Uses only Python's standard library. These tests support the analytic proof;
they do not replace its all-dimension asymptotic estimates.
"""
from fractions import Fraction
from math import comb


def parameters(d):
    assert d >= 49
    # unique X congruent to d (mod 4) in [sqrt(d)-6, sqrt(d)-2)
    candidates = [x for x in range(d + 1) if (x - d) % 4 == 0
                  and (x + 6)**2 >= d and (x + 2)**2 < d]
    # for square-end cases the strict right bound can miss X when X+2=sqrt(d)
    if not candidates:
        import math
        candidates = [x for x in range(d + 1) if (x - d) % 4 == 0
                      and math.sqrt(d) - 6 <= x < math.sqrt(d) - 2]
    assert len(candidates) == 1, (d, candidates)
    x = candidates[0]
    r = (d - x)//2
    assert r % 2 == 0 and 0 < r < d
    return x, r


def kappa(d, r, v):
    lo = max(0, v - (d-r))
    hi = min(v, r)
    return Fraction(sum((-1)**j * comb(r,j) * comb(d-r,v-j)
                        for j in range(lo,hi+1)), comb(d,v))


def verify(d):
    x,r=parameters(d)
    vals=[kappa(d,r,v) for v in range(d+1)]
    k2=Fraction(x*x-d,d*(d-1))
    eps=-k2/(1-k2)
    assert 0<eps<1
    assert vals[0] == 1
    assert vals[1] == Fraction(x,d)
    assert vals[2] == k2
    assert vals[3] == Fraction(x*(x*x-3*d+2), d*(d-1)*(d-2))
    assert vals == vals[::-1]
    assert all(v >= k2 for v in vals), (d, min(vals),k2)
    assert sum(comb(d,v)*a*a for v,a in enumerate(vals))==Fraction(2**d,comb(d,r))
    p1=eps+(1-eps)*vals[1]
    p2=eps+(1-eps)*vals[2]
    assert p1 == Fraction(x+1,d+x)
    assert p2 == 0
    q = d+1-2*d*p1
    return x,r,float(q),float((d+1-q)/d**0.5)

if __name__=='__main__':
    ds=[64,81,100,121,144,169,196,225,256,289,324,400]
    for d in ds:
        print('d=%d X=%d r=%d Q=%.9f normalized_deficit=%.8f'%((d,)+verify(d)))
    print('PASS: exact formulas, symmetry, every Boolean vertex, Parseval identity, and star values')
