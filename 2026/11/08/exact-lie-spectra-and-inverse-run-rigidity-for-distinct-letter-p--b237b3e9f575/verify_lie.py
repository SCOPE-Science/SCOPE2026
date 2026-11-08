#!/usr/bin/env python3
"""Independent finite enumeration for the run-period Lie-complexity theorem.

Only Python standard library is required. All word lengths and cyclic rotations
are enumerated directly; the predicted class family is constructed separately.
The finite checks corroborate (but do not replace) the written general proof.
"""
from itertools import product
from random import Random


def necklace(s):
    return min(s[k:] + s[:k] for k in range(len(s)))


def observed_classes(runs, n):
    period = ''.join(chr(65+i)*a for i, a in enumerate(runs))
    m = len(period)
    host = period * (n//m + 3)
    factors = {host[i:i+n] for i in range(m)}
    classes = {necklace(s) for s in factors}
    return {x for x in classes if all(x[j:] + x[:j] in factors for j in range(n))}


def predicted_classes(runs, n):
    q = len(runs)
    period = ''.join(chr(65+i)*a for i, a in enumerate(runs))
    m = len(period)
    out = {chr(65+i)*n for i, a in enumerate(runs) if n<=a}
    if n % m == 0:
        out.add(necklace(period*(n//m)))
    if q == 2 and n < m:
        if n == 2 and min(runs) >= 2:
            out.add('AB')
        if 2 <= n and min(runs)==1:
            if runs[0] == 1:
                out.add(necklace('A'+'B'*(n-1)))
            else:
                out.add(necklace('A'*(n-1)+'B'))
    return out


def formula(runs,n):
    q=len(runs);m=sum(runs)
    count = sum(n<=r for r in runs)+int(n%m==0)
    if q==2:
        count += int(n==2) if min(runs)>=2 else int(2<=n<m)
    return count


def check(runs,n):
    got=observed_classes(runs,n)
    expected=predicted_classes(runs,n)
    assert got==expected,(runs,n,'observed',sorted(got),'expected',sorted(expected))
    assert len(got)==formula(runs,n),(runs,n,len(got),formula(runs,n))


def main():
    cases=0
    for q in range(2,6):
        for runs in product(range(1,5),repeat=q):
            for n in range(1,2*sum(runs)+1):
                check(runs,n)
                cases+=1
    random=Random(20261107)
    random_cases=0
    for q in (6,7):
        for _ in range(100):
            runs=tuple(random.randrange(1,8) for _ in range(q))
            length=sum(runs)
            for n in (1,2,3,length-1,length,length+1,2*length,2*length+1):
                check(runs,n)
                random_cases+=1
    print('PASS: %d exhaustive parameter-length configurations (q=2..5, run lengths=1..4, n=1..2L)'%cases)
    print('PASS: %d reproducible randomized parameter-length configurations (q=6,7)'%random_cases)
    print('PASS: predicted and observed complete conjugacy CLASS SETS match, not merely class counts')
    print('All tests use direct periodic-factor enumeration; infinite claims use the proof.')


if __name__=='__main__':
    main()
