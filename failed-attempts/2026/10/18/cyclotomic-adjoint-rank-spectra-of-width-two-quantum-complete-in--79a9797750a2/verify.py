"""Finite-field verification of adjoint-rank spectra in skew truncated monomial algebras.
Works in ordinary prime fields and GF(4)."""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, q):
        self.q=q
        if q==4:
            self.add=lambda a,b:a^b
            def mul(a,b):
                c=0
                for i in range(2):
                    for j in range(2):
                        if (a>>i)&1 and (b>>j)&1:
                            c^= (1<<(i+j))
                for k in (3,2):
                    if (c>>k)&1:
                        c^=7<<(k-2)
                return c
            self.mul=mul
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def inv(self,a):
        assert a
        return next(x for x in range(1,self.q) if self.mul(a,x)==1)
    def pow(self,a,n):
        r=1
        for _ in range(n):r=self.mul(r,a)
        return r

def compute_rank(M,F):
    A=[row[:] for row in M]; h=len(A); w=len(A[0]); rank=0
    for j in range(w):
        piv=next((i for i in range(rank,h) if A[i][j]),None)
        if piv is None: continue
        A[rank],A[piv]=A[piv],A[rank]
        iv=F.inv(A[rank][j]); A[rank]=[F.mul(iv,v) for v in A[rank]]
        for i in range(h):
            if i==rank or not A[i][j]:continue
            c=A[i][j]
            A[i]=[F.sub(u,F.mul(c,v)) for u,v in zip(A[i],A[rank])]
        rank+=1
        if rank==h:break
    return rank

def mul(v,w,n,lam,F):
    o=[0]*(2*n)
    for i,a in enumerate(v):
        if a==0:continue
        x= i>=n; d=i%n
        for j,b in enumerate(w):
            if b==0:continue
            y=j>=n; e=j%n
            if d+e>=n or (x and y):continue
            factor=F.pow(lam,d) if (not x and y) else 1
            pos=(n if (x or y) else 0)+d+e
            o[pos]=F.add(o[pos],F.mul(F.mul(a,b),factor))
    return o

def actual_rank(a,n,lam,F):
    columns=[]
    for j in range(2*n):
        ej=[0]*(2*n);ej[j]=1
        x=mul(a,ej,n,lam,F);y=mul(ej,a,n,lam,F)
        columns.append([F.sub(u,v) for u,v in zip(x,y)])
    M=[[col[i] for col in columns] for i in range(2*n)]
    return compute_rank(M,F)

def valuation(c):
    return next((i for i,x in enumerate(c) if x),len(c))

def predicted_rank(a,n,lam,F):
    good=[i for i in range(1,n) if F.pow(lam,i)!=1]
    f=a[:n];g=a[n:]
    s=next((i for i in good if f[i]),n)
    t=valuation(g)
    return n-s+sum(1 for i in good if i+t<s)

def predicted_hist(n,lam,F):
    q=F.q; good=[i for i in range(1,n) if F.pow(lam,i)!=1]
    wfs={n:q**(n-len(good))}
    for s in good:
        wfs[s]=(q-1)*q**(n-sum(i<=s for i in good))
    wgs={t:(q-1)*q**(n-t-1) for t in range(n)};wgs[n]=1
    hist=Counter()
    for s,wf in wfs.items():
        for t,wg in wgs.items():
            r=n-s+sum(1 for i in good if i+t<s)
            hist[r]+=wf*wg
    return hist

def verify(q,n,lam):
    F=Field(q)
    tally=Counter()
    for a in product(range(q),repeat=2*n):
        pred=predicted_rank(a,n,lam,F)
        act=actual_rank(a,n,lam,F)
        if act!=pred:raise AssertionError((q,n,lam,a,act,pred))
        tally[act]+=1
    h=predicted_hist(n,lam,F)
    assert tally==h,(q,n,lam,tally,h)
    assert sum(h.values())==q**(2*n)
    commute=sum(cnt*q**(2*n-r) for r,cnt in h.items())
    print(f'PASS q={q} n={n} lambda={lam} order={next(d for d in range(1,q) if F.pow(lam,d)==1)} hist={dict(sorted(h.items()))} commuting={commute}')

if __name__=='__main__':
    for q,n,lams in [(2,5,[1]),(3,4,[2]),(4,3,[2,3]),(5,3,[2,4]),(7,3,[2,3,6]),(4,4,[2])]:
        for lam in lams:verify(q,n,lam)
    print('VERIFY_OK_QCI_ADJOINT')
