#!/usr/bin/env python3
"""Exact rational moment/Gram checks for a cubic harmonic sampling theorem.
No numerical integration or external dependencies are used.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, prod, factorial

def poly_term(d, exps, coeff=1):
    return {tuple(exps):F(coeff)}
def add(p,q,scale=1):
    r=p.copy()
    for a,b in q.items():
        r[a]=r.get(a,F(0))+F(scale)*b
    return {a:b for a,b in r.items() if b}
def mon(d, inds):
    exps=[0]*d
    for i in inds: exps[i]+=1
    return poly_term(d,exps)
def multiply(p,q):
    out={}
    for a,c in p.items():
        for b,e in q.items():
            m=tuple(x+y for x,y in zip(a,b))
            out[m]=out.get(m,F(0))+c*e
    return out

def doublefac(n):
    if n<=0:return 1
    return prod(range(n,0,-2))

def sphere_moment(e):
    if any(x%2 for x in e):return F(0)
    d=len(e); deg=sum(e)//2
    return F(prod(doublefac(x-1) for x in e),prod(d+2*j for j in range(deg)))

def orbit_moment(e,k):
    if any(x%2 for x in e):return F(0)
    d=len(e); sup=sum(bool(x) for x in e)
    if sup>k:return F(0)
    return F(comb(d-sup,k-sup), comb(d,k)*k**(sum(e)//2))

def bilinear(p,q,m):
    pq=multiply(p,q)
    return sum((c*m(e) for e,c in pq.items()),F(0))

def basis(d):
    z=[];t=[];s=[]
    for i in range(d):
        p=mon(d,[i,i,i]); c=F(3,d+2)
        for j in range(d):p=add(p,mon(d,[i,j,j]),-c)
        z.append(p)
    for i in range(d):
        js=[j for j in range(d) if j!=i]; ref=js[-1]
        for j in js[:-1]:t.append(add(mon(d,[i,j,j]),mon(d,[i,ref,ref]),-1))
    for inds in combinations(range(d),3):s.append(mon(d,inds))
    return z,t,s

def lambdas(d,k):
    return [F((d+4)*(d+2-3*k)**2,6*k*k*(d-1)),
            F((k-1)*(d-k)*(d+2)*(d+4),2*k*k*(d-1)*(d-2)),
            F((k-1)*(k-2)*(d+2)*(d+4),k*k*(d-1)*(d-2))]

def check(d,k):
    parts=basis(d)
    expected=[d,d*(d-2),comb(d,3)]
    assert list(map(len,parts))==expected
    la=lambdas(d,k)
    B=[(idx,p) for idx,part in enumerate(parts) for p in part]
    for i,(ai,p) in enumerate(B):
        for aj,q in B[:i+1]:
            whole=bilinear(p,q,sphere_moment)
            observed=bilinear(p,q,lambda e:orbit_moment(e,k))
            assert observed==(la[ai]*whole if ai==aj else 0), (d,k,i,ai,aj,observed,whole)
    assert sum(m*l for m,l in zip(expected,la))==sum(expected)
    return la,expected

def main():
    count=0
    for d in range(3,9):
        for k in range(1,d+1):
            la,m=check(d,k); count+=1
            if d in (4,5,7) and k in (2,3,4): print('d,k=',d,k,'spectrum=',la,'multiplicities=',m)
    print('PASS: exact all-entry Gram identities, trace, and sector counts on',count,'(d,k) pairs')

if __name__=='__main__':main()
