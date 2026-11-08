#!/usr/bin/env python3
"""Exact independent finite-field verification of the coordinate-hyperflex tangent divisor."""
from itertools import product

def digits(n, p, deg):
    out=[]
    for _ in range(deg):out.append(n%p);n//=p
    return out

def packed(a,p):return sum(v*p**i for i,v in enumerate(a))

def rem(a,b,p):
    a=list(a)
    while a and a[-1]==0:a.pop()
    while len(a)>=len(b):
        v=a[-1]*pow(b[-1],-1,p)%p
        for j in range(len(b)):a[len(a)-len(b)+j]=(a[len(a)-len(b)+j]-v*b[j])%p
        while a and a[-1]==0:a.pop()
    return a

def irred(p,m):
    for t in range(1,p**m):
        f=digits(t,p,m)+[1]
        if not f[0]:continue
        if all(rem(f,digits(u,p,j)+[1],p) for j in range(1,m//2+1) for u in range(p**j)):
            return f
    raise RuntimeError('no irreducible modulus')

class F:
    def __init__(self,p,r,n=2):
        self.p,self.r,self.m=p,r,n*r
        self.q,self.Q=p**r,p**(n*r)
        self.mod=irred(p,self.m)
        d=[digits(i,p,self.m) for i in range(self.Q)]
        self.add=[[0]*self.Q for _ in range(self.Q)]
        self.mul=[[0]*self.Q for _ in range(self.Q)]
        for i,a in enumerate(d):
            for j,b in enumerate(d):
                self.add[i][j]=packed([(a[k]+b[k])%p for k in range(self.m)],p)
                h=[0]*(2*self.m-1)
                for u in range(self.m):
                    for v in range(self.m):h[u+v]=(h[u+v]+a[u]*b[v])%p
                for k in range(2*self.m-2,self.m-1,-1):
                    c=h[k]
                    for v in range(self.m):h[k-self.m+v]=(h[k-self.m+v]-c*self.mod[v])%p
                self.mul[i][j]=packed(h[:self.m],p)
        self.neg=[packed([(-v)%p for v in a],p) for a in d]
        self.base=[x for x in range(self.Q) if self.pow(x,self.q)==x]
        self.dpow=[self.pow(x,self.q-1) for x in range(self.Q)]
        assert len(self.base)==self.q
    def pow(self,a,n):
        v=1
        while n:
            if n&1:v=self.mul[v][a]
            a=self.mul[a][a];n>>=1
        return v
    def inverse(self,a):return self.pow(a,self.Q-2)
    def count(self,a,b,c):
        # C: a*x^d+b*y^d+c*z^d; coordinate flex tangent union is
        # (b*y^d+c*z^d)(a*x^d+c*z^d)(a*x^d+b*y^d)=0.
        A=[self.mul[a][v] for v in self.dpow]
        B=[self.mul[b][v] for v in self.dpow]
        C=c
        add=self.add
        # affine chart z=1
        count=0
        for ax in A:
            for by in B:
                if add[by][C]==0 or add[ax][C]==0 or add[ax][by]==0:count+=1
        # infinity z=0, chart x=1, and one terminal vertex (0:1:0)
        ax=a
        count+=1+sum((by==0 or add[ax][by]==0) for by in B)
        return count

def order(v,F):
    assert v in F.base and v
    for k in range(1,F.q):
        if F.pow(v,k)==1:return k
    raise RuntimeError('order not found')

def run(p,r,n=2,all_params=True):
    Fld=F(p,r,n);base=Fld.base;add=Fld.add;neg=Fld.neg;mul=Fld.mul
    examined=0;types={}
    for a in base[1:]:
        for b in base[1:]:
            c=neg[add[a][b]]
            if c==0:continue
            aa=mul[neg[c]][Fld.inverse(a)] # -c/a
            bb=mul[neg[c]][Fld.inverse(b)] # -c/b
            cc=mul[neg[b]][Fld.inverse(a)] # -b/a
            assert mul[bb][cc]==neg[aa]
            orders=tuple(order(t,Fld) for t in (aa,bb,cc))
            k=sum(n%t==0 for t in orders)
            from math import lcm
            pair_sum=sum(n%lcm(orders[i],orders[j])==0 for i,j in ((0,1),(0,2),(1,2)))
            if p==2:
                L=lcm(*orders)
                expected=3+(Fld.q-1)*Fld.Q*k-2*(Fld.q-1)**2*(n%L==0)
            else:
                expected=3+(Fld.q-1)*Fld.Q*k-(Fld.q-1)**2*pair_sum
            observed=Fld.count(a,b,c)
            assert observed==expected,(Fld.q,a,b,c,orders,observed,expected)
            assert orders[0]>1 and orders[1]>1 and orders[2]>1
            types[orders]=types.get(orders,0)+1
            examined+=1
            if not all_params and examined==12:break
        if not all_params and examined==12:break
    assert examined>0
    print(f'q={Fld.q} n={n} cases={examined} direct_projective_count=OK order_types={len(types)}')

if __name__=='__main__':
    for p,r in [(5,1),(7,1),(2,3),(3,2),(11,1),(13,1)]:
        run(p,r,all_params=(p<11))
    for p,r in [(5,1),(7,1),(2,3),(3,2)]:
        run(p,r,n=1,all_params=True)
    run(7,1,n=3,all_params=True)
    print('VERIFY_HYPERFLEX_TANGENT_MOTIVE_OK')
