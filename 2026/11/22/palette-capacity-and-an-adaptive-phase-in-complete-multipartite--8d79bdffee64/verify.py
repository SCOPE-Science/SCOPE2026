#!/usr/bin/env python3
"""Reproduce finite checks of multipartite proper-colouring membership dimensions.
Requires only Python 3.10+ standard library.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


def colorings(sizes, q):
    parts = [list(range(sum(sizes[:i]), sum(sizes[:i + 1]))) for i in range(len(sizes))]
    for c in product(range(q), repeat=sum(sizes)):
        sets = [set(c[v] for v in P) for P in parts]
        if all(not (sets[i] & sets[j]) for i in range(len(parts)) for j in range(i+1,len(parts))):
            yield c


def vc_witness(sizes,q):
    r=len(sizes); n=sum(sizes);s=min(r,q-r)
    parts=[list(range(sum(sizes[:i]),sum(sizes[:i+1]))) for i in range(r)]
    ranked=sorted(range(r),key=lambda i:(-sizes[i],i))
    chosen=set(ranked[:s])
    tests=[(v,i) for i in range(r) for v in (parts[i] if i in chosen else parts[i][:1])]
    traces={tuple(int(c[v]==a) for v,a in tests) for c in colorings(sizes,q)}
    assert len(traces)==1<<len(tests), (sizes,q,len(tests),len(traces))
    print('VC witness',sizes,'palette',q,'tests',len(tests),'traces',len(traces),'PASS')


def palette_masks(C,q):
    n=len(C[0]); full=(1<<len(C))-1
    masks=[]
    for v in range(n):
        for a in range(q):
            mask=sum(1<<i for i,c in enumerate(C) if c[v]==a)
            if mask not in (0,full):
                masks.append((v,a,mask))
    return masks


def has_complete_tree(C,q,d):
    masks=palette_masks(C,q)
    full=(1<<len(C))-1
    @lru_cache(maxsize=None)
    def rec(state,depth):
        if depth==0:return True
        if state.bit_count() < (1<<depth):return False
        for v,a,mask in masks:
            yes=state&mask; no=state&~mask
            if yes.bit_count() < (1<<(depth-1)) or no.bit_count() < (1<<(depth-1)):
                continue
            if rec(no,depth-1) and rec(yes,depth-1):return True
        return False
    res=rec(full,d)
    return res,rec.cache_info().currsize


def verify_tree(node,branch,depth,C):
    if depth==0:
        assert set(node)=={'coloring'}
        c=tuple(node['coloring'])
        assert c in C and c in branch
        return 1
    assert set(node)=={'query','zero','one'}
    v,a=node['query'];assert 0<=v<6 and 0<=a<5
    yes={c for c in branch if c[v]==a};no=branch-yes
    assert yes and no
    return verify_tree(node['zero'],no,depth-1,C)+verify_tree(node['one'],yes,depth-1,C)


def main():
    checks=[([2,2],3),([3,2],3),([2,2],4),([2,2,2],4),([2,2,2],5),([2,2,2],6),([3,2,2],4),([3,2,2],5),([2,2,1,1],5),([2,2,1,1],6)]
    for sizes,q in checks:vc_witness(sizes,q)
    for q in (3,4,5,6):
        C=list(colorings([2,2,2],q));print('K(2,2,2) palette',q,'concepts',len(C))
        if q==4:
            has,states=has_complete_tree(C,q,5)
            assert has is False
            print('exhaustive depth 5',has,'memoized states',states,'PASS')
        if q==5:
            node=json.loads((Path(__file__).parent/'tree_certificate.json').read_text(encoding='utf-8'))
            leaves=verify_tree(node,set(C),6,set(C))
            assert leaves==64
            print('depth 6 certificate leaves',leaves,'PASS')
    print('ALL FINITE CHECKS PASSED')

if __name__=='__main__':main()
