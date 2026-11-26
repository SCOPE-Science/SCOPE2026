#!/usr/bin/env python3
"""Independent finite-semigroup checks for block-retraction entropy rates.
Requires Python 3 standard library only.
"""
from itertools import product
from collections import Counter
from math import comb, lgamma, log, exp

def block_idempotents(m):
    return (phi for phi in product(range(m),repeat=m)
            if all(phi[phi[i]]==phi[i] for i in range(m)))

def weight(n,s):
    return sum(comb(n,r)*r**(s*n-r) for r in range(1,n+1))

def predicted(m,n):
    ans=Counter()
    for phi in block_idempotents(m):
        counts=Counter(phi)
        z=1
        for root,s in counts.items():
            z*=weight(n,s)
        ans[phi]=z
    return ans

def direct(m,n):
    counts=Counter()
    blocks=[list(product(range(n),repeat=n)) for _ in range(m)]
    for phi in product(range(m),repeat=m):
        for maps in product(*blocks):
            f=tuple(n*phi[i]+maps[i][j] for i in range(m) for j in range(n))
            if all(f[f[x]]==f[x] for x in range(m*n)):
                counts[phi]+=1
    return counts

def logsumexp(values):
    a=max(values)
    return a+log(sum(exp(v-a) for v in values))

def logweight(n,s):
    terms=[lgamma(n+1)-lgamma(r+1)-lgamma(n-r+1)+(s*n-r)*log(r)
           for r in range(1,n+1)]
    return logsumexp(terms)

def main():
    for m,n in ((2,2),(2,3),(3,2),(3,3),(4,2)):
        p=predicted(m,n)
        b=direct(m,n)
        assert p==b,(m,n,p,b)
        totals=Counter()
        for phi,v in p.items():totals[len(set(phi))]+=v
        print('exact m,n',m,n,'total',sum(totals.values()),'root-counts',dict(totals))
    for m in (2,3,4):
        n=2000
        ls={s:logweight(n,s) for s in range(1,m+1)}
        block=[(phi,sum(ls[s] for s in Counter(phi).values())) for phi in block_idempotents(m)]
        normal=logsumexp([v for phi,v in block])
        for k in range(1,m+1):
            z=logsumexp([v for phi,v in block if len(set(phi))==k])
            pred=(m-k+1)*log(m-k+1)-m*log(m)
            print('asymptotic m,k',m,k,'observed',round((z-normal)/n,6),'predicted',round(pred,6))
    print('VERIFY_OK_FIXED_BLOCK_RETRACTIONS')
if __name__=='__main__':main()
