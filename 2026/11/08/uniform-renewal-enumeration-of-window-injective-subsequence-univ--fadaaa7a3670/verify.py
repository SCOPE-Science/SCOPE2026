"""Finite exact checks for window-injective subsequence-universality formulas.

Run with Python 3, standard library only: python verify.py
Finite checks are not a proof for all alphabet sizes and lengths.
"""
from collections import defaultdict
from itertools import product
from math import factorial


def scalar_product(a, b, N):
    out = [0] * (N + 1)
    for i, x in enumerate(a[:N+1]):
        if x:
            for j, y in enumerate(b[:N+1-i]):
                if y:
                    out[i+j] += x*y
    return out


def shift_scale(a, scale, shift, N):
    out = [0] * (N + 1)
    for i in range(N+1-shift):
        out[i+shift] = a[i]*scale
    return out


def generating_coefficients(q, d, N):
    """Evaluate explicit rational series via formal power-series operations."""
    r = q-d
    reachable = [1] + [0]*N
    incomplete = [0]*(N+1)
    for j in range(r):
        residence = [0]*(N+1)
        for n in range(N+1):
            residence[n] = reachable[n] + (j*residence[n-1] if n else 0)
            incomplete[n] += residence[n]
        reachable = shift_scale(residence, r-j, 1, N)
    complete = reachable
    short = [r**j if j < d else 0 for j in range(N+1)]
    post = scalar_product(complete, short, N)
    renew = shift_scale(complete, r**d, d, N)
    g = {0: incomplete}
    max_arches = N//q
    for k in range(1, max_arches+1):
        p = scalar_product(renew, g[k-1], N)
        if k == 1:
            p = [p[n]+post[n] for n in range(N+1)]
        g[k] = p
    result = defaultdict(int)
    fall = 1
    for n in range(d):
        if n:
            fall *= q-n+1
        result[n,0] += fall
    fall *= q-d+1 if d else 1
    # fall now (q)_d
    for k, series in g.items():
        for n in range(d,N+1):
            result[n,k] += fall*series[n-d]
    return dict(result)


def state_coefficients(q, d, N):
    """Independent weighted transition enumeration with explicit arch states."""
    dp = {('init',0,0):1}
    out = defaultdict(int)
    for n in range(N+1):
        nxt = defaultdict(int)
        for (phase, s, k), weight in dp.items():
            out[n,k] += weight
            if n == N:
                continue
            if phase == 'init':
                nxt[('arch' if s+1 == d else 'init',s+1,k)] += weight*(q-s)
            elif phase == 'arch':
                if s > d:
                    nxt[('arch',s,k)] += weight*(s-d)
                if s+1 == q:
                    nxt[('restart',0,k+1)] += weight*(q-s)
                else:
                    nxt[('arch',s+1,k)] += weight*(q-s)
            else:
                nxt[('arch' if s+1 == d else 'restart',s+1 if s+1 < d else d,k)] += weight*(q-d)
        dp = nxt
    return dict(out)


def enumerate_literal(q, d, N):
    counts = defaultdict(int)
    for n in range(N+1):
        for w in product(range(q), repeat=n):
            if any(w[i] in w[max(0,i-d):i] for i in range(n)):
                continue
            seen = set()
            arches = 0
            for c in w:
                seen.add(c)
                if len(seen) == q:
                    arches += 1
                    seen.clear()
            counts[n,arches] += 1
    return dict(counts)


def canonical(a):
    return {key:value for key,value in a.items() if value}


def main():
    dp_cells = 0
    for q in range(3,9):
        for d in range(2,q):
            N = 32
            A = canonical(generating_coefficients(q,d,N))
            B = canonical(state_coefficients(q,d,N))
            assert A == B, ('rational/state mismatch',q,d,{x:(A.get(x),B.get(x)) for x in A.keys()|B.keys() if A.get(x)!=B.get(x)})
            dp_cells += len(A)
            for k in range(1,N//q+1):
                assert A[q*k,k] == factorial(q)*((q-d)**d*factorial(q-d))**(k-1), (q,d,k)
            assert all(A.get((n,k),0) == (factorial(q) if n>=q-1 else (factorial(q)//factorial(q-n))) if k==n//q else A.get((n,k),0)==0 for n in range(0,N+1) for k in range(0,N//q+2)) if q==d+1 else True
    brute_cases=[(3,2,10),(4,2,9),(4,3,9),(5,2,8),(5,3,8),(5,4,8),(6,3,7)]
    tested_words = 0
    for q,d,N in brute_cases:
        exact = enumerate_literal(q,d,N)
        calc = canonical(generating_coefficients(q,d,N))
        assert exact == calc, ('literal/formula mismatch',q,d,exact,calc)
        tested_words += sum(exact.values())
    C = canonical(generating_coefficients(4,2,60))
    numerator = {(0,0):1,(1,0):3,(2,0):8,(3,0):12,(4,1):16,(5,1):16}
    for n in range(61):
        for k in range(n//4+1):
            right = (C.get((n-1,k),0) if n>=1 else 0) + (8*C.get((n-4,k-1),0) if n>=4 and k>=1 else 0)+numerator.get((n,k),0)
            assert C.get((n,k),0)==right,(n,k,C.get((n,k),0),right)
    print('VERIFY_OK q=3..8 d=2..q-1 n<=32 finite_cells=%d literal_instances=%d quaternary_identity_n<=60' % (dp_cells,tested_words))

if __name__ == '__main__':
    main()
