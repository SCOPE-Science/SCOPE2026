#!/usr/bin/env python3
"""Exact rational checks for complete-graph star-deletion fastest mixing formulas.
No third-party dependencies. Finite checks complement the mathematical proof.
"""
from fractions import Fraction as F

def candidate(a,b):
    assert a>=1 and b>=2
    n=1+a+b
    H=4*b-2*a*a-a*b-a
    if b<=a*a:
        tag='capacity-slack'
        x=F(1,a+1);w=F(1,a+b)
        mu2=F(b,(a+1)*(a+b));mu=None
    elif H<=0:
        tag='balanced-boundary'
        x=F(b-a,a*(b-1));w=F(a-1,a*(b-1))
        mu2=1-F(n*(b-a)*(a-1),a*(b-1)**2);mu=None
    else:
        tag='gap-limited'
        d=a*(b+1)+4*b
        x=F(a+2*b,d);w=F(a+2,d)
        mu=F(4*b-a*a,d);mu2=mu*mu
    y=(1-x-b*w)/a
    z=(1-a*w)/b
    return tag,x,y,z,w,mu2,mu

def full_matrix(a,b,params):
    n=1+a+b; _,x,y,z,w,_,_=params
    p=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:continue
            if i==0 or j==0: p[i][j]=x if 1<=max(i,j)<=a else F(0)
            elif i<=a and j<=a:p[i][j]=y
            elif i>a and j>a:p[i][j]=z
            else:p[i][j]=w
    for i in range(n):p[i][i]=1-sum(p[i])
    return p

def check(a,b):
    n=1+a+b
    tag,x,y,z,w,m2,mu=candidate(a,b)
    assert min(x,y,z,w,1-a*x)>=0,(a,b,tag,'feasible')
    assert x+b*w<=1 and a*w<=1
    assert y==F(1-x-b*w,a) and z==F(1-a*w,b)
    # On each block's sum-zero subspace the eigenvalue is exactly zero.
    assert 1-x-a*y-b*w==0
    assert 1-a*w-b*z==0
    S=(a+1)*x+(a+b)*w
    Delta=1-S+n*a*x*w
    T=2-S
    if tag in ('capacity-slack','balanced-boundary'):
        assert T==0 and -Delta==m2 and m2>=0,(a,b,tag,Delta,m2)
        if tag=='capacity-slack':
            assert x==F(1,a+1) and m2==F(b,(a+b)*(a+1))
        else:
            assert x+b*w==1 and b>a*a
            assert 4*b-2*a*a-a*b-a<=0
    else:
        assert mu>0 and mu*mu-mu*T+Delta==0,(a,b,tag)
        other=T-mu
        assert -mu<=other<=mu and mu>=0,(a,b,tag,other,mu)
        d=a*(b+1)+4*b
        assert 1-mu==F(n*a,d)
        assert other==-F(n*a,d)
        assert x+b*w==1 and 4*b-2*a*a-a*b-a>0
    assert m2>=0
    # The row/column probabilities and quotient spectral invariants are tested exactly.
    if n<=20:
        p=full_matrix(a,b,candidate(a,b))
        assert all(sum(row)==1 and min(row)>=0 for row in p)
        assert all(p[i][j]==p[j][i] for i in range(n) for j in range(n))
        assert all(p[0][j]==0 for j in range(a+1,n))
        assert all(p[0][j]==x for j in range(1,a+1))
        assert all(p[i][j]==y for i in range(1,a+1) for j in range(1,a+1))
        assert all(p[i][j]==z for i in range(a+1,n) for j in range(a+1,n))
        assert all(p[i][j]==w for i in range(1,a+1) for j in range(a+1,n))
    # The universal missing-neighbor norm bound is exact in regime I.
    low=F(b,(a+b)*(a+1))
    assert m2>=low,(a,b,tag,m2,low)
    if b>a*a:
        wb=F(a-1,a*(b-1));ws=F(a+2,a*(b+1)+4*b)
        assert wb<F(1,b) and wb<F(1,a+b)
        if tag=='balanced-boundary':assert ws<=wb
        if tag=='gap-limited':assert ws>wb
    return tag

if __name__=='__main__':
    counts={}
    for a in range(1,13):
        for b in range(2,121):
            tag=check(a,b)
            counts[tag]=counts.get(tag,0)+1
    # Stress the high-b asymptotic regime and threshold arithmetic.
    for a in (1,2,3,4,8,16,33):
        for b in (a*a, a*a+1, a*a+9, 1000, 10000):
            if b>=2:
                tag=check(a,b)
                counts[tag]=counts.get(tag,0)+1
    print('EXACT_VERIFY_OK',counts,'total',sum(counts.values()))
