#!/usr/bin/env python3
"""Direct substitution checks for free generalized dimonoids.

Elements are (nonempty tuple of generator indices, control word a/b of length one less).
This program enumerates maps of free generators, composes them using the two actual
binary operations, and counts idempotent maps without using the classification theorem.
"""
from itertools import product
from math import comb

def elements(k, L):
    for m in range(1, L + 1):
        for letters in product(range(k), repeat=m):
            for ops in product('ab', repeat=m-1):
                yield (letters, ''.join(ops))

def left(a, b):
    return (a[0] + b[0], a[1] + 'a' * len(b[0]))

def right(a, b):
    return (a[0] + b[0], b[1] + 'b' * len(a[0]))

def apply(subst, e):
    w, u = e
    if len(w) == 1:
        return subst[w[0]]
    if u[-1] == 'a':
        return left(apply(subst, (w[:-1], u[:-1])), subst[w[-1]])
    return right(subst[w[0]], apply(subst, (w[1:], u[:-1])))

def expected(k, L):
    return {s: comb(k,s) * (sum(s**m*2**(m-1) for m in range(1,L+1)))**(k-s)
            for s in range(1,k+1)}

def run(k,L):
    im=list(elements(k,L))
    identity=tuple(((i,), '') for i in range(k))
    for e in im:
        assert apply(identity,e) == e, (k,L,e)
    from collections import Counter
    result=Counter()
    for subst in product(im, repeat=k):
        if all(apply(subst, subst[x]) == subst[x] for x in range(k)):
            support=sum(subst[x] == ((x,), '') for x in range(k))
            result[support]+=1
    exact=expected(k,L)
    assert all(result[s] == exact[s] for s in range(1,k+1)), (k,L,result,exact)
    assert not result[0]
    assert sum(result.values())==sum(exact.values())
    print(f'PASS k={k} L={L} maps={len(im)**k} fixed_support_counts={dict(sorted(result.items()))} total={sum(result.values())}')

if __name__ == '__main__':
    for k,L in [(1,4),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1)]:
        run(k,L)
    for k in range(2,21):
        bases=[(2*s)**(k-s) for s in range(1,k)]
        assert max(bases) < (2*k)**k
    print('VERIFY_OK')
