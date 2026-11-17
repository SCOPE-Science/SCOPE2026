#!/usr/bin/env python3
"""Independent finite checks of rooted-star confluence orbit formula.

Run: python3 checker.py.  All assertions are exact.  The finite checks
supplement rather than replace the arbitrary-size combinatorial proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial, gcd, prod


def partitions(n, lower=1):
    if not n:
        yield ()
    for a in range(lower, n+1):
        for q in partitions(n-a, a):
            yield (a,)+q


def z(lam):
    return prod(a**b*factorial(b) for a,b in Counter(lam).items())


def fixed_formula(lam):
    k=len(lam)
    g=[sum(gcd(a,b) for b in lam) for a in lam]
    return (2**k + prod(2**(1+t)-1 for t in g)
            + 2**k*(prod(1+2**t for t in g)-2**sum(g)))


def orbit_formula(m):
    s=sum((Fraction(fixed_formula(lam),z(lam)) for lam in partitions(m)),Fraction())
    assert s.denominator == 1
    return s.numerator


def row_transform(rows, p):
    # p[0] = 0, p[1:] is a permutation of the leaves.
    ret=[0]*len(p)
    for source, row in enumerate(rows):
        ret[p[source]]=sum(1<<p[target] for target in range(len(p)) if row>>target&1)
    return tuple(ret)


def cycle_type(p):
    visited=set(); lengths=[]
    for start in range(1,len(p)):
        if start not in visited:
            j=start;c=0
            while j not in visited:
                visited.add(j);c+=1;j=p[j]
            lengths.append(c)
    return tuple(sorted(lengths))


def confluence_direct(rows):
    n=len(rows)
    # Universal relation witnesses, not any closed formula.
    below=[1]+[1|(1<<i) for i in range(1,n)]
    above=[(1<<n)-1]+[1<<i for i in range(1,n)]
    for a in range(n):
        for b in range(n):
            if not (above[a]>>b&1):
                continue
            for u in range(n):
                if rows[a]>>u&1 and not any(
                    rows[b]>>v&1 and above[u]>>v&1 for v in range(n)
                ): return False
                if rows[b]>>u&1 and not any(
                    rows[a]>>v&1 and below[u]>>v&1 for v in range(n)
                ): return False
    return True


def modalities_agree(rows):
    n=len(rows);top=(1<<n)-1
    below=[1]+[1|(1<<i) for i in range(1,n)]
    above=[top]+[1<<i for i in range(1,n)]
    upsets=[u for u in range(1<<n) if not(u&1) or u==top]
    for u in upsets:
        hits=[bool(row&u) for row in rows]
        inside=[(row&~u)==0 for row in rows]
        for a in range(n):
            lo=[b for b in range(n) if below[a]>>b&1]
            hi=[b for b in range(n) if above[a]>>b&1]
            possibility_P=any(hits[b] for b in lo)
            possibility_W=all(hits[b] for b in hi)
            necessity_F=all(inside[b] for b in hi)
            necessity_D=any(inside[b] for b in lo)
            if possibility_P!=possibility_W or necessity_F!=necessity_D:
                return False
    return True


def brute(m):
    n=m+1
    pset=[(0,)+p for p in permutations(range(1,n))]
    totals=0;reps=set();fixed=Counter()
    for rows in product(range(1<<n),repeat=n):
        good=confluence_direct(rows)
        assert good==modalities_agree(rows), ('modal mismatch',rows)
        if not good:
            continue
        totals+=1
        transformed=[row_transform(rows,p) for p in pset]
        reps.add(min(transformed))
        for p,r2 in zip(pset,transformed):
            if r2==rows: fixed[cycle_type(p)]+=1
    for p in pset:
        lam=cycle_type(p)
        assert fixed[lam] % (factorial(m)//z(lam))==0
        assert fixed[lam]//(factorial(m)//z(lam))==fixed_formula(lam)
    assert totals==fixed_formula((1,)*m)
    assert len(reps)==orbit_formula(m)
    return totals,len(reps)


def main():
    counts=[7,50,940,53170,9968880,6472894706,
            14750019886992,119118310350433826]
    for m, count in enumerate(counts,1):
        assert orbit_formula(m)==count
    for m in (1,2,3):
        a,b=brute(m)
        print('BRUTE',m,'labelled',a,'orbits',b)
    print('ROOTED_STAR_CONFLUENCE_ORBIT_OK')

if __name__=='__main__':main()
