#!/usr/bin/env python3
"""Exact orbit-incompatibility Euler-characteristic verifier for KG(7,3)."""
from itertools import combinations
from functools import lru_cache
from collections import Counter
from math import factorial
N=7
TRIPLES=tuple(combinations(range(N),3))
TRIINDEX={t:i for i,t in enumerate(TRIPLES)}
CONFLICT=tuple(sum(1<<j for j,t in enumerate(TRIPLES) if not set(s)&set(t)) for s in TRIPLES)

def partitions(n,cap=None):
    if n==0:
        yield ()
        return
    if cap is None:cap=n
    for k in range(min(cap,n),1-1,-1):
        for rest in partitions(n-k,k):yield (k,)+rest

def permutation(part):
    p=list(range(N)); start=0
    for k in part:
        for j in range(k):p[start+j]=start+(j+1)%k
        start+=k
    assert start==N
    return p

def orbit_model(p):
    tp=[TRIINDEX[tuple(sorted(p[x] for x in t))] for t in TRIPLES]
    unseen=set(range(35)); orbit=[]
    while unseen:
        t=min(unseen);o=[];x=t
        while x not in o:o.append(x);unseen.discard(x);x=tp[x]
        assert x==t
        orbit.append(o)
    valid=[]
    for o in orbit:
        if all(not (CONFLICT[a]&(1<<b)) for a,b in combinations(o,2)):
            valid.append(o)
    bad=[]
    for i,o in enumerate(valid):
        mask=0
        for j,other in enumerate(valid):
            if i!=j and any(CONFLICT[a]&(1<<b) for a in o for b in other):mask|=1<<j
        bad.append(mask)
    return orbit,valid,tuple(bad)

def indep_at_minus_one(adj):
    m=len(adj)
    @lru_cache(None)
    def p(mask):
        if mask==0:return 1
        # choose vertex that maximizes degree for speed
        it=[i for i in range(m) if mask>>i&1]
        i=max(it,key=lambda i:(adj[i]&mask).bit_count())
        a=mask&~(1<<i)
        return p(a)-p(a&~adj[i])
    val=p((1<<m)-1)
    return val,p.cache_info()

def top_char(part):
    # coeff t^6 of product (1-(-t)^k)
    coeff=[1]+[0]*6
    for k in part:
        new=coeff[:]
        for j in range(6-k+1):new[j+k]+=(-1)**(k+1)*coeff[j]
        coeff=new
    return coeff[6]

def class_size(part):
    c=Counter(part); den=1
    for k,m in c.items():den*=k**m*factorial(m)
    return factorial(N)//den

def main():
    rows=[]
    for part in partitions(N):
        p=permutation(part)
        orbit,valid,bad=orbit_model(p)
        pol,info=indep_at_minus_one(bad)
        c9=top_char(part);c6=c9-pol
        row=dict(part='.'.join(map(str,part)),class_size=class_size(part),orbits=len(orbit),valid_orbits=len(valid),clique_polynomial_at_minus_one=pol,reduced_fixed_euler=-pol,trace_H9=c9,trace_H6=c6,recursion_states=info.currsize)
        rows.append(row)
    assert len(rows)==15
    assert sum(r['class_size'] for r in rows)==factorial(7)
    for r,part in zip(rows,partitions(7)):
        # The fixed r-subsets are unions of permutation cycles.
        coeff=[1]+[0]*3
        for cycle in part:
            if cycle<=3:
                nxt=coeff[:]
                for j in range(4-cycle):nxt[j+cycle]+=coeff[j]
                coeff=nxt
        f1,f2,f3=coeff[1],coeff[2],coeff[3]
        epsilon=(-1)**(7-len(part))
        assert r['trace_H9']==epsilon*f1
        assert r['trace_H6']==1+(1+epsilon)*(f3-f2)
    assert rows[-1]['part']=='1.1.1.1.1.1.1' and rows[-1]['trace_H6']==29 and rows[-1]['trace_H9']==7,rows[-1]
    assert sum(r['class_size']*r['trace_H6']**2 for r in rows)%factorial(7)==0
    assert sum(r['class_size']*r['trace_H6']*r['trace_H9'] for r in rows)%factorial(7)==0
    for r in rows:print(r)
    print('character norm6',sum(r['class_size']*r['trace_H6']**2 for r in rows)//factorial(7))
    print('character norm9',sum(r['class_size']*r['trace_H9']**2 for r in rows)//factorial(7))
    print('H6 invariants',sum(r['class_size']*r['trace_H6'] for r in rows)/factorial(7))
    print('H9 invariants',sum(r['class_size']*r['trace_H9'] for r in rows)/factorial(7))
if __name__=='__main__':main()

def fixed_count(part,k):
    coeff=[1]+[0]*k
    for c in part:
        if c<=k:
            new=coeff[:]
            for j in range(k+1-c):new[j+c]+=coeff[j]
            coeff=new
    return coeff[k]

def char_decomposition():
    rows=[]
    for part in partitions(7):
        _,valid,bad=orbit_model(permutation(part));p,_=indep_at_minus_one(bad)
        rows.append((part,class_size(part),-p))
    cs=[row[1] for row in rows]; V=[row[2] for row in rows]
    def ip(x,y):
        q=sum(w*a*b for w,a,b in zip(cs,x,y));assert q%5040==0,(q,x,y)
        return q//5040
    def per_character(lam,mu):
        @lru_cache(None)
        def assignments(i,slots):
            if i==len(mu):return int(all(v==0 for v in slots))
            ans=0
            for j in range(len(lam)):
                if slots[j]>=mu[i]:
                    ss=list(slots);ss[j]-=mu[i]
                    ans+=assignments(i+1,tuple(ss))
            return ans
        return assignments(0,lam)
    spechts={}
    for lam in partitions(7):
        M=[per_character(lam,mu) for mu,_,_ in rows]
        residual=M[:]
        for nu,c in spechts.items():
            a=ip(M,c)
            if a:
                residual=[x-a*y for x,y in zip(residual,c)]
        assert ip(residual,residual)==1,(lam,residual,ip(residual,residual))
        spechts[lam]=residual
    virtual={name:ip(V,c) for name,c in spechts.items()}
    positive={name:a for name,a in virtual.items() if a>0}
    negative={name:-a for name,a in virtual.items() if a<0}
    assert positive == {(7,):1,(4,3):1,(2,2,2,1):1}
    assert negative == {(2,1,1,1,1,1):1,(1,1,1,1,1,1,1):1}
    # Known Betti dimensions 29 and 7 saturate the positive and negative
    # virtual summands: no common irreducible can occur in both degrees.
    assert sum(a*spechts[name][-1] for name,a in positive.items())==29
    assert sum(a*spechts[name][-1] for name,a in negative.items())==7
    H6=[sum(a*spechts[name][i] for name,a in positive.items()) for i in range(15)]
    H9=[sum(a*spechts[name][i] for name,a in negative.items()) for i in range(15)]
    assert [a-b for a,b in zip(H6,H9)]==V
    for i,part in enumerate(partitions(7)):
        assert H9[i]==top_char(part) # independent exterior-power consistency
        assert H6[i]==1+(1+(-1)**(7-len(part)))*(fixed_count(part,3)-fixed_count(part,2))
    for name,a in sorted(virtual.items(),reverse=True):
        if a:print('Virtual Specht',name,'coefficient',a,'dimension',spechts[name][-1])
    print('VIRTUAL_DECOMPOSITION_AND_BETTI_SATURATION_OK')
if __name__=='__main__':char_decomposition()
