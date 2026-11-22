"""Finite-state checks for marker-cycle overlap theorem.

The infinite theorem is proved analytically in RESULT.md; this program
checks the finite symbolic overlap mechanism used by that proof.
"""
from collections import defaultdict
from fractions import Fraction

def block(m,phase,n):
    return tuple(int((phase+j) % m == 0) for j in range(n))

def formula(w):
    n=len(w)
    marks=[i for i,a in enumerate(w) if a]
    if not marks: return 1
    if len(marks)==1:
        i=marks[0]
        return max(i+1,n-i)
    return marks[1]-marks[0]

def verify(M,n):
    cells=defaultdict(set)
    for m in range(1,M+1):
        for phase in range(m):
            cells[block(m,phase,n)].add((m,phase))
    for w,points in cells.items():
        real=next(k for k in range(1,n+2) if any((m,(phase+k)%m) in points for m,phase in points))
        predicted=formula(w)
        assert real==predicted,(M,n,w,real,predicted)
        assert predicted<=n
        for m,phase in points:
            if n>=2*m:
                assert points=={(m,phase)}
                assert predicted==m
    for s in (2,3,4):
        Z=sum((Fraction(1,m**s) for m in range(1,M+1)),Fraction(0))
        for k in (0,1,2,3):
            direct=sum((formula(w)**k * sum((Fraction(1,m**(s+1)) for m,phase in pts),Fraction(0)) for w,pts in cells.items()),Fraction(0))/Z
            zero=sum((Fraction(m-n,m**(s+1)) for m in range(n+1,M+1)),Fraction(0))
            singles=sum((max(i+1,n-i)**k * sum((Fraction(1,m**(s+1)) for m in range(max(i+1,n-i),M+1)),Fraction(0)) for i in range(n)),Fraction(0))
            multis=sum((Fraction(min(m,n-m)*m**k,m**(s+1)) for m in range(1,min(n,M+1))),Fraction(0))
            predicted=(zero+singles+multis)/Z
            assert direct==predicted,(M,n,s,k,direct,predicted)
    return len(cells)

if __name__=='__main__':
    checks=0
    for M in (16,22,29):
        for n in range(1,min(13,M-2)+1):
            checks+=verify(M,n)
    print('PASS: all exact overlap predictions, admissibility and singleton thresholds')
    print('Distinct word-atom checks:',checks)
    print('Exact rational moment-identity checks:', 3*13*3*4)
