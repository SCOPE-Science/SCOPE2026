#!/usr/bin/env python3
"""Exhaustive skew-zero-forcing checks on full graph subdivisions.

Uses no external dependencies. Executed with Python 3.9+.
"""
import itertools
from collections import Counter, deque


def connected(n, es):
    seen={0}
    for _ in range(n):
        for a,b in es:
            if a in seen or b in seen:
                seen.update((a,b))
    return len(seen)==n

def forest(n, es):
    parent=list(range(n))
    def root(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    for a,b in es:
        ra,rb=root(a),root(b)
        if ra==rb:
            return False
        parent[ra]=rb
    return True

def skew_all(n,es):
    m=len(es)
    neighbors=[0]*(n+m)
    for i,(a,b) in enumerate(es):
        neighbors[a]|=1<<(n+i)
        neighbors[b]|=1<<(n+i)
        neighbors[n+i]|=(1<<a)|(1<<b)
    universe=(1<<(n+m))-1
    def closure(blue):
        while True:
            white=universe^blue
            extra=0
            for adj in neighbors:
                wn=adj&white
                if wn and not (wn&(wn-1)):
                    extra|=wn
            if not (extra&white):
                return blue
            blue|=extra
    return {mask for mask in range(1<<(n+m)) if closure(mask)==universe}

def check(n,es):
    m=len(es)
    real=skew_all(n,es)
    predicted=set()
    for mask in range(1<<(n+m)):
        if mask&((1<<n)-1) == 0:
            continue
        uncovered=[es[i] for i in range(m) if not(mask&(1<<(n+i)))]
        if forest(n,uncovered):
            predicted.add(mask)
    assert real==predicted,(n,es,sorted(real^predicted)[:8])
    sizes=Counter(k.bit_count() for k in real)
    opt=min(sizes)
    st=sum(forest(n,[es[i] for i in range(m) if mask>>i&1]) for mask in range(1<<m) if mask.bit_count()==n-1)
    assert opt==m-n+2 and sizes[opt]==n*st,(n,es,opt,sizes[opt],st)
    opts={x for x in real if x.bit_count()==opt}
    slides=0; jumps=0
    for a in opts:
        for b in opts:
            if a>=b or (a^b).bit_count()!=2:
                continue
            jumps+=1
            diff=a^b
            removed = (a & diff).bit_length()-1
            added = (b & diff).bit_length()-1
            if (removed < n and added >= n and removed in es[added-n]) or (added < n and removed >= n and added in es[removed-n]):
                slides += 1
    assert slides==0
    return len(real),opt,len(opts),jumps

def main():
    total=0
    examples=[]
    for n in range(2,5):
        poss=list(itertools.combinations(range(n),2))
        for bits in range(1<<len(poss)):
            es=[e for j,e in enumerate(poss) if bits>>j&1]
            if not connected(n,es):continue
            ans=check(n,es)
            examples.append((n,len(es),ans))
            total+=1
    for n,es in [(5,list(itertools.combinations(range(5),2))),
                 (5,[(0,1),(1,2),(2,3),(3,4),(4,0)]),
                 (5,[(0,1),(0,2),(0,3),(0,4)]),
                 (5,[(0,1),(1,2),(2,3),(3,4),(4,0),(0,2)])]:
        ans=check(n,es)
        examples.append((n,len(es),ans));total+=1
    print('All connected labelled simple graphs on n=2,3,4, plus four n=5 examples: PASS',total)
    print('K5: n,m,total skew sets, min, optimal sets, jump edges:',examples[-4])

if __name__=='__main__':main()
