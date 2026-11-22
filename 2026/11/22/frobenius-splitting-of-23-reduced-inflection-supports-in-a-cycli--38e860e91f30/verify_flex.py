#!/usr/bin/env python3
"""Exact finite-field checks of a generic cyclic-six quartic flex descent theorem.
Public mathematical code; Python standard library only. Execute: python verify_flex.py
"""
from itertools import product
from collections import Counter


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)

def divmodp(a,b,p):
    a=list(trim(a));b=trim(b)
    if b==(0,):raise ZeroDivisionError
    ib=pow(b[-1],-1,p)
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a!=([0]):
        shift=len(a)-len(b);c=a[-1]*ib%p;q[shift]=c
        for j,v in enumerate(b):a[shift+j]=(a[shift+j]-c*v)%p
        a=list(trim(a))
    return trim(q),trim(a)

def all_factors(f,p):
    f=trim([int(i)%p for i in f]);out=[]
    while len(f)>1:
        found=None
        for d in range(1,(len(f)-1)//2+1):
            for coeff in product(range(p),repeat=d):
                h=tuple(coeff)+(1,)
                q,rem=divmodp(f,h,p)
                if rem==(0,):found=(h,q);break
            if found:break
        if found:
            h,f=found;out.append(h)
        else:
            lc=pow(f[-1],-1,p)
            out.append(trim([(x*lc)%p for x in f]));f=(1,)
    return out

def pmul(a,b,p,mod):
    n=len(mod)-1
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    for k in range(len(c)-1,n-1,-1):
        v=c[k]
        for j in range(n):c[k-n+j]=(c[k-n+j]-v*mod[j])%p
        c[k]=0
    return tuple((c+[0]*n)[:n])

def ppow(a,e,p,mod):
    n=len(mod)-1
    out=(1,)+(0,)*(n-1)
    while e:
        if e&1:out=pmul(out,a,p,mod)
        a=pmul(a,a,p,mod);e//=2
    return out

def cycles(p,r):
    assert p>=5 and r%p and (r*r-4)%p
    assert (11*r**4-1080*r*r+3888)%p
    f=(1,0,r%p,0,1)
    P=tuple(t%p for t in (3*r,0,18-r*r,0,5*r,0,2))
    bf=all_factors(f,p);pf=all_factors(P,p)
    assert all(len(fac)>1 for fac in bf+pf)
    assert sum(len(h)-1 for h in bf)==4
    assert sum(len(h)-1 for h in pf)==6
    m=Counter({1:1});m.update(len(h)-1 for h in bf)
    for h in pf:
        e=len(h)-1;q=p**e
        y=(0,1)+(0,)*(e-2) if e>=2 else ((-h[0])%p,)
        y2=pmul(y,y,p,h);y4=pmul(y2,y2,p,h)
        gamma=tuple((-y4[i]-r*y2[i]-(i==0))%p for i in range(e))
        assert any(gamma)
        if q%3==2:
            m[e]+=1;m[2*e]+=1
        else:
            unit=(1,)+(0,)*(e-1)
            if ppow(gamma,(q-1)//3,p,h)==unit:m[e]+=3
            else:m[3*e]+=1
    assert sum(e*c for e,c in m.items())==23,(p,r,m)
    return dict(sorted(m.items()))


def direct_count(p,r,n):
    # Use these *independently selected* irreducible moduli for p=7, n=1,2,3.
    assert p==7 and n in (1,2,3)
    mod={1:(0,1),2:(-3%7,0,1),3:(1,1,0,1)}[n]
    elems=list(product(range(p),repeat=n));zero=(0,)*n;one=(1,)+(0,)*(n-1)
    def add(a,b):return tuple((x+y)%p for x,y in zip(a,b))
    def neg(a):return tuple(-x%p for x in a)
    def scale(a,k):return tuple(k*x%p for x in a)
    def mul(a,b):return pmul(a,b,p,mod)
    def power(a,k):
        t=one
        while k:
            if k&1:t=mul(t,a)
            a=mul(a,a);k//=2
        return t
    cubes=Counter(power(x,3) for x in elems)
    count=1  # rational hyperflex at [1:0:0]
    for y in elems:
        y2=power(y,2);y4=power(y,4)
        gamma=neg(add(add(y4,scale(y2,r)),one))
        for x in elems:
            if power(x,3)!=gamma:continue
            # Hessian in affine Z=1, exact in characteristic seven
            A=add(scale(y2,12),scale(one,2*r))
            B=scale(y,4*r)
            C=add(scale(y2,2*r),scale(one,12))
            H=add(scale(mul(x,add(mul(A,C),neg(mul(B,B)))),6),
                  neg(scale(mul(power(x,4),A),9)))
            if H==zero:count+=1
    return count


def run():
    expected={
     1:{1:5,3:6},
     3:{1:7,2:5,3:2},
     4:{1:7,2:5,6:1},
     6:{1:1,2:2,6:3}}
    assert set(expected)=={r for r in range(7) if r!=0 and (r*r-4)%7 and (11*r**4-1080*r*r+3888)%7}
    for r,m in expected.items():assert cycles(7,r)==m,(r,cycles(7,r))
    for r in (3,4):
        m=cycles(7,r)
        for n in (1,2,3):
            predicted=sum(d*v for d,v in m.items() if n%d==0)
            observed=direct_count(7,r,n)
            assert predicted==observed,(r,n,predicted,observed)
    for p in (5,7,11,13,17,19):
        for r in range(p):
            if r and (r*r-4)%p and (11*r**4-1080*r*r+3888)%p:
                cycles(p,r)
    print('CYCLIC_SIX_QUARTIC_FLEX_FROBENIUS_VERIFIED')

if __name__=='__main__':run()
