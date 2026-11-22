"""Self-contained numerical diagnostics for the q-Ricker interval theorem.

All infinite-time and all-parameter statements require the mathematical proof;
finite numerical checks below are diagnostic, not certificates of those statements.
Run: python3 verify.py
"""
import math


def G(t, a, k):
    z = math.exp(-t)
    return a*t*z/(1-k*t*z)


def bisect_root(fun, left, right, iters=130):
    fleft, fright = fun(left), fun(right)
    assert fleft * fright < 0
    for _ in range(iters):
        middle = (left+right)/2
        fm = fun(middle)
        if fm == 0:
            return middle
        if fm * fleft > 0:
            left, fleft = middle, fm
        else:
            right = middle
    return (left+right)/2


def roots(a, k):
    c = math.log(k)
    def f(t): return math.exp(t)-k*t-a
    return bisect_root(f, 0, c), bisect_root(f, c, 1)


def preimage(t, a, k):
    b = 1.5
    while G(b, a, k) > t:
        b *= 2
    return bisect_root(lambda q: G(q,a,k)-t, 1, b)


def iterate(t, a, k, n):
    for _ in range(n): t = G(t, a, k)
    return t


def close(a, b, tol=1e-10):
    assert abs(a-b) < tol * (1 + abs(a)+abs(b)), (a,b)


def main():
    k = 1.5
    c = math.log(k)
    ac = k*(1-c)
    assert 1 < k < math.e and ac < 1 and ac < math.e-k
    # Exact analytic identities are proved in RESULT.md; these are spot checks.
    for s in [0.01, 0.05, 0.3, c, 0.75, 1, 1.5, 3.0, 6.0]:
        aa = ac + 0.02
        R = aa*math.exp(-s)/(1-k*s*math.exp(-s))
        close(G(s, aa, k), s*R)
        assert G(s,aa,k) >=0
    for a in [ac-0.02, ac, ac+0.02]:
        mx = a/(math.e-k)
        assert mx < 1
        assert all(0 <= G(t,a,k) <= mx+1e-14 for t in [0,0.01,0.1,0.4,0.8,1,2,4,9,50])
    # Subcritical all-orbit extinction, including very high initial abundance.
    for t in [0.001,0.1,c,0.7,1.0,3.0,1e3]:
        assert iterate(t,ac-0.02,k,300) < 1e-5
    # At fold: preimage, invariant endpoint, interior parabolic law.
    bc = preimage(c,ac,k)
    close(G(c,ac,k),c)
    close(G(bc,ac,k),c)
    assert bc > 1
    for t in [c+0.005, (c+1)/2,1.0,(bc+1)/2,bc-0.01]:
        for n in [30000,120000]:
            tn = iterate(t,ac,k,n)
            assert c < tn < c+0.01
            assert abs(n*(tn-c)-2*(1-c)/c) < 0.14
    assert iterate(c-0.01,ac,k,1000) < 1e-5
    assert iterate(bc+0.01,ac,k,1000) < 1e-5
    # Supercritical exact basin boundary and interior attractor.
    aa = ac+0.02
    lo,hi = roots(aa,k)
    bb = preimage(lo,aa,k)
    assert 0 < lo < c < hi < 1 < bb
    close(G(lo,aa,k),lo)
    close(G(hi,aa,k),hi)
    close(G(bb,aa,k),lo)
    for t in [lo+0.005,(lo+hi)/2,hi,(hi+bb)/2,bb-0.01]:
        close(iterate(t,aa,k,250),hi,1e-9)
    for t in [0.001,lo-0.005,bb+0.005,2*bb,100]:
        assert iterate(t,aa,k,250) < 1e-6
    # Fold square-root basin-width coefficient.
    coefficient = (bc-c)/(c*(bc-1))*math.sqrt(2/k)
    for d in [1e-5,1e-6]:
        ll, _ = roots(ac+d,k)
        rr = preimage(ll,ac+d,k)
        approximate = (bc-c)+coefficient*math.sqrt(d)
        assert abs((rr-ll)-approximate) < 40*d
    print('PASS: normalized map, three global regimes, parabolic law, fold-width law diagnostics')
    print('fold, critical preimage:',ac,bc)
    print('supercritical roots and preimage:',lo,hi,bb)

if __name__ == '__main__':
    main()
