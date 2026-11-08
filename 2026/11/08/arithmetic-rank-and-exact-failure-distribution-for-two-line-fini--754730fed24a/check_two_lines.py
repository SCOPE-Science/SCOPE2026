#!/usr/bin/env python3
"""Independent brute force check for principal Fourier sampling on two finite-field lines.
Only small finite fields are tested; the mathematical proof is separate.
"""
import cmath, itertools, math
from collections import Counter
import numpy as np

class Field:
    def __init__(self,p,poly=(0,1)):
        self.p,self.poly=p,poly
        self.f=len(poly)-1
        assert poly[-1]==1
        self.q=p**self.f
        self.pows=[p**i for i in range(self.f)]
        self.cs=[[x//p**i%p for i in range(self.f)] for x in range(self.q)]
    def num(self,a):return sum((v%self.p)*self.pows[i] for i,v in enumerate(a))
    def add(self,x,y):return self.num([(a+b)%self.p for a,b in zip(self.cs[x],self.cs[y])])
    def neg(self,x):return self.num([-a for a in self.cs[x]])
    def mul(self,x,y):
        c=[0]*(2*self.f-1)
        for i,a in enumerate(self.cs[x]):
            for j,b in enumerate(self.cs[y]):c[i+j]=(c[i+j]+a*b)%self.p
        for i in range(2*self.f-2,self.f-1,-1):
            coeff=c[i]
            for j in range(self.f): c[i-self.f+j]=(c[i-self.f+j]-coeff*self.poly[j])%self.p
        return self.num(c[:self.f])
    def pow(self,x,n):
        if n<0:return self.pow(self.pow(x,self.q-2),-n)
        out=1
        while n:
            if n&1:out=self.mul(out,x)
            x=self.mul(x,x);n//=2
        return out
    def trace(self,x):
        s=0;y=x
        for _ in range(self.f):s=self.add(s,y);y=self.pow(y,self.p)
        assert all(t==0 for t in self.cs[s][1:]),(self.q,s)
        return s
    def dot(self,v,w):return self.add(self.mul(v[0],w[0]),self.mul(v[1],w[1]))
    def div(self,a,b):return self.mul(a,self.pow(b,self.q-2))
    def order(self,a):
        assert a!=0
        x=1
        for d in range(1,self.q):
            x=self.mul(x,a)
            if x==1:return d
        raise AssertionError('no order')

def run(field):
    F=field;q=F.q
    ls=[(1,s) for s in range(q)]+[(0,1)]
    roots=np.exp(2j*np.pi*np.arange(F.p)/F.p)
    observed=Counter();predicted=Counter();maxerr=0.;total=0
    for i,j in itertools.combinations(range(q+1),2):
        v,w=ls[i],ls[j]
        alpha,beta,gamma=F.dot(v,v),F.dot(w,w),F.dot(v,w)
        if 0 in (alpha,beta,gamma):nullity=0
        else:
            ratio=F.div(F.mul(alpha,beta),F.mul(gamma,gamma))
            assert ratio!=1
            nullity=(q-1)//F.order(ratio)
        S=[(0,0)]+[(F.mul(t,z[0]),F.mul(t,z[1])) for z in [v,w] for t in range(1,q)]
        n=len(S)
        mat=np.empty((n,n),complex)
        for a,x in enumerate(S):
            for b,y in enumerate(S):mat[a,b]=roots[F.trace(F.dot(x,y))]
        s=np.linalg.svd(mat,compute_uv=False)
        calc=int(np.sum(s<1e-7))
        assert calc==nullity, (q,i,j,(alpha,beta,gamma),nullity,calc,s)
        predicted[nullity]+=1
        observed[calc]+=1
        total+=1
    assert sum(observed.values())==(q+1)*q//2
    if q%2==1:
        full=(q+1)//2 if q%4==3 else (5*q-3)//2
    else:full=3*q//2
    assert observed[0]==full,(q,observed,full)
    return {'field_order':q,'characteristic':F.p,'degree':F.f,'pairs':total,'full_rank_pairs':observed[0], 'nullity_histogram':dict(sorted(observed.items()))}

def main():
    fields=[Field(p) for p in [3,5,7,11,13,17]]
    fields += [Field(2,(1,1,1)), Field(2,(1,1,0,1)), Field(2,(1,1,0,0,1)), Field(3,(1,0,1)),Field(5,(2,0,1))]
    # F4 polynomial x^2+x+1, F8 x^3+x+1, F16 x^4+x+1, F9 x^2+1, F25 x^2+2.
    for F in fields:
        print('PASS',run(F),flush=True)
    print('TWO_LINE_FOURIER_RANK_CHECK_PASS')
if __name__=='__main__':main()
