#!/usr/bin/env python3
"""Exact finite-characteristic and finite dihedral-group checks for Chebyshev divisors.
All operations use integer coefficients and modular arithmetic; no external modules.
"""
from math import gcd, comb

def mul_poly(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=(out[i+j]+x*y)%p
    return out

def pow_poly(a,n,p):
    out=[1]
    for _ in range(n): out=mul_poly(out,a,p)
    return out

def cheby_coeff(d,p):
    if d==0:return [2%p]
    if d==1:return [0,1]
    a,b=[2%p],[0,1]
    for k in range(1,d):
        xb=[0]+b
        out=[(xb[i] if i<len(xb) else 0)-(a[i] if i<len(a) else 0) for i in range(len(xb))]
        a,b=b,[z%p for z in out]
    return b

def test_cayley(p,r):
    q=p**r; d=(q+1)//2
    if d<5:return
    coeff=cheby_coeff(d,p)
    plus=[pow(2,i,p) for i in range(d+1)]
    rhs=[0]*(d+1)
    for i,c in enumerate(coeff):
        term=mul_poly(pow_poly([1,1],i,p),pow_poly([1,-1],d-i,p),p)
        for j in range(d+1):rhs[j]=(rhs[j]+c*plus[i]*term[j])%p
    expect=[0]*(d+1); expect[0]=2%p; expect[-1]=2%p
    assert rhs==expect,(p,r,d,rhs,expect)

def op(g,h,d):
    a,ep=g; b,de=h
    return ((a+ep*b)%d,ep*de)

def inv(g,d):
    a,e=g; return ((-e*a)%d,e)

def F(g,Q,d):
    a,e=g;return ((Q*a)%d,e)

def action(g,h,Q,d):
    return op(op(inv(h,d),g,d),F(h,Q,d),d)

def root_count(d,Q,a,eps,n):
    k=eps*Q
    b=a+(k-1)//2
    s=sum(k**i for i in range(n))
    t=gcd(d,k**n-1)
    return t if (b*s)%t==0 else 0

def test_twists(d,Q):
    G=[(a,e) for e in (1,-1) for a in range(d)]
    unused=set(G); orbits=[]
    while unused:
        g=min(unused)
        orb={action(g,h,Q,d) for h in G}
        assert orb <= unused
        unused-=orb
        orbits.append((g,orb))
    for eps in (1,-1):
        m=gcd(d,Q-eps)
        sect=[(g,orb) for g,orb in orbits if g[1]==eps]
        assert len(sect)==(m+gcd(m,2))//2,(d,Q,eps,sect)
        predicted_dihedral=gcd(m,2)
        assert sum(2*gcd(d,Q-eps)==2*d//len(orb) for g,orb in sect)==predicted_dihedral
        for (a,e),orb in sect:
            actual=2*d//len(orb)
            expected=m*(2 if 2*a % m==0 else 1)
            assert actual==expected,(d,Q,a,e,actual,expected)
            for n in range(1,9):
                mapping={j:(eps*Q*j + a+(eps*Q-1)//2)%d for j in range(d)}
                jmap=set(range(d))
                actual_pts=0
                for j in range(d):
                    v=j
                    for _ in range(n):v=mapping[v]
                    if v==j:actual_pts+=1
                assert actual_pts==root_count(d,Q,a,eps,n),(d,Q,a,e,n,actual_pts)
            assert all(len({root_count(d,Q,x,y,n) for (x,y) in orb})==1 for n in range(1,9))
    return len(orbits)

def matmul(A,B,p):
    c=((A[0]*B[0]+A[1]*B[2])%p,(A[0]*B[1]+A[1]*B[3])%p,(A[2]*B[0]+A[3]*B[2])%p,(A[2]*B[1]+A[3]*B[3])%p)
    return matnorm(c,p)

def matnorm(A,p):
    a=next(x for x in A if x%p!=0)
    return tuple((x*pow(a,-1,p))%p for x in A)

def test_s3(p):
    generators=[matnorm((-1,0,0,1),p),matnorm((2,12,-1,2),p)]
    cur={matnorm((1,0,0,1),p)}
    while True:
        nxt=cur|{matmul(x,g,p) for x in cur for g in generators}
        if len(nxt)==len(cur):break
        cur=nxt
        assert len(cur)<=6
    assert len(cur)==6,p

if __name__=='__main__':
    cases=[(3,2),(3,3),(3,4),(5,2),(7,2),(11,1),(13,1),(17,1),(19,1)]
    for p,r in cases:
        d=(p**r+1)//2
        if d<5 or d>125:continue
        test_cayley(p,r)
        for s in (1,2,3):
            if d>65 and s>1:continue
            Q=p**s
            z=test_twists(d,Q)
            print('dihedral',p,r,d,s,'forms',z)
    for p in (3,19,23,43):test_s3(p)
    print('exact checks passed')
