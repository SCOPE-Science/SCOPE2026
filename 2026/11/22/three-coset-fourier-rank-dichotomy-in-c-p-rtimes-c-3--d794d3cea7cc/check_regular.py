#!/usr/bin/env python3
"""Exact prime-field rank checks for the 3-tap Frobenius convolution theorem.

Runs all normalized supports for primes 7 and 13, and all 1330
unnormalized supports at 7. The modular prime exceeds the Hadamard
bound for every minor, so these modular ranks equal complex ranks.
"""
from itertools import combinations
from collections import Counter
from math import comb

MOD=2147483647  # prime

def find_t(p):
    return next(t for t in range(2,p) if pow(t,3,p)==1 and t!=1)

def verify(p,full=False):
    t=find_t(p)
    N=3*p
    # Hadamard: every row has 3 ones, so every minor <= 3**(N/2)
    assert 3**N < MOD*MOD
    group=[(a,j) for j in range(3) for a in range(p)]
    lookup={g:i for i,g in enumerate(group)}
    weights=(1,t,(t*t)%p)
    def mul(x,y):
        return ((x[0]+weights[x[1]]*y[0])%p,(x[1]+y[1])%3)
    rows=[[lookup[mul(g,h)] for h in group] for g in group]
    def rank(s):
        M=[[0]*N for _ in range(N)]
        for g in s:
            for c,r in enumerate(rows[g]): M[r][c]=1
        piv=0
        for c in range(N):
            pivot=next((k for k in range(piv,N) if M[k][c]),None)
            if pivot is None: continue
            M[piv],M[pivot]=M[pivot],M[piv]
            r0=M[piv]
            # normalize the row over the exact finite field
            fac=pow(r0[c],-1,MOD)
            for j in range(c,N):r0[j]=(r0[j]*fac)%MOD
            for i in range(piv+1,N):
                ri=M[i]
                v=ri[c]
                if v:
                    for j in range(c+1,N):ri[j]=(ri[j]-v*r0[j])%MOD
                    ri[c]=0
            piv+=1
            if piv==N:break
        return piv
    def expected(s):
        bins=Counter(group[g][1] for g in s)
        if len(bins)<3: return N
        x,y,z=[group[g] for g in s]
        # Normalize the b^0 element to the identity on the left.
        # A normal-form transversal is {a^i, a^j b, a^k b^2}.
        # Left translating by a^-i gives {1,a^(j-i)b,a^(k-i)b^2}.
        i=next(g[0] for g in (x,y,z) if g[1]==0)
        u=(next(g[0] for g in (x,y,z) if g[1]==1)-i)%p
        v=(next(g[0] for g in (x,y,z) if g[1]==2)-i)%p
        return p if (u+t*v)%p==0 else N-2
    count=Counter()
    if full:
        iterator=combinations(range(N),3)
    else:
        iterator=((0,i,j) for i,j in combinations(range(1,N),2))
    for s in iterator:
        got=rank(s)
        want=expected(s)
        if got!=want:raise AssertionError((p,s,got,want))
        count[got]+=1
    if not full:
        count=Counter({k:v*N//3 for k,v in count.items()})
    target={p:p*p,N-2:p*p*(p-1),N:p*(p-1)*(7*p-2)//2}
    assert dict(count)==target,(p,count,target)
    assert sum(count.values())==comb(N,3)
    print('PASS p=%d mode=%s support_counts=%s'%(p,'all' if full else 'all-normalized',dict(sorted(count.items()))))

if __name__=='__main__':
    verify(7,True)
    verify(13,False)
