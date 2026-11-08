#!/usr/bin/env python3
"""Standalone finite verification for reverse-complement subsequence enumerator.
Uses only Python's standard library. Not a proof of the infinite theorem.
"""
from itertools import product
from math import comb


def poly_add(a, b):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) +
             (b[i] if i < len(b) else 0)) for i in range(n)]


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def generating_polynomials(m, kmax):
    # R=(1+t-t*z^2)^m, polynomial coefficient R_j(t).
    r = {}
    for j in range(m+1):
        # coefficient of z^(2j): (-1)^j binom(m,j) t^j (1+t)^(m-j)
        r[2*j] = [0]*j + [(-1)**j * comb(m,j) * comb(m-j, s)
                          for s in range(m-j+1)]
    # H=(R-1)/(1-zR) and F=z H/(1-z).
    h = []
    for degree in range(kmax):
        numerator = r.get(degree, [0])[:]
        if degree == 0:
            numerator[0] -= 1
        for j in range(degree):
            numerator = poly_add(numerator, poly_mul(r.get(j, [0]), h[degree-1-j]))
        h.append(numerator)
    result = []
    cumulative = [0]
    for x in h:
        cumulative = poly_add(cumulative, x)
        result.append(cumulative)
    return result


def brute_histogram(m,k):
    q=2*m
    w=list(range(q))*k
    n=len(w)
    out=set()
    for mask in range(1, 1<<n):
        if mask.bit_count() % 2:
            continue
        u=tuple(w[i] for i in range(n) if mask & (1<<i))
        if all(u[i] + u[-1-i] == q-1 for i in range(len(u)//2)):
            out.add(u)
    counts={}
    for u in out:
        h=len(u)//2
        counts[h]=counts.get(h,0)+1
    return counts


def weak_descent_cost(seq):
    return sum(seq[i] >= seq[i+1] for i in range(len(seq)-1))


def check_greedy(m,k):
    q=2*m
    w=list(range(q))*k
    # All shorter words tested by choosing all index subsets, confirming cost bound.
    for mask in range(1, 1<<len(w)):
        if mask.bit_count() > 8: continue
        u=tuple(w[i] for i in range(len(w)) if mask & (1<<i))
        d=weak_descent_cost(u)
        assert d <= k-1
    return True


def verify_half_spectrum():
    total=0
    for q,max_n in ((2,6),(4,4)):
        for n in range(1,max_n+1):
            for a in product(range(q), repeat=n):
                w=a+tuple(q-1-i for i in a[::-1])
                direct=set()
                for mask in range(1,1<<(2*n)):
                    if mask.bit_count()%2: continue
                    u=tuple(w[i] for i in range(2*n) if mask>>i&1)
                    if all(u[i]+u[-1-i]==q-1 for i in range(len(u)//2)):
                        direct.add(u)
                expected=set()
                for mask in range(1,1<<n):
                    v=tuple(a[i] for i in range(n) if mask>>i&1)
                    expected.add(v+tuple(q-1-i for i in v[::-1]))
                assert direct==expected,(q,n,a)
                total+=1
    return total


def main():
    confs=0
    tested_masks=0
    for m,kmax in ((1,9),(2,4),(3,3),(4,2)):
        polys=generating_polynomials(m,kmax)
        for k in range(1,kmax+1):
            expected={h:x for h,x in enumerate(polys[k-1]) if h>0 and x}
            got=brute_histogram(m,k)
            assert expected==got,(m,k,expected,got)
            confs+=1
            tested_masks+=(1<<(2*m*k))-1
            print(f'm={m}, k={k}, length={2*m*k}, distinct={sum(got.values())}, histogram={sorted(got.items())}')
    for m,k in ((1,5),(2,3),(3,2)):
        check_greedy(m,k)
    universal=verify_half_spectrum()
    print(f'VERIFY_OK configurations={confs} masks={tested_masks} symmetric_hosts={universal} tests=histogram_greedy_half_spectrum')

if __name__=='__main__':
    main()
