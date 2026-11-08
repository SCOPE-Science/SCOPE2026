#!/usr/bin/env python3
"""Finite symbolic checks of universal quadratic half-discriminant identities over F2.

All mathematical identities checked exactly in polynomial rings over F2.
The conceptual proof for arbitrary odd dimension is given separately.
"""
from itertools import combinations

# A polynomial in F2[z0,...] is the set of monomials with coefficient 1.
# Each monomial is a nondecreasing tuple of variable indices, repetitions allowed.
def add(*ps):
    ans = set()
    for p in ps:
        ans.symmetric_difference_update(p)
    return ans

def mul(p, q):
    out = set()
    for a in p:
        for b in q:
            term = tuple(sorted(a + b))
            if term in out: out.remove(term)
            else: out.add(term)
    return out

def deriv(p, j):
    out = set()
    for m in p:
        if m.count(j) % 2:
            t = list(m)
            t.remove(j)
            t = tuple(t)
            if t in out: out.remove(t)
            else: out.add(t)
    return out

def var(i): return {(i,)}

def pfaff(indices, b):
    if not indices: return {()}
    i = indices[0]
    out = set()
    for k in indices[1:]:
        remain = [j for j in indices if j not in (i,k)]
        out = add(out, mul(b[tuple(sorted((i,k)))], pfaff(remain,b)))
    return out

def check(N):
    assert N % 2 == 1 and N >= 3
    pairs = list(combinations(range(N),2))
    a = [var(i) for i in range(N)]
    b = {p:var(N+j) for j,p in enumerate(pairs)}
    w = [pfaff([j for j in range(N) if j !=i], b) for i in range(N)]
    # Universal Pfaffian kernel identities B*w=0.
    for i in range(N):
        assert not add(*(mul(b[tuple(sorted((i,j)))],w[j]) for j in range(N) if j !=i)), ('kernel',N,i)
    Q = add(*(mul(a[i],mul(w[i],w[i])) for i in range(N)),
            *(mul(b[i,j],mul(w[i],w[j])) for i,j in pairs))
    # Complete gradient: derivatives in diagonal and mixed coefficient directions.
    for i in range(N):
        assert deriv(Q,i) == mul(w[i],w[i]), ('diagonal',N,i)
    for j,(i,k) in enumerate(pairs):
        assert deriv(Q,N+j) == mul(w[i],w[k]), ('mixed',N,i,k)
    assert Q
    print('N=%d: kernel %d, gradient %d, terms %d: PASS' % (N,N,N+len(pairs),len(Q)))

if __name__ == '__main__':
    for dim in (3,5,7): check(dim)
    print('ALL_CHECKS_PASSED')
