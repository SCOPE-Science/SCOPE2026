#!/usr/bin/env python3
"""Independent enumeration of ideals in finite bouquet branch algebras.

This checker enumerates every reduced row-echelon subspace of the radical,
checks invariance under each algebra generator, and compares dimension strata
with a separate Gaussian-binomial inclusion-exclusion formula. No external
libraries are required. Only prime fields are enumerated directly.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def gaussian(n, k, q):
    if not 0 <= k <= n:
        return 0
    num = den = 1
    for j in range(k):
        num *= q**(n-j) - 1
        den *= q**(k-j) - 1
    assert num % den == 0
    return num // den


def no_axis(s, d, q):
    return sum((-1)**j * comb(s,j) * gaussian(s-j,d-j,q)
               for j in range(min(s,d)+1))


def formula(ns, q):
    a = Counter()
    for bs in product(*(range(1,n+1) for n in ns)):
        core_dim = sum(n-b for n,b in zip(ns,bs))
        s = sum(b>=2 for b in bs)
        for d in range(s+1):
            a[core_dim+d] += no_axis(s,d,q)
    a[1+sum(n-1 for n in ns)] += 1
    return a


def rref_subspaces(dim, q):
    for d in range(dim+1):
        for piv in combinations(range(dim),d):
            pivot_set = set(piv)
            free = [(i,j) for i,p in enumerate(piv)
                    for j in range(p+1,dim) if j not in pivot_set]
            for vals in product(range(q),repeat=len(free)):
                rows = [[int(j==p) for j in range(dim)] for p in piv]
                for (i,j),x in zip(free,vals):
                    rows[i][j]=x
                yield tuple(piv),tuple(tuple(row) for row in rows)


def contained(v, piv, rows, q):
    v = list(v)
    for p,row in zip(piv,rows):
        c=v[p]
        if c:
            v=[(x-c*y)%q for x,y in zip(v,row)]
    return not any(v)


def check(ns, q):
    N=sum(n-1 for n in ns)
    shift=[]
    at=0
    for n in ns:
        shift.append({at+j:at+j+1 for j in range(n-2)})
        at+=n-1
    hist=Counter()
    subspaces=0
    for piv,rows in rref_subspaces(N,q):
        subspaces+=1
        valid=True
        for row in rows:
            for sh in shift:
                vec=[0]*N
                for j,k in sh.items():
                    vec[k]=row[j]
                if not contained(vec,piv,rows,q):
                    valid=False
                    break
            if not valid:break
        if valid:hist[len(rows)]+=1
    hist[N+1]+=1  # whole algebra, unique nonproper ideal
    expected=formula(ns,q)
    assert hist==expected,(ns,q,dict(hist),dict(expected))
    print(f'PASS ns={ns} q={q} radical_subspaces={subspaces} ideals={sum(hist.values())} dimension_counts={dict(sorted(hist.items()))}')


def main():
    for ns,q in [((2,2,2),2),((3,3,3),2),((3,3,3),3),
                 ((3,4),2),((2,3,3),2),((2,2,2,2),2),
                 ((2,2,2,2),3),((2,4),3)]:
        check(ns,q)
    print('BOUQUET_IDEALS_INDEPENDENT_RREF_ENUMERATION_PASS')

if __name__=='__main__':
    main()
