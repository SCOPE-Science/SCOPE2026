"""Exact direct-convolution checks for the Lagrangian-averaged Heisenberg walk.

Run: python CHECK.py
Only Python's standard library is required. Integer arithmetic verifies the
point probabilities. Prime-order complex matrix checks are an optional extra.
"""
from itertools import product
from fractions import Fraction
from collections import defaultdict
from math import gcd

class Field:
    def __init__(self,q):
        if q not in (3,5,7,9):
            raise ValueError('tested orders are 3, 5, 7, and 9')
        self.q=q
        self.p=3 if q==9 else q
    def add(self,a,b):
        if self.q!=9:return (a+b)%self.p
        return (a%3+b%3)%3+3*((a//3+b//3)%3)
    def neg(self,a):
        return self.sub(0,a)
    def sub(self,a,b):
        if self.q!=9:return (a-b)%self.p
        return ((a%3-b%3)%3)+3*((a//3-b//3)%3)
    def mul(self,a,b):
        if self.q!=9:return a*b%self.p
        a0,a1=a%3,a//3
        b0,b1=b%3,b//3
        return (a0*b0-a1*b1)%3+3*((a0*b1+a1*b0)%3)
    def half(self,a):
        return self.mul(a,2 if self.p==3 else pow(2,-1,self.p))
    def dot(self,a,b):
        z=0
        for u,v in zip(a,b):z=self.add(z,self.mul(u,v))
        return z
    def omega(self,v,w):
        m=len(v)//2
        return self.sub(self.dot(v[:m],w[m:]),self.dot(v[m:],w[:m]))
    def trace_prime(self,a):
        if self.q!=9:return a
        # F_9 with theta^2=-1, the q=3 Frobenius sends theta to -theta.
        return (2*(a%3))%3

def test(q,m):
    F=Field(q)
    Q=q**m
    V=list(product(range(q),repeat=2*m))
    zvec=(0,)*(2*m)
    group=[(v,z) for v in V for z in range(q)]
    A=Fraction(1,Q)
    B=Fraction(1,Q*(Q+1))
    step={v: (A if v==zvec else B) for v in V}
    P2=defaultdict(Fraction)
    for v in V:
        for w in V:
            u=tuple(F.add(x,y) for x,y in zip(v,w))
            z=F.half(F.omega(v,w))
            P2[(u,z)] += step[v]*step[w]
    assert sum(P2.values())==1
    U=Fraction(1,q*Q*Q)
    tv2=sum(abs(P2[g]-U) for g in group)/2
    assert tv2==Fraction(2*(q-1),q*(Q+1)),(q,m,tv2)
    tv1=sum(abs((step[v] if z==0 else 0)-U) for v,z in group)/2
    assert tv1==Fraction(q-1,q)
    chi2=(q*Q*Q)*sum(P2[g]*P2[g] for g in group)-1
    predicted=Fraction(Q*Q-1,(Q+1)**4)+Fraction((q-1)*Q*(Q+1)*8,(Q+1)**4)
    assert chi2==predicted,(q,m,chi2,predicted)
    # Reproduce every point mass for several positive times, not just TV.
    dist={(zvec,0):Fraction(1)}
    for t in range(1,5):
        nxt=defaultdict(Fraction)
        for (v,z),mass in dist.items():
            for w in V:
                out=tuple(F.add(x,y) for x,y in zip(v,w))
                phase=F.half(F.omega(v,w))
                nxt[(out,F.add(z,phase))] += mass*step[w]
        dist=nxt
        assert sum(dist.values())==1
        aa=Fraction(1,(Q+1)**t)
        bb=Fraction(2**t,(Q+1)**t)
        for (v,z) in group:
            d= (Q*Q-1 if v==zvec else -1)*aa
            d+=Fraction(Q,2)*bb*(Q+1 if v==zvec else 1)*(q-1 if z==0 else -1)
            expected=U*(1+d)
            assert dist.get((v,z),0)==expected,(q,m,t,v,z,dist.get((v,z),0),expected)
        tv=sum(abs(dist.get(g,0)-U) for g in group)/2
        assert tv==Fraction(q-1,q)*Fraction(2,Q+1)**(t-1),(q,m,t,tv)
    if q in (3,5,7) and m<=2:
        import cmath
        xs=list(product(range(q),repeat=m))
        idx={x:i for i,x in enumerate(xs)}
        mat=[[0j]*Q for _ in range(Q)]
        for v in V:
            u,w=v[:m],v[m:]
            mass=step[v]
            for i,x in enumerate(xs):
                y=tuple(F.add(x[k],u[k]) for k in range(m))
                phase=F.dot(w,tuple(F.add(x[k],F.half(u[k])) for k in range(m)))
                mat[i][idx[y]] += float(mass)*cmath.exp(2j*cmath.pi*phase/q)
        for i,x in enumerate(xs):
            for j,y in enumerate(xs):
                val=( (1 if x==y else 0) + (1 if tuple(F.neg(t) for t in x)==y else 0))/(Q+1)
                assert abs(mat[i][j]-val)<1e-11,(q,m,i,j,mat[i][j],val)
    print('verified',q,m,'Q',Q,'TV1',tv1,'TV2',tv2,'chi2',chi2)

if __name__=='__main__':
    for q,m in ((3,1),(5,1),(7,1),(3,2),(9,1)):
        test(q,m)
    print('LAGRANGIAN_HEISENBERG_EXACT_CHECKS_PASS')
