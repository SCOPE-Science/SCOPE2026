#!/usr/bin/env python3
"""Exact finite permutation checks for record/length-three ordinal-pattern covariance."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

PATTERNS = ('123','132','213','231','312','321')

def predicted(n):
    den=12*n*(n-1)
    return {
      '123':F((n-2)*(5*n-1),den),
      '132':F(-(n-5)*(n-2),den),
      '213':F(2*(n-2)**2,den),
      '231':F(2*(n-2)**2,den),
      '312':F(-2*(n-2)*(2*n-1),den),
      '321':F(-2*(n-2)*(2*n-1),den),
    }

def local_pattern(triple):
    return ''.join(str(1+sum(v<x for v in triple)) for x in triple)

def exact(n):
    sumR=0; sums={p:0 for p in PATTERNS}; cross={p:0 for p in PATTERNS}
    for a in permutations(range(1,n+1)):
        recordmax=0; R=0
        for x in a:
            if x>recordmax:
                R+=1; recordmax=x
        pcounts=dict.fromkeys(PATTERNS,0)
        for i in range(1,n-1):
            pcounts[local_pattern(a[i-1:i+2])]+=1
        sumR+=R
        for p in PATTERNS:
            sums[p]+=pcounts[p]
            cross[p]+=R*pcounts[p]
    N=factorial(n)
    return {p: F(cross[p],N)-F(sumR*sums[p],N*N) for p in PATTERNS}

def local_formula(i,p,which):
    # P(ordinal triple=p AND record at i+which)
    if which==-1:
        first={1:F(1,i*(i+1)),2:F(i-1,i*(i+1)),3:F(i-1,2*(i+1))}[int(p[0])]
        return first/F(i-1)
    if which==0:
        mid=F(i,2*(i+1)) if p[1]=='3' else (F(1,i+1) if p=='123' else 0)
        return mid/F(i)
    last=F(1,2) if p[2]=='3' else F(0)
    return last/F(i+1)

def exact_joint_local(i):
    res={(p,k):0 for p in PATTERNS for k in (-1,0,1)}
    for a in permutations(range(1,i+2)):
        p=local_pattern(a[i-2:i+1])
        for k in (-1,0,1):
            j=i+k
            if a[j-1]==max(a[:j]): res[p,k]+=1
    count=factorial(i+1)
    return {q:F(v,count) for q,v in res.items()}

if __name__ == '__main__':
    count=0
    for n in range(3,9):
        measured=exact(n)
        expected=predicted(n)
        for p in PATTERNS:
            assert measured[p]==expected[p],(n,p,measured[p],expected[p])
            count+=1
        assert sum(measured.values())==0
        print(n,' '.join(f'{p}:{measured[p]}' for p in PATTERNS))
    # Independent local-joint enumerations, not relying on global formula.
    for i in range(2,8):
        q=exact_joint_local(i)
        for pat in PATTERNS:
            for which in (-1,0,1):
                assert q[pat,which]==local_formula(i,pat,which), (i,pat,which,q[pat,which],local_formula(i,pat,which))
                count+=1
    print('VERIFY_OK exact_covariance_checks=',36,'exact_joint_local_checks=',count-36)

