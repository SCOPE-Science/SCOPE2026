#!/usr/bin/env python3
"""Independent finite-field checks for reduced bitangent contact scheme."""
from itertools import product


def arithmetic(p):
    d = next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    zero=(0,0); one=(1,0)
    def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def mul(a,b):return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def power(a,n):
        t=one
        while n:
            if n&1:t=mul(t,a)
            a=mul(a,a); n//=2
        return t
    elems=[(a,b) for a in range(p) for b in range(p)]
    mu4=[t for t in elems if power(t,4)==one]
    mu8=[t for t in elems if power(t,4)==(p-1,0)]
    mu3=[t for t in elems if power(t,3)==one and t!=one]
    assert (len(mu4),len(mu8),len(mu3))==(4,4,2)
    def canon(t):
        for v in reversed(t):
            if v!=zero:
                inv=power(v,p*p-2)
                return tuple(mul(w,inv) for w in t)
        raise AssertionError('zero point')
    H={}
    for r in mu8:
        for pt in ((r,one,zero),(r,zero,one),(zero,r,one)):
            key=canon(pt);assert key not in H;H[key]='hyper'
    O={}
    for a,b,w in product(mu4,mu4,mu3):
        # x=ab*w^2, y=b*w, z=a; tangent coefficients 1,a,b
        pt=(mul(mul(a,b),power(w,2)),mul(b,w),a)
        key=canon(pt)
        assert key not in O and key not in H
        O[key]='ordinary'
        x,y,z=key
        assert add(add(power(x,4),power(y,4)),power(z,4))==zero
        h=add(add(mul(power(x,4),power(y,4)),mul(power(y,4),power(z,4))),mul(power(z,4),power(x,4)))
        assert h==zero
        assert add(add(x,mul(a,y)),mul(b,z))==zero
        # tangent gradient proportional to [1,a,b]
        t=(power(x,3),power(y,3),power(z,3))
        assert mul(t[0],a)==t[1] and mul(t[0],b)==t[2]
    assert len(H)==12 and len(O)==32
    W={**H,**O}
    cycles=[]
    unseen=set(W)
    while unseen:
        point=next(iter(unseen)); cursor=point; orbit=[]
        while cursor not in orbit:
            assert cursor in W
            orbit.append(cursor)
            cursor=canon(tuple(power(c,p) for c in cursor))
        assert cursor==point
        assert set(orbit)<=unseen
        unseen.difference_update(orbit)
        cycles.append((len(orbit),W[point]))
    hfix=sum(1 for k,v in W.items() if v=='hyper' and canon(tuple(power(c,p) for c in k))==k)
    ofix=sum(1 for k,v in W.items() if v=='ordinary' and canon(tuple(power(c,p) for c in k))==k)
    expect_h=12 if p%8==1 else 0
    expect_o={1:32,5:0,7:8,11:0}[p%12]
    assert (hfix,ofix)==(expect_h,expect_o)
    assert all(n in (1,2) for n,_ in cycles)
    # independently enumerate base-field points lying in the two complete intersections
    hcount=ocount=0
    for X in range(p):
      for Y in range(p):
        for Z in (1,):
          if (X**4+Y**4+Z**4)%p:continue
          if X*Y*Z%p==0:hcount+=1
          if (X**4*Y**4+Y**4*Z**4+Z**4*X**4)%p==0:ocount+=1
    for X in range(p):
      Y=1;Z=0
      if (X**4+Y**4)%p==0:hcount+=1
    X=1;Y=0;Z=0
    assert (hcount,ocount)==(expect_h,expect_o),(p,hcount,ocount,expect_h,expect_o)
    return len(W),hfix,ofix,sorted((n,t) for n,t in cycles)


def main():
    ps=(5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    seen={}
    for p in ps:
        total,h,o,cycles=arithmetic(p)
        sig=(h+o,(44-h-o)//2)
        seen.setdefault(p%24,sig)
        assert seen[p%24]==sig
        print('p=%d residue=%d hyper=%d ordinary=%d cycles=%s'%(p,p%24,h,o,sig))
    assert len(seen)==8
    print('FERMAT_CONTACT_SPLITTING_VERIFIED_OK')

if __name__=='__main__':main()
