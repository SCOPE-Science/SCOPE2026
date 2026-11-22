#!/usr/bin/env python3
"""Independent exact constant-weight-three coset enumeration (no dependencies)."""
import itertools, math, sys, json

def check(n,k):
    triples = [(1<<i)|(1<<j)|(1<<l) for i,j,l in itertools.combinations(range(n),3)]
    counts={}
    full=[]
    best=[]
    total=0
    for piv in itertools.combinations(range(n),k):
        nonpiv=tuple(c for c in range(n) if c not in piv)
        allowed=[tuple(c for c in nonpiv if c>p) for p in piv]
        # independently parameterize each reduced row as the pivot plus a subset of allowed columns
        opts=[]
        for p,al in zip(piv,allowed):
            opts.append([1<<p|sum(1<<c for j,c in enumerate(al) if (mask>>j)&1) for mask in range(1<<len(al))])
        for rows in itertools.product(*opts):
            total+=1
            # Rather than reducing each weight-three word, take the orbit union under the eight kernel translations.
            subspace=[0]
            for row in rows: subspace += [v ^ row for v in subspace]
            covered=bytearray(1<<n)
            sz=0
            for w in triples:
                for h in subspace:
                    x=w^h
                    if not covered[x]: covered[x]=1;sz+=1
            quotient=sz//(1<<k)
            assert sz%(1<<k)==0
            counts[quotient]=counts.get(quotient,0)+1
            if quotient==(1<<(n-k)) and len(full)<3: full.append(rows)
            if quotient==max(counts) and len(best)<3: best.append(rows)
    assert total==math.prod((2**(n-i)-1) for i in range(k))//math.prod((2**(k-i)-1) for i in range(k))
    return {'n':n,'k':k,'m':n-k,'subspaces':total,'distribution':dict(sorted(counts.items())), 'full_witnesses':full}

if __name__=='__main__':
    profiles=[(5,2),(6,2),(6,3),(7,2),(7,3),(8,3),(9,3)]
    for n,k in profiles:
        if len(sys.argv)>1 and (n,k)!=(int(sys.argv[1]),int(sys.argv[2])): continue
        result=check(n,k)
        print(json.dumps(result,separators=(',',':')), flush=True)
