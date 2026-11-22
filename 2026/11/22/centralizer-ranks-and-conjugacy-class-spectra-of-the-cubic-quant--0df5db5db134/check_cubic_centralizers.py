#!/usr/bin/env python3
"""Direct finite-field commutator-rank checks for a cubic quantum complete intersection."""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,q):
        if q not in (4,7,13): raise ValueError(q)
        self.q=q;self.zero=0;self.one=1
        self.zeta={4:2,7:2,13:3}[q]
    def add(self,x,y):return x^y if self.q==4 else (x+y)%self.q
    def neg(self,x):return x if self.q==4 else (-x)%self.q
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):
        if self.q!=4:return x*y%self.q
        # GF(4) = GF(2)[u]/(u^2+u+1), 2 represents u
        r=0
        for i in range(2):
            for j in range(2):
                if (x>>i)&1 and (y>>j)&1:
                    k=i+j
                    r^=1<<k
        if r&4:r^=7
        return r
    def pow(self,a,n):
        r=1
        for _ in range(n):r=self.mul(r,a)
        return r
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)

BASE=[(i,j) for i in range(3) for j in range(3)]
IDX={v:i for i,v in enumerate(BASE)}

def addprod(F, terms):
    r=0
    for x,y in terms:r=F.add(r,F.mul(x,y))
    return r

def mat_ad(F,a):
    M=[[0]*9 for _ in range(9)]
    z=F.zeta
    for i,(i1,i2) in enumerate(BASE):
        for j,(j1,j2) in enumerate(BASE):
            if i1+j1>2 or i2+j2>2:continue
            comm=F.sub(F.pow(z,i2*j1),F.pow(z,j2*i1))
            k=IDX[i1+j1,i2+j2]
            # ad_a on e_j: sum_i a_i (e_i e_j-e_j e_i)
            M[k][j]=F.add(M[k][j],F.mul(a[i],comm))
    return M

def rank(F,M):
    A=[row[:] for row in M];m=len(A);n=len(A[0]);r=0
    for j in range(n):
        k=next((k for k in range(r,m) if A[k][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        inv=F.inv(A[r][j]);A[r]=[F.mul(inv,x) for x in A[r]]
        for k in range(m):
            if k==r:continue
            v=A[k][j]
            if v:A[k]=[F.sub(x,F.mul(v,y)) for x,y in zip(A[k],A[r])]
        r+=1
        if r==m:break
    return r

def predicted(F,a):
    # PBW coefficients
    A=a[IDX[1,0]];B=a[IDX[0,1]]
    C=a[IDX[2,0]];D=a[IDX[1,1]];E=a[IDX[0,2]]
    f=a[IDX[2,1]];g=a[IDX[1,2]]
    if A or B:return 4
    if C or E:
        delta=F.sub(F.mul(F.mul(F.zeta,C),E),F.mul(D,D))
        return 2 if delta==0 else 3
    if D:return 2
    if f or g:return 1
    return 0

def multiplicities(q):
    return {0:q*q,1:(q*q-1)*q*q,2:(q*q+q-2)*q**4,
            3:(q-1)*(q*q-1)*q**4,4:(q*q-1)*q**7}

def test(F):
    q=F.q; counts=Counter()
    # exhaustive on the parameter space relevant to rank, with f,g=0; 
    # and exhaustive independent tests of f,g on zero low-degree input
    for a,b,c,d,e in product(range(q),repeat=5):
        v=[0]*9
        for ij,val in [((1,0),a),((0,1),b),((2,0),c),((1,1),d),((0,2),e)]:v[IDX[ij]]=val
        p=predicted(F,v);r=rank(F,mat_ad(F,v))
        assert r==p,(q,v,r,p)
        counts[r]+=1
    for f,g in product(range(q),repeat=2):
        v=[0]*9;v[IDX[2,1]]=f;v[IDX[1,2]]=g
        assert rank(F,mat_ad(F,v))==predicted(F,v)
    # check all additional two coefficients for hand-picked lower-degree triples,
    # including characteristic-two and the degenerate rank-two cone
    for c,d,e in [(0,0,0),(1,0,0),(0,1,0),(1,1,1),
                  (1,0,1),(0,0,1)]:
        for f,g in product(range(q),repeat=2):
            v=[0]*9
            for ij,val in [((2,0),c),((1,1),d),((0,2),e),((2,1),f),((1,2),g)]:
                v[IDX[ij]]=val%q
            assert rank(F,mat_ad(F,v))==predicted(F,v)
    expected={0:1,1:0,2:q*q+q-2,3:(q-1)*(q*q-1),4:(q*q-1)*q**3}
    assert counts==Counter(expected),(q,counts,expected)
    # full histogram: multiply independent f,g and two central parameters
    full={r:0 for r in range(5)}
    for r,c in counts.items():full[r]+=c*q**4
    full[0]-=q**4;full[0]+=q*q
    full[1]+=(q*q-1)*q*q
    assert full==multiplicities(q),(q,full,multiplicities(q))
    assert sum(full.values())==q**9
    pc_num=sum(ct*q**(9-r) for r,ct in full.items())
    assert pc_num==q**11*(q**3+2*q*q-2)  # q^18 * (q^3+2q^2-2)/q^7
    print('PASS',q,'zeta',F.zeta,'lower-param exhaustive',q**5,
          'histogram',sorted(full.items()),'commuting pairs',pc_num)

if __name__=='__main__':
    for q in (4,7,13): test(Field(q))
