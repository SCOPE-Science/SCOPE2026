#!/usr/bin/env python3
"""Exact finite-field checks for the characteristic-three Igusa quartic.

No external packages required. The geometric classification is proved separately;
finite-field enumeration is a corroboration, not a substitute for the proof.
"""
from itertools import product
from math import factorial

class Field:
    def __init__(self, m):
        assert m in (1, 2)
        self.m = m
        self.q = 3**m
    def add(self, x, y):
        if self.m == 1:
            return (x+y)%3
        return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
    def neg(self, x):
        if self.m == 1: return (-x)%3
        return ((-x%3)%3)+3*((-(x//3))%3)
    def sub(self,x,y): return self.add(x,self.neg(y))
    def mul(self,x,y):
        if self.m == 1: return x*y%3
        a,b=x%3,x//3
        c,d=y%3,y//3
        # z^2=-1=2 in GF(3), irreducible
        return (a*c+2*b*d)%3 +3*((a*d+b*c)%3)
    def pow(self,x,n):
        r=1
        while n:
            if n&1: r=self.mul(r,x)
            x=self.mul(x,x); n//=2
        return r
    def inv(self,x):
        assert x
        return self.pow(x,self.q-2)
    def sm(self,*xs):
        r=0
        for x in xs: r=self.add(r,x)
        return r

def projective_points(n,q):
    # Exactly one representative: leading nonzero coordinate 1.
    for j in range(n):
        for suffix in product(range(q),repeat=n-j-1):
            yield (0,)*j+(1,)+suffix

def rank(F,m):
    a=[list(row) for row in m]
    rows=len(a); cols=len(a[0]); k=0
    for j in range(cols):
        ip=next((i for i in range(k,rows) if a[i][j]),None)
        if ip is None: continue
        a[k],a[ip]=a[ip],a[k]
        u=F.inv(a[k][j]); a[k]=[F.mul(u,t) for t in a[k]]
        for i in range(rows):
            if i==k:continue
            fac=a[i][j]
            if fac:a[i]=[F.sub(t,F.mul(fac,s)) for t,s in zip(a[i],a[k])]
        k+=1
        if k==rows:break
    return k

def calc(F,x):
    # x=(x1,x2,x3,x4); x5=-sum(x1...x4), x6=0.
    x5=F.neg(F.sm(*x))
    six=(*x,x5,0)
    s2=F.sm(*(F.pow(t,2) for t in six))
    s4=F.sm(*(F.pow(t,4) for t in six))
    val=F.sub(F.pow(s2,2),s4)
    u=[F.sub(t,x5) for t in x]
    # ∂F/∂x_i = s2 * (x_i-x5) - (x_i^3-x5^3)
    grad=[F.sub(F.mul(s2,F.sub(t,x5)),F.sub(F.pow(t,3),F.pow(x5,3))) for t in x]
    # Hessian in four affine cone coordinates after eliminating x5
    H=[[F.add(F.mul(2,F.mul(u[i],u[j])),F.mul(s2,((i==j)+1)%3)) for j in range(4)] for i in range(4)]
    return val,grad,H

def theoretical_nodes(F):
    # Distinct unordered perfect matchings of six indices correspond to 15 nodes.
    out=set()
    for t in set(__import__('itertools').permutations((0,0,1,1,2,2))):
        # Translate by -t6, then use x6=0, then scale first nonzero of x1..x4.
        x=[(z-t[5])%3 for z in t[:4]]
        j=next(j for j,z in enumerate(x) if z)
        inv=F.inv(x[j])
        out.add(tuple(F.mul(z,inv) for z in x))
    assert len(out)==15
    return out

def check(m):
    F=Field(m)
    nodes=theoretical_nodes(F)
    points=0; singular=[]
    for x in projective_points(4,F.q):
        val,grad,H=calc(F,x)
        if val==0:
            points+=1
            if all(t==0 for t in grad):
                assert rank(F,H)==3,(x,H)
                singular.append(x)
    assert len(singular)==15,(m,len(singular))
    assert set(singular)==nodes,(m,set(singular)^nodes)
    print('GF(%d): base P3 total=%d; quartic points=%d; singular=%d; each Hessian rank=3'%(F.q,sum(1 for _ in projective_points(4,F.q)),points,len(singular)))
    return points

def check_cone(m,expected_base):
    F=Field(m)
    # In H: coordinates x1,..,x4, x6=a, x5=-sum(x1..x4)-a.
    # F(x_i+a) is invariant and equals base F(x_i), including all fields.
    cnt=0; singular=0
    for v in projective_points(5,F.q):
        b=v[:4]
        val,grad,_=calc(F,b)
        if val==0:
            cnt+=1
            # derivative vanishes on cone if x1..x4=0 (vertex) or if base singular
            if all(g==0 for g in grad):singular+=1
    assert cnt==1+F.q*expected_base,(cnt,expected_base)
    assert singular==1+15*F.q,(singular,1+15*F.q)
    print('GF(%d): cone P4 points=%d; singular cone points=%d; predicted=(%d,%d)'%(F.q,cnt,singular,1+F.q*expected_base,1+15*F.q))

if __name__=='__main__':
    assert factorial(6)//(factorial(2)**3*factorial(3))==15
    for m in (1,2):
        b=check(m)
        check_cone(m,b)
    print('ALL_IGUSA3_EXACT_CHECKS_PASSED')
