#!/usr/bin/env python3
"""Exact cyclotomic tensor Fourier checker for classical parking preferences.
Only Python's standard library is required. Run: python3 check_tensor.py
"""
from itertools import product
from collections import Counter
from math import factorial

PHI = {2:(1,1), 3:(1,1,1), 4:(1,0,1), 5:(1,1,1,1,1), 6:(1,-1,1)}

def red(poly, q):
    phi = PHI[q]
    vals = list(poly)
    d = len(phi)-1
    while len(vals) > d:
        c = vals.pop()
        if c:
            shift = len(vals)-d
            for j in range(d):
                vals[shift+j] -= c*phi[j]
    return tuple(vals + [0]*(d-len(vals)))

def mul(a,b,q):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return red(c,q)

def is_parking(a):
    return all(x <= j for j,x in enumerate(sorted(a)))

def spectrum(n):
    q=n+1; d=len(PHI[q])-1; size=q**n
    zero=(0,)*d
    words=list(product(range(q),repeat=n))
    values=[(1,)+(0,)*(d-1) if is_parking(a) else zero for a in words]
    powers=[red([0]*k+[1],q) for k in range(q)]
    for axis in range(n):
        stride=q**(n-axis-1); block=q*stride
        out=[zero]*size
        for start in range(0,size,block):
            for remainder in range(stride):
                inp=[values[start+t*stride+remainder] for t in range(q)]
                for k in range(q):
                    acc=[0]*d
                    for t in range(q):
                        v=mul(inp[t],powers[(k*t)%q],q)
                        for j in range(d): acc[j]+=v[j]
                    out[start+k*stride+remainder]=tuple(acc)
        values=out
    zeros=[f for f,v in zip(words,values) if v==zero]
    forced=[f for f in words if (sum(f)%q==0) and any(f)]
    extra=[f for f in zeros if sum(f)%q]
    expected={(1,2,3,4,5),(1,2,3,3,4),(1,2,3,3,5),
              (1,3,3,4,5),(2,3,3,4,5)}
    expected_extra=expected if n==5 else set()
    assert {tuple(sorted(f)) for f in extra}==expected_extra
    assert len(zeros)==len(forced)+len(extra)
    assert len(extra)==(360 if n==5 else 0)
    assert len(forced)==q**(n-1)-1
    print('n=%d q=%d |PF|=%d total=%d forced=%d extra=%d rank=%d'%(
        n,q, sum(1 for a in words if is_parking(a)),size,len(forced),len(extra),size-len(zeros)))
    return zeros

if __name__=='__main__':
    for n in range(1,6): spectrum(n)
    print('PASS: exact cyclotomic tensor transform, every frequency')
