#!/usr/bin/env python3
"""Finite exact checks for competitive Lotka-Volterra rings.
Uses only the Python 3 standard library. This is not an infinite proof.
"""
from fractions import Fraction as Q
from collections import Counter
from math import cos, pi

SAMPLES = {
    5: ("0.62", "0.8", "0.99"),
    7: ("0.555", "0.58", "0.617"),
    9: ("0.5321", "0.54", "0.5549"),
    11: ("0.5212", "0.526", "0.5320"),
    13: ("0.5150", "0.518", "0.5210"),
    15: ("0.5112", "0.513", "0.5149"),
}

def solve(A, rhs):
    n = len(rhs)
    B = [list(A[i]) + [rhs[i]] for i in range(n)]
    for j in range(n):
        p = next((i for i in range(j,n) if B[i][j] != 0), None)
        if p is None:
            return None
        B[j], B[p] = B[p], B[j]
        z = B[j][j]
        B[j] = [v / z for v in B[j]]
        for i in range(n):
            if i != j and B[i][j]:
                f = B[i][j]
                B[i] = [u - f*v for u,v in zip(B[i],B[j])]
    return [r[-1] for r in B]

def runs(mask,n):
    if mask == (1<<n)-1:
        return [n]
    i = next(i for i in range(n) if not (mask>>i)&1)
    v = [bool((mask>>((i+z)%n))&1) for z in range(1,n+1)]
    runs_, length = [], 0
    for bit in v:
        if bit:
            length += 1
        elif length:
            runs_.append(length)
            length = 0
    return runs_

def pd_path(L,a):
    prev, now = Q(1), Q(1)
    for k in range(2,L+1):
        nxt=now-a*a*prev
        if nxt<=0:return False
        prev,now=now,nxt
    return True

def stable_support(mask,n,a):
    if mask == (1<<n)-1:
        # Only tested beyond the exact full-coexistence stability threshold.
        return False
    S = [i for i in range(n) if (mask>>i)&1]
    if not S:return False
    # If two consecutive species are extinct, at least one has invasion
    # rate >=1-alpha>0 because any surviving equilibrium abundance <=1.
    for i in range(n):
        if not (mask>>i)&1 and (not (mask>>((i-1)%n)&1) or not (mask>>((i+1)%n)&1)):
            return False
    if any(not pd_path(L,a) for L in runs(mask,n)):
        return False
    A=[[Q(int(i==j)) + (a if ((i-j)%n in (1,n-1)) else 0) for j in S]for i in S]
    vals=solve(A,[Q(1)]*len(S))
    if vals is None or any(v<=0 for v in vals):return False
    X={i:v for i,v in zip(S,vals)}
    if any(1-a*(X.get((i-1)%n,0)+X.get((i+1)%n,0))>=0
           for i in range(n) if i not in X):return False
    assert all(sum(A[ii][jj]*vals[jj] for jj in range(len(S)))==1
               for ii in range(len(S)))
    return True

def run():
    checks=0
    for n,values in SAMPLES.items():
        lo=1/(2*cos(pi/n));hi=1/(2*cos(pi/(n-2)))
        for raw in values:
            a=Q(raw)
            assert lo<float(a)<hi,(n,raw,lo,hi)
            count=0
            for mask in range(1,1<<n):
                status=stable_support(mask,n,a)
                checks+=1
                if status:
                    count+=1
                    assert sorted(runs(mask,n))==[1,n-3],(n,raw,mask,runs(mask,n))
            assert count==n,(n,raw,count)
            print('PASS',n,'alpha',raw,'stable states',count)
    print('EXACT SUPPORT TESTS',checks)

if __name__=='__main__':run()
