#!/usr/bin/env python3
"""Exact small labelled extension check for I3-free oriented digraphs."""
from itertools import product, combinations
from collections import defaultdict
from math import comb

def edges(r):return list(combinations(range(r),2))
def transfer(r):
    E=edges(r); m=len(E); terms=defaultdict(int)
    for mask in range(1<<m):
        es=[E[j] for j in range(m) if mask>>j&1]
        if any(all(tuple(sorted(p)) in es for p in combinations(t,2)) for t in combinations(range(r),3)):
            continue
        W=0
        for vals in product((0,1,2),repeat=r):
            if any(vals[i]==vals[j]==0 for i,j in es):continue
            W+=1
        terms[W]+=2**(m-len(es))
    return dict(sorted(terms.items(),reverse=True))

def direct_count(n,r):
    N=n+r
    pairs=list(combinations(range(N),2))
    free=[(i,j) for i,j in pairs if j>=n]
    tri=[tuple(combinations(t,2)) for t in combinations(range(N),3)]
    pos={p:i for i,p in enumerate(free)}
    relevant=[]
    for t in tri:
        q=[pos[p] for p in t if p in pos]
        if len(q)==3:relevant.append(q)
    total=0
    for vals in product(range(3),repeat=len(free)):
        if all(not(vals[i]==vals[j]==vals[k]==0) for i,j,k in relevant):
            total+=1
    return total

def main():
    expected={1:{3:1},2:{9:2,8:1},3:{27:8,24:12,22:6}}
    for r in range(1,6):
        terms=transfer(r)
        print(f'r={r}: {terms}')
        if r in expected:assert terms==expected[r]
        for n in range(0,4):
            if n*r+comb(r,2)>12:continue
            formula=sum(coeff*W**n for W,coeff in terms.items())
            brute=direct_count(n,r)
            assert formula==brute,(n,r,formula,brute)
            print(f' n={n}, r={r}: {brute}')
        if r>=3:
            bases=sorted(terms,reverse=True)
            assert bases[0]==3**r and bases[1]==8*3**(r-2) and bases[2]==22*3**(r-3),bases[:4]
            assert terms[bases[0]]==2**comb(r,2)
            assert terms[bases[1]]==comb(r,2)*2**(comb(r,2)-1)
    print('ALL_EXACT_ENUMERATION_CHECKS_OK')
if __name__=='__main__':main()
