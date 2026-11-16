#!/usr/bin/env python3
"""Exact finite-field character checks using separate computational methods for the rank-one triangular cone.
Only elementary integer and finite-field arithmetic; no numerical tolerance.
"""
from collections import Counter
from itertools import product
import numpy as np

def edges(n): return [(i,j) for i in range(n) for j in range(i+1,n)]

def reps_prime(n,p):
    ed=edges(n); out=[]
    for k in range(n):
        for l in range(k+1,n):
            for uf in product(range(p),repeat=k):
                u=list(uf)+[1]+[0]*(n-k-1)
                for vf in product(range(p),repeat=n-l-1):
                    v=[0]*l+[1]+list(vf)
                    out.append([u[i]*v[j]%p for i,j in ed])
    return np.array(out,dtype=np.int32)

def test_prime(n,p):
    ed=edges(n);d=len(ed); R=reps_prime(n,p);N=p**d
    counts=Counter()
    for start in range(0,N,384):
        nums=np.arange(start,min(N,start+384),dtype=np.int64)
        X=np.stack([(nums//p**i)%p for i in range(d)],axis=1).astype(np.int32)
        z=np.count_nonzero((X @ R.T)%p == 0, axis=1)
        Ws=1-len(R)+p*z
        counts.update(map(int,Ws))
        if n>=4: assert np.all(Ws% (p*p)==(-p)%(p*p))
    if n==2: assert counts[0]==p-1
    if n==3: assert counts[0]==p*p*(p-1)
    if n>=4: assert counts[0]==0
    assert sum(counts.values())==N
    assert sum(w*c for w,c in counts.items())==N
    print('prime',p,'n',n,'ambient',N,'rank-one-lines',len(R),'Fourier-zeros',counts[0], 'distinct-values',len(counts))
    return counts

def test_binary_walsh(n):
    ed=edges(n);d=len(ed); N=1<<d
    f=np.zeros(N,dtype=np.int64)
    f[0]=1
    for a in range(1,1<<n):
        k=a.bit_length()-1
        for b in range(1,1<<n):
            l=(b&-b).bit_length()-1
            if k<l:
                idx=sum(1<<r for r,(i,j) in enumerate(ed) if (a>>i&1) and (b>>j&1))
                f[idx]=1
    g=f.copy()
    for t in range(d):
        g=g.reshape(-1,2,1<<t)
        left=g[:,0,:].copy();right=g[:,1,:].copy()
        g[:,0,:]=left+right;g[:,1,:]=left-right
        g=g.reshape(-1)
    count=Counter(map(int,g))
    if n>=4: assert np.all(g%4==2)
    if n==3: assert count[0]==4
    if n==2: assert count[0]==1
    assert int(f.sum()) == (n-2)*(2**(n-1))+2
    assert int(np.sum(g))==N
    print('binary direct Walsh',n,'ambient',N,'cone-size',int(f.sum()),'Fourier-zeros',count[0], 'minmax',(int(g.min()),int(g.max())))
    return count

# GF(4)=GF(2)[a]/(a^2+a+1), represented by 0,1,a,1+a.
def mul4(x,y):
    r=0
    for i in (0,1):
        if x>>i&1:r ^= (y<<i)
    if r&8:r ^= 0b1100 # a^3=a(a+1)=1 in GF4, x^3+1 multiple of modulus
    if r&4:r ^= 0b111 # a^2=a+1
    return r

def add4(a,b):return a^b

def trace4(a): return a^mul4(a,a) # must be 0 or 1

def test_GF4(n):
    ed=edges(n);d=len(ed);N=4**d
    lines=[]
    for k in range(n):
        for l in range(k+1,n):
            for uf in product(range(4),repeat=k):
                u=list(uf)+[1]+[0]*(n-k-1)
                for vf in product(range(4),repeat=n-l-1):
                    v=[0]*l+[1]+list(vf)
                    lines.append([mul4(u[i],v[j]) for i,j in ed])
    # Full direct additive-character sum, separately from projective formulas, all nonzero scalar representatives.
    s=set([tuple([0]*d)])
    for rep in lines:
        for c in (1,2,3):s.add(tuple(mul4(c,a) for a in rep))
    assert len(s)==1+3*len(lines)
    values=Counter()
    for index in range(N):
        X=[];x=index
        for _ in range(d):X.append(x%4);x//=4
        z=0
        for rep in lines:
            t=0
            for a,b in zip(X,rep):t^=mul4(a,b)
            z+=(t==0)
        v_projective=1-len(lines)+4*z
        v_direct=0
        for A in s:
            t=0
            for a,b in zip(X,A):t^=mul4(a,b)
            v_direct+=1 if trace4(t)==0 else -1
        assert v_direct==v_projective,(index,v_direct,v_projective)
        if n>=4: assert v_direct%16==12
        values[v_direct]+=1
    if n==3:assert values[0]==16*3
    if n>=4: assert values[0]==0
    print('GF4 direct characters',n,'ambient',N,'cone-size',len(s),'zeros',values[0],'values',sorted(values))
    return values

if __name__=='__main__':
    for n in range(2,7):test_binary_walsh(n)
    for p,n in [(3,2),(3,3),(3,4),(3,5),(5,3),(5,4),(7,3)]: test_prime(n,p)
    for n in (3,4):test_GF4(n)
    print('RANK_ONE_TRIANGULAR_FOURIER_ALL_EXACT_CHECKS_PASS')
