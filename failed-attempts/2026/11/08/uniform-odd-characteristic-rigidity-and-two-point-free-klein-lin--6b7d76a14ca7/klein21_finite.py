#!/usr/bin/env python3
"""Exhaustive projective-plane checks of the specialized 21 Klein lines."""
from collections import Counter
from klein21_certificate import L

def modq(q,w,quad=False):
    if quad:
        characteristic=3
        # Represent F9 as (a,b) with w^2=-w-2 = 1+2w in F3.
        def co(x):return (x%characteristic,0)
        def add(a,b):return ((a[0]+b[0])%characteristic,(a[1]+b[1])%characteristic)
        def mul(a,b):return ((a[0]*b[0]+a[1]*b[1])%characteristic,(a[0]*b[1]+a[1]*b[0]+2*a[1]*b[1])%characteristic)
        elts=[(a,b) for a in range(3) for b in range(3)]
        zero=(0,0);one=(1,0)
        def evalr(pair):return ((pair[0])%characteristic,pair[1]%characteristic)
    else:
        def co(x):return x%q
        def add(a,b):return (a+b)%q
        def mul(a,b):return (a*b)%q
        elts=list(range(q));zero=0;one=1
        def evalr(pair):return (pair[0]+w*pair[1])%q
    lines=[tuple(evalr(t) for t in ln) for ln in L]
    assert len(set(lines))==21
    pts=[(one,x,y) for x in elts for y in elts]+[(zero,one,x) for x in elts]+[(zero,zero,one)]
    mult=Counter()
    for p in pts:
        hits=sum(add(add(mul(l[0],p[0]),mul(l[1],p[1])),mul(l[2],p[2]))==zero for l in lines)
        mult[hits]+=1
    assert len(pts)==q*q+q+1
    assert mult[3]==28 and mult[4]==21
    assert all(k in [0,1,3,4] for k in mult),mult
    assert mult[0]==(q-9)*(q-11),mult
    print('FIELD',q,'OMEGA',w,'INCIDENCE',dict(sorted(mult.items())))
    return mult
if __name__=='__main__':
    for q,w,quad in [(7,3,False),(9,None,True),(11,4,False),(11,6,False),(23,9,False)]:
        if not quad and (w*w+w+2)%q:continue
        modq(q,w,quad)
    print('FINITE_VERIFY_OK')
