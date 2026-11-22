#!/usr/bin/env python3
"""Independent finite-field enumeration for multiplication-Jordan profiles.
Only uses Python's standard library.  All matrix power ranks are computed
from multiplication of algebra elements (not the predicted ideal formula).
"""
from itertools import product
from collections import Counter
from math import gcd

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5,7,9)
        self.q=q
        self.p=2 if q==4 else (3 if q==9 else q)
    def add(self,a,b):
        if self.q in (4,9):
            p=self.p
            return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
        return (a+b)%self.p
    def mul(self,a,b):
        if self.q==4:
            a0,a1=a%2,a//2;b0,b1=b%2,b//2
            # alpha^2=alpha+1
            return ((a0*b0+a1*b1)%2)+2*((a0*b1+a1*b0+a1*b1)%2)
        if self.q==9:
            a0,a1=a%3,a//3;b0,b1=b%3,b//3
            # alpha^2=-1
            return ((a0*b0-a1*b1)%3)+3*((a0*b1+a1*b0)%3)
        return (a*b)%self.p
    def pow(self,a,n):
        z=1
        for _ in range(n):z=self.mul(z,a)
        return z
    def inv(self,a):
        assert a!=0
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise ValueError('no inverse')
    def neg(self,a):return self.add(0,self.mul(a,self.p-1))

def rank(F,rows):
    B=[row[:] for row in rows]
    if not B:return 0
    m,n=len(B),len(B[0]);r=0
    for c in range(n):
        pivot=next((k for k in range(r,m) if B[k][c]),None)
        if pivot is None:continue
        B[r],B[pivot]=B[pivot],B[r]
        inv=F.inv(B[r][c])
        B[r]=[F.mul(v,inv) for v in B[r]]
        for i in range(m):
            if i==r or B[i][c]==0:continue
            t=B[i][c]
            B[i]=[F.add(B[i][j],F.neg(F.mul(t,B[r][j]))) for j in range(n)]
        r+=1
        if r==m:break
    return r

def mult(F,a,b,aa,bb):
    # indices 0=1; 1..aa-1=x^i; aa..aa+bb-2=y^j; aa+bb-1=s=x^aa=y^bb
    N=aa+bb; v=[0]*N
    def put(t,val):v[t]=F.add(v[t],val)
    # avoid reference to valuation or ideal-rank formulas
    for i,ai in enumerate(a):
        if not ai:continue
        for j,bj in enumerate(b):
            if not bj:continue
            z=F.mul(ai,bj)
            if i==0:put(j,z);continue
            if j==0:put(i,z);continue
            if i==N-1 or j==N-1:continue
            if i<aa and j<aa:
                t=i+j
                if t<aa:put(t,z)
                elif t==aa:put(N-1,z)
            elif aa<=i<N-1 and aa<=j<N-1:
                t=(i-aa+1)+(j-aa+1)
                if t<bb:put(aa+t-1,z)
                elif t==bb:put(N-1,z)
    return v

def actual(F,ell,aa,bb):
    N=aa+bb
    v=[1]+[0]*(N-1)
    rs=[N]
    for k in range(1,N+2):
        v=mult(F,v,ell,aa,bb)
        cols=[]
        for j in range(N):
            basis=[0]*N;basis[j]=1
            cols.append(mult(F,v,basis,aa,bb))
        rs.append(rank(F,[list(z) for z in zip(*cols)]))
        if rs[-1]==0:break
    return tuple(rs)

def predicted(F,ell,aa,bb):
    N=aa+bb
    fx=ell[1:aa]; gy=ell[aa:N-1];c=ell[-1]
    i=next((i for i,x in enumerate(fx,1) if x),10**9)
    j=next((j for j,x in enumerate(gy,1) if x),10**9)
    u=0 if i==10**9 else fx[i-1]
    v=0 if j==10**9 else gy[j-1]
    rs=[N]
    for k in range(1,N+2):
        A=i*k;B=j*k
        if A<aa and B<bb:r=N-A-B
        elif A<aa:r=aa+1-A
        elif B<bb:r=bb+1-B
        else:
            t=0
            if A==aa:t=F.add(t,F.pow(u,k))
            if B==bb:t=F.add(t,F.pow(v,k))
            if k==1:t=F.add(t,c)
            r=int(t!=0)
        rs.append(r)
        if r==0:break
    return tuple(rs)

def to_partition(rs):
    rs=list(rs)+[0,0]
    e=[rs[k-1]-2*rs[k]+rs[k+1] for k in range(1,len(rs)-1)]
    return tuple(d for d in range(len(e),0,-1) for _ in range(e[d-1]))

def formula_hist(F,a,b):
    q=F.q; N=a+b
    result=Counter()
    def add(weight, xval=None, yval=None, i=None, j=None, c=0):
        if not weight:return
        v=[0]*N
        if i is not None:v[i]=xval
        if j is not None:v[a+j-1]=yval
        v[-1]=c
        result[to_partition(predicted(F,v,a,b))]+=weight
    add(1)
    add(q-1,c=1)
    for i in range(1,a):add(q*(q-1)*q**(a-1-i),xval=1,i=i)
    for j in range(1,b):add(q*(q-1)*q**(b-1-j),yval=1,j=j)
    for i in range(1,a):
        for j in range(1,b):
            base=q**(a+b-1-i-j)
            if a%i==0 and b%j==0 and a//i==b//j:
                k=a//i
                d=gcd(k,q-1)
                roots=d if F.pow(F.neg(1),(q-1)//d)==1 else 0
                explicit=sum(F.pow(t,k)==F.neg(1) for t in range(1,q))
                assert roots==explicit
                tminus=next((t for t in range(1,q) if F.pow(t,k)==F.neg(1)),None)
                tplus=next((t for t in range(1,q) if F.pow(t,k)!=F.neg(1)),None)
                if tminus is not None:add(base*(q-1)*roots,1,tminus,i,j)
                if tplus is not None:add(base*((q-1)**2-(q-1)*roots),1,tplus,i,j)
            else:add(base*(q-1)**2,1,1,i,j)
    return result

def run(q,a,b):
    F=Field(q);N=a+b;cnt=0;predtypes=Counter();actualtypes=Counter()
    for tup in product(range(q),repeat=N-1):
        ell=(0,)+tup
        ap=actual(F,ell,a,b);pp=predicted(F,ell,a,b)
        if ap!=pp:
            raise AssertionError((q,a,b,tup,ap,pp))
        predtypes[to_partition(pp)]+=1; actualtypes[to_partition(ap)]+=1;cnt+=1
    assert predtypes==actualtypes==formula_hist(F,a,b) and cnt==q**(N-1)
    print('PASS',f'q={q}',f'a={a}',f'b={b}',f'instances={cnt}',f'Jordan-types={len(predtypes)}')

if __name__=='__main__':
    for cfg in [(2,2,2),(2,2,3),(2,3,3),(2,3,4),(3,2,2),(3,3,3),(3,3,4),(4,2,2),(4,2,3),(5,2,2),(5,3,3),(7,2,2),(9,2,2)]:run(*cfg)
