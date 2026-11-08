#!/usr/bin/env python3
"""Direct small-field verification of a Jordan-spectrum formula for a monomial complete intersection.

No symbolic-matrix rank routine is used: the check builds multiplication tables
in the original monomial basis, multiplies powers and row-reduces independently.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, q):
        if q not in (2,3,4,5):
            raise ValueError('Supported direct-test fields: 2, 3, 4, 5')
        self.q=q
        self.p=2 if q==4 else q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.p
    def neg(self,a):
        return a if self.q==4 else (-a)%self.p
    def mul(self,a,b):
        if self.q!=4:return a*b%self.p
        out=0
        while b:
            if b&1:out^=a
            b>>=1
            a<<=1
            if a&4:a^=7  # reduce z^2 = z + 1 over F_2
        return out
    def inverse(self,a):
        if not a:raise ZeroDivisionError
        if self.q==4:return self.mul(a,a) # nonzero elements have order 3
        return pow(a,-1,self.p)

def vector_product(u,v,m,F):
    z=[0]*(2*m)
    for i in range(m):
        for j in range(m-i):
            z[i+j]=F.add(z[i+j],F.mul(u[i],v[j]))
            z[m+i+j]=F.add(z[m+i+j],F.add(F.mul(u[i],v[m+j]),F.mul(u[m+i],v[j])))
    return z

def matrix_rank(columns,F):
    n=len(columns)
    a=[[columns[j][i] for j in range(n)] for i in range(n)]
    r=0
    for j in range(n):
        t=next((i for i in range(r,n) if a[i][j]!=0),None)
        if t is None:continue
        a[r],a[t]=a[t],a[r]
        z=F.inverse(a[r][j]);a[r]=[F.mul(z,u) for u in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                c=a[i][j]
                a[i]=[F.add(u,F.neg(F.mul(c,v))) for u,v in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

def direct_jordan_type(f,m,F):
    N=2*m
    powers=[N]
    fpower=[1]+[0]*(N-1)
    for t in range(1,m+3):
        fpower=vector_product(fpower,f,m,F)
        cols=[]
        for j in range(N):
            basis=[0]*N;basis[j]=1
            cols.append(vector_product(fpower,basis,m,F))
        powers.append(matrix_rank(cols,F))
    assert powers[-1]==0 and powers[-2]==0
    return tuple(t for t in range(m+1,0,-1) for _ in range(powers[t-1]-2*powers[t]+powers[t+1]))

def valuation(vec,m):
    for i,v in enumerate(vec):
        if v:return i
    return m

def formula_ranks(m,u,v,p):
    ranks=[2*m]
    for t in range(1,m+3):
        alpha=t*u
        beta=None if t%p==0 else (t-1)*u+v
        delta=alpha if beta is None else min(alpha,beta)
        eps=2*alpha-delta
        ranks.append(max(m-delta,0)+max(m-eps,0))
    return ranks

def formula_jordan_type(m,u,v,p):
    ranks=formula_ranks(m,u,v,p)
    return tuple(t for t in range(m+1,0,-1) for _ in range(ranks[t-1]-2*ranks[t]+ranks[t+1]))

def weight(m,w,q):
    return 1 if w==m else (q-1)*q**(m-w-1)

def test(m,q):
    F=Field(q)
    predicted=Counter()
    for u in range(1,m+1):
        for v in range(m+1):
            predicted[formula_jordan_type(m,u,v,F.p)]+=weight(m,u,q)*weight(m,v,q)
    actual=Counter()
    for coords in product(range(q),repeat=2*m-1):
        f=(0,)+coords[:m-1]+coords[m-1:]
        j=direct_jordan_type(f,m,F)
        u=valuation(f[:m],m);v=valuation(f[m:],m)
        assert j==formula_jordan_type(m,u,v,F.p),(m,q,f,j,(u,v))
        actual[j]+=1
    assert actual==predicted,(m,q,actual,predicted)
    assert sum(actual.values())==q**(2*m-1)
    assert all(sum(part)==2*m for part in actual)
    print('VERIFIED m=%d q=%d; %d nilpotent elements; %d Jordan types'%(m,q,sum(actual.values()),len(actual)))
    print('  '+repr(sorted(actual.items())))

if __name__=='__main__':
    for m,q in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]:
        test(m,q)
    print('WIDTH_TWO_JORDAN_SPECTRUM_DIRECT_CHECK_OK')
