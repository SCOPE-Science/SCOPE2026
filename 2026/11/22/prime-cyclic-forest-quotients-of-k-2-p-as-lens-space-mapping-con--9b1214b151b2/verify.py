#!/usr/bin/env python3
"""Finite checks for the cyclic orbit model of a bipartite graphic-matroid forest complex."""
from collections import defaultdict
from itertools import product


def masks(p):
    return [sum(1 << (i + (p if c == 2 else 0)) for i, c in enumerate(cs) if c) for cs in product(range(3), repeat=p) if any(cs)]

def rotate(mask,p):
    v=0
    for i in range(p):
        if mask & (1 << i): v |= (1 << ((i+1)%p))
        if mask & (1 << (p+i)): v |= (1 << (p+(i+1)%p))
    return v

def cflag(flag,p):
    out=[]; cur=flag
    for k in range(p):
        out.append(cur)
        cur=tuple(rotate(m,p) for m in cur)
    return min(out)

def submasks(mask):
    s=(mask-1)&mask
    while s:
        yield s
        s=(s-1)&mask

def quotient_flags(p):
    fs=masks(p)
    ranks=defaultdict(set)
    memo={}
    def flags_ending(f):
        if f not in memo:
            ans={(f,)}
            for s in submasks(f):
                ans.update(fl+(f,) for fl in flags_ending(s))
            memo[f]=ans
        return memo[f]
    for f in fs:
        for flag in flags_ending(f):
            ranks[len(flag)-1].add(cflag(flag,p))
    return [sorted(ranks[i]) for i in range(p)]

def sparse_rank(columns,mod):
    piv={};rank=0
    for col in columns:
        v={k:(a%mod) for k,a in col.items() if a%mod}
        while v:
            r=min(v)
            if r not in piv:
                a=pow(v[r],-1,mod)
                piv[r]={k:(a*w)%mod for k,w in v.items() if a*w%mod}
                rank+=1
                break
            a=v[r]
            for k,w in piv[r].items():
                z=(v.get(k,0)-a*w)%mod
                if z:v[k]=z
                elif k in v:del v[k]
    return rank

def base_betti(p,mod):
    chain=quotient_flags(p)
    counts=[len(d) for d in chain]
    bdrank=[0]*p
    boundaries=[None]*p
    for j in range(1,p):
        rows={f:i for i,f in enumerate(chain[j-1])}
        columns=[]
        for fl in chain[j]:
            d=defaultdict(int)
            for k in range(len(fl)):
                r=rows[cflag(fl[:k]+fl[k+1:],p)]
                d[r]+=(-1)**k
            columns.append(d)
        boundaries[j]=columns
        bdrank[j]=sparse_rank(columns,mod)
    for j in range(2,p):
        for col in boundaries[j]:
            composition=defaultdict(int)
            for row,a in col.items():
                for r,b in boundaries[j-1][row].items():
                    composition[r]+=a*b
            assert all(v==0 for v in composition.values()),(p,j,composition)
    betti=[counts[j]-(bdrank[j] if j else 0)-(bdrank[j+1] if j+1<p else 0) for j in range(p)]
    return counts,bdrank,betti

def check(p):
    # Forest criterion: two doubled columns form a 4-cycle, no others do.
    good=0
    for cs in product(range(4),repeat=p):  # absent, upper, lower, both
        parent=list(range(p+2))
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        cycle=False
        for i,c in enumerate(cs):
            for hub in (0,1):
                if c==3 or c==hub+1:
                    x,y=root(hub),root(i+2)
                    if x==y:cycle=True
                    else:parent[x]=y
        legal=sum(c==3 for c in cs)<=1
        assert (not cycle)==legal,(p,cs)
        if legal:good+=1
    expected=(p+3)*3**(p-1)
    assert good==expected,(good,expected)
    # The suspended lens model has one cell in dimensions 2..p-1,
    # alternating differential p in odd dimensions >=3, plus an attached p-cell of degree p.
    for coeff in (p,101):
        counts,ranks,betti=base_betti(p,coeff)
        wanted=[1]+[0]*(p-1)
        if coeff==p:
            wanted[2:p]=[1]*(p-2)
        else:wanted[p-1]=1
        assert betti==wanted,(p,coeff,counts,ranks,betti,wanted)
        print(f'p={p} F_{coeff}: chain ranks {counts}; boundary ranks {ranks}; betti {betti}')
    print(f'p={p} forest face count {good}; cross-polytope quotient base check passed')

if __name__=='__main__':
    for p in (3,5):check(p)
    print('VERIFY_OK')
