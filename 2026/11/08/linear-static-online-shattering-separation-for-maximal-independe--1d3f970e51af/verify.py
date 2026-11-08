#!/usr/bin/env python3
"""Self-contained verifier for maximal-independent-set path shattering."""
import itertools
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def is_mis(word):
    n=len(word)
    return all(not (word[i] and word[i+1]) for i in range(n-1)) and all(
        word[i] or (i>0 and word[i-1]) or (i+1<n and word[i+1])
        for i in range(n))


def mis(n):
    return tuple(w for w in itertools.product((0,1), repeat=n) if is_mis(w))


def vc(n, C):
    for k in range(n, -1, -1):
        for S in itertools.combinations(range(n),k):
            traces = {tuple(w[i] for i in S) for w in C}
            if len(traces)==1<<k:
                return k
    raise AssertionError('empty concept family')


def online(C,n):
    ids=tuple(range(len(C)))
    @lru_cache(None)
    def dimension(sub):
        if len(sub)<=1:return 0
        out=0
        for i in range(n):
            zero=tuple(k for k in sub if C[k][i]==0)
            one=tuple(k for k in sub if C[k][i]==1)
            if zero and one:
                out=max(out,1+min(dimension(zero),dimension(one)))
        return out
    return dimension(ids)


def check_tree(node, constraints=(), depth=0):
    if 'leaf' in node:
        assert set(node)=={'leaf'}
        w=tuple(int(s) for s in node['leaf'])
        assert len(w)==10 and is_mis(w)
        assert all(w[i-1]==b for i,b in constraints)
        assert depth==4
        return [w]
    assert set(node)=={'query_vertex','zero','one'}
    q=node['query_vertex']
    assert type(q)==int and 1<=q<=10 and q not in [i for i,b in constraints]
    left=check_tree(node['zero'],constraints+((q,0),),depth+1)
    right=check_tree(node['one'],constraints+((q,1),),depth+1)
    return left+right


def glue(blocks):
    out=list(blocks[0])
    for B in blocks[1:]:
        sep=0 if out[-1] or B[0] else 1
        out.append(sep)
        out.extend(B)
    return tuple(out)


def main():
    cert=json.loads((ROOT/'tree_P10.json').read_text(encoding='utf8'))
    leaves=check_tree(cert)
    assert len(leaves)==len(set(leaves))==16
    C10=mis(10)
    assert set(leaves)==set(C10)
    actual=[]
    for n in range(1,13):
        C=mis(n)
        d=vc(n,C)
        assert d==(n+1)//3, (n,d)
        expected=None
        if n<=10:
            l=online(C,n)
            expected=l
            assert l==d if n<=9 else l==4
        actual.append((n,len(C),d,expected))
    assert [r[1] for r in actual[:10]]==[1,2,2,3,4,5,7,9,12,16]
    for k in (1,2,3):
        for blocks in itertools.product(C10, repeat=k):
            w=glue(blocks)
            assert len(w)==11*k-1 and is_mis(w)
            for j,b in enumerate(blocks):
                assert w[11*j:11*j+10]==b
    print('MIS_PATH_SHATTERING_CERTIFICATE_PASS')
    print('P10 hypotheses=16; complete depth=4; distinct leaves=16')
    print('n, #MIS, VC, Ldim [None means not computed]:')
    for row in actual:print(*row)
    print('connected gluing: k=1,2,3; product tuples=16,256,4096')

if __name__=='__main__':main()
