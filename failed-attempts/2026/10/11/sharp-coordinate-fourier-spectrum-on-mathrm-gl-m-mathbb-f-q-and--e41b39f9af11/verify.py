#!/usr/bin/env python3
"""Independent finite-domain checks for coordinate-character Fourier Gram matrices on GL_m(F_q).
Uses only Python standard library. Infinite identities are proved in RESULT.md, not by this finite test.
"""
from itertools import product
from fractions import Fraction as F

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q != 4:return a*b%self.q
        c=0
        for i in range(2):
            if (a>>i)&1:
                for j in range(2):
                    if (b>>j)&1:c ^= 1 <<(i+j)
        if c&8:c ^= (8^4^2) # x^3 = x+1 in x^2+x+1, reduce polynomial x^3+x+1
        if c&4:c ^= 7 # x^2 = x+1
        return c
    def inv(self,a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise AssertionError((self.q,a))

def rank(a,n,f):
    x=[list(a[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        v=next((i for i in range(r,n) if x[i][j]),None)
        if v is None:continue
        x[r],x[v]=x[v],x[r]
        d=f.inv(x[r][j]);x[r]=[f.mul(d,z) for z in x[r]]
        for i in range(r+1,n):
            if x[i][j]:
                c=x[i][j]
                x[i]=[f.add(x[i][k],f.neg(f.mul(c,x[r][k]))) for k in range(n)]
        r+=1
    return r

def formula(q,n):
    t=q**n;c=q-1
    u=F(-1,t-1);v=F(1,(t-1)*(q**(n-1)-1))
    mid=F(t*(t-1-n*c),(t-q)*(t-1))
    cyc=F(t,t-q);fib=F(t,t-1)
    h=fib+c*((2*n-1)*u+(n-1)**2*v)
    assert h- n*n*c*u*u == F(t*(t-1-n*c)**2,(t-q)*(t-1)**2)
    return u,v,mid,cyc,fib,h

def full_case(q,n):
    field=Field(q); K=n*n;size=q**(n*n)
    if size>65536:raise ValueError(size)
    inv=[a for a in product(range(q),repeat=K) if rank(a,n,field)==n]
    GL=len(inv)
    expected=1
    for i in range(n):expected*=q**n-q**i
    assert GL==expected
    labels=[None]+[(i,a) for i in range(K) for a in range(1,q)]
    P=len(labels)
    gs=[[F(0) for _ in range(P)] for _ in range(P)]
    u,v,mid,cyc,fib,h=formula(q,n)
    rank_counts=[0,0,0]
    for i,l1 in enumerate(labels):
        gs[i][i]=F(1)
        for j in range(i+1,P):
            l2=labels[j]
            b=[0]*K
            if l1 is not None:b[l1[0]]=field.add(b[l1[0]],l1[1])
            if l2 is not None:b[l2[0]]=field.add(b[l2[0]],field.neg(l2[1]))
            br=rank(b,n,field)
            assert br in (1,2)
            rank_counts[br]+=1
            counts=[0]*q
            inds=[(ind,co) for ind,co in enumerate(b) if co]
            for a in inv:
                z=0
                for ind,co in inds:z=field.add(z,field.mul(a[ind],co))
                counts[z]+=1
            assert len(set(counts[1:]))==1,(q,n,i,j,counts)
            actual=F(counts[0]-counts[1],GL)
            assert actual==(u if br==1 else v),(q,n,i,j,br,actual,u,v)
            gs[i][j]=gs[j][i]=actual
    def action(v):return [sum(gs[i][j]*v[j] for j in range(P)) for i in range(P)]
    def check(v,lambda_):
        a=action(v)
        assert all(x==lambda_*y for x,y in zip(a,v)),(q,n,lambda_,v)
    def uv(vals):
        v=[F(0)]*P
        for j,l in enumerate(labels[1:],1):v[j]=F(vals[l[0]])
        return v
    # Scalar-fiber mean-zero modes.
    if q>2:
        for cell in range(K):
            v=[F(0)]*P
            v[labels.index((cell,1))]=1;v[labels.index((cell,2))]=-1
            check(v,fib)
    # Row and column zero-sum modes.
    for col in range(1,n):
        v=[0]*K
        for row in range(n):v[row*n]=1;v[row*n+col]=-1
        check(uv(v),mid)
    for row in range(1,n):
        v=[0]*K
        for col in range(n):v[col]=1;v[row*n+col]=-1
        check(uv(v),mid)
    # Rectangle interactions.
    for row in range(1,n):
        for col in range(1,n):
            v=[0]*K
            v[0]+=1;v[row*n+col]+=1;v[col]-=1;v[row*n]-=1
            check(uv(v),cyc)
    # Trivial two-dimensional block: basis e0 and sum of all nonconstant characters.
    e0=[F(0)]*P;e0[0]=1
    ew=[F(0)]+[F(1)]*(P-1)
    assert action(e0)==[F(1)]+[u]*(P-1)
    assert action(ew)==[K*(q-1)*u]+[h]*(P-1)
    print('EXACT_GRAM',f'q={q}',f'm={n}',f'GL={GL}',f'functions={P}',f'entries={P*P}',f'rank1_pairs={rank_counts[1]}',f'rank2_pairs={rank_counts[2]}')

if __name__=='__main__':
    # Finite checks do not establish the all-prime-power theorem.
    for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)]:full_case(q,n)
    # Additional exact rational parameter checks of transition and eigenvalue inequalities.
    import math
    for q in range(2,101):
        for n in range(2,2*q+15):
            t=q**n;c=q-1
            u,v,mid,cyc,fib,h=formula(q,n)
            det= h-n*n*c*u*u
            assert det>0 and mid>0 and cyc>fib>mid
            dmid=(mid-1)*(mid-h)-n*n*c*u*u
            dfib=(fib-1)*(fib-h)-n*n*c*u*u
            dcyc=(cyc-1)*(cyc-h)-n*n*c*u*u
            assert dmid<0 and dfib<0
            assert (dcyc>0)==(n<2*q),(q,n,'crossover')
            assert (dcyc<0)==(n>=2*q)
    print('VERIFY_OK full_finite_fields=7 threshold_pairs=11000_plus')
