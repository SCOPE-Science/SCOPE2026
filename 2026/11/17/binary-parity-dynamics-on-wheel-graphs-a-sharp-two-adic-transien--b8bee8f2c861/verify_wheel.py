#!/usr/bin/env python3
"""Self-contained exact GF(2) rank verification for binary adjacency dynamics on wheels."""
from collections import Counter

def mat(n):
    rows=[0]*(n+1)
    for j in range(1,n+1):
        rows[0]|=1<<j
        rows[j]|=1
        rows[j]|=(1<<(1+(j%n)))|(1<<(1+((j-2)%n)))
    return rows

def apply(rows,x):
    y=0
    for i,r in enumerate(rows):
        if (r & x).bit_count()%2:y|=1<<i
    return y

def rank(cols, d):
    basis={}
    for c in cols:
        while c:
            i=c.bit_length()-1
            if i in basis:c^=basis[i]
            else:
                basis[i]=c;break
    return len(basis)

def ranks(n):
    A=mat(n);d=n+1
    cols=[1<<i for i in range(d)]
    out=[d]
    for _ in range(max(8,n)):
        cols=[apply(A,x) for x in cols]
        out.append(rank(cols,d))
    return out

def formula(n):
    d=n+1
    if n%2:
        return [d]*max(9,n+1)
    v=n & -n
    out=[d]
    out.append(n if v==2 else n-2)
    out.append(n-min(4,v)+(1 if v<=4 else 0))
    for t in range(3,max(9,n+1)):
        out.append(n-min(2*t,v))
    return out

if __name__=='__main__':
    for n in range(3,33):
        a=ranks(n);b=formula(n)
        assert a[:len(b)]==b,(n,a[:len(b)],b)
        if n%2:
            print(f'n={n} odd: all states recurrent, rank={a[0]}')
        else:
            v=n&-n;p=n-v
            counts=[2**p]
            for t in range(1, max(4,v//2+1)):
                counts.append(2**(p+n+1-a[t])-sum(counts))
            while counts[-1]==0:counts.pop()
            assert sum(counts)==2**(n+1),(n,counts)
            print(f'n={n} v={v} recurrent_dim={p} preperiod_hist={counts}')
    # independently enumerate states and first entry to stable rank for n=4,6,8,10
    for n in (3,4,5,6,7,8,10):
        A=mat(n);d=n+1
        r=ranks(n);period_dim=d if n%2 else n-(n&-n)
        bound=next(i for i,x in enumerate(r) if x==period_dim)
        hist=Counter()
        for x in range(1<<d):
            seen={};y=x;t=0
            while y not in seen:
                seen[y]=t
                y=apply(A,y);t+=1
            hist[seen[y]]+=1
        counts=[2**period_dim]+[2**(period_dim+d-r[t])-2**(period_dim+d-r[t-1]) for t in range(1,bound+1)]
        assert [hist[t] for t in range(bound+1)]==counts,(n,hist,counts)
        print('full-enumeration',n,counts)
    print('ALL CHECKS PASSED')
