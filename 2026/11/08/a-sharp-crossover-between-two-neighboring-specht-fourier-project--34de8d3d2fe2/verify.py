#!/usr/bin/env python3
"""Exact finite arithmetic for two natural symmetric-group Fourier blocks.
Run: python3 verify.py (from the directory with finite_certificate.tsv).
Only Python 3 standard library is required.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import permutations
from pathlib import Path

LIMIT=32
q=[Q(0)]*(LIMIT+1)
q[0]=Q(1)
for r in range(1,LIMIT+1):
    q[r]=sum((q[r-j] for j in range(3,r+1)), Q(0))/r
# Second calculation from the exact no-1/no-2-cycle inclusion-exclusion EGF.
for r in range(LIMIT+1):
    alt=sum((Q((-1)**(a+b),factorial(a)*2**b*factorial(b))
             for a in range(r+1) for b in range((r-a)//2+1)),Q(0))
    assert alt==q[r], ('cycle_EGF',r)

def chars(k,m):
    return Q((k-1)*(k-2),2)-m, Q(k*(k-1),2)+m-k

def averages(n):
    h=t=h2=t2=Q(0)
    for k in range(n+1):
        for m in range((n-k)//2+1):
            w=q[n-k-2*m]/(factorial(k)*2**m*factorial(m))
            a,b=chars(k,m)
            h+=w*abs(a); t+=w*abs(b)
            h2+=w*a*a; t2+=w*b*b
    assert h2==t2==1, ('irreducible_orthogonality',n)
    return h,t

def gap(n):
    h,t=averages(n)
    return Q(n*(n-3),2)*t-Q((n-1)*(n-2),2)*h

lines=Path(__file__).with_name('finite_certificate.tsv').read_text(encoding='utf-8').strip().splitlines()
assert lines[0]=='n\tweighted_gap_exact' and len(lines)==27
for n,line in enumerate(lines[1:],4):
    a,v=line.split('\t')
    assert int(a)==n
    val=gap(n)
    assert val==Q(v), ('certificate',n,val,v)
    assert (val>0)==(n==5 or n>=8),('phase',n,val)
print('EXACT_FINITE_PHASE_CERTIFICATE_PASSED',len(lines)-1)

# An entirely different check counts each actual permutation for n=4..8.
for n in range(4,9):
    aa=bb=0
    for perm in permutations(range(n)):
        seen=set()
        k=m=0
        for i in range(n):
            if i in seen: continue
            j=i; le=0
            while j not in seen:
                seen.add(j)
                j=perm[j]
                le+=1
            k+=(le==1);m+=(le==2)
        x,y=chars(k,m)
        aa+=abs(x);bb+=abs(y)
    h,t=averages(n)
    assert (Q(aa,factorial(n)),Q(bb,factorial(n)))==(h,t)
print('DIRECT_PERMUTATION_CHARACTER_AVERAGES_PASSED',sum(factorial(i) for i in range(4,9)))

# The same moment computation at n=30 is an exact rational witness.
h,t=averages(30)
d=t-h
C=60011
assert Q(68,25)**8<3000  # strict analytic bound e<68/25 is elementary.
assert d-Q(2*C,2**30)>Q(1,40), ('limit_lower',d)
assert d+Q(2*C,2**30)<Q(1,38), ('limit_upper',d)
assert Q(1,40)-Q(2*C,2**30)>Q(1,41), ('large_n_lower',d)
print('ANALYTIC_LIMIT_ENCLOSURE_CERTIFICATE_PASSED')
print('EXACT_MOMENT_GAP_N30',d)
print('ALL_PAIRED_SPECHT_FOURIER_CHECKS_PASSED')
