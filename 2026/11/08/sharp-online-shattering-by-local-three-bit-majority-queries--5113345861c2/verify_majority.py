#!/usr/bin/env python3
"""Independent finite experiments and explicit all-depth mistake-tree verifier."""
from itertools import combinations
from functools import lru_cache

BASEQUERIES = ((0,1,2),(0,1,3),(0,2,3))

def answer(x,tri):
    return int(sum(x[i] for i in tri) >= 2)

def find_base():
    base={}
    for x in __import__('itertools').product((0,1),repeat=4):
        if 0 < sum(x) < 4:
            k=tuple(answer(x,tri) for tri in BASEQUERIES)
            base[k]=x
    assert len(base)==8
    return base

def explicit_tree(max_n=11):
    base=find_base()
    # paths map to (sequence of queried triples on that path, witness vector)
    paths={k:(BASEQUERIES,x) for k,x in base.items()}
    for n in range(4,max_n+1):
        assert len(paths)==2**(n-1)
        for bits,(queries,x) in paths.items():
            assert len(x)==n and len(queries)==n-1
            assert all(answer(x,tri)==b for tri,b in zip(queries,bits))
            assert 0 < sum(x)<n
        print('TREE_CERTIFICATE',n,'depth',n-1,'leaves',len(paths),flush=True)
        if n==max_n:break
        new={}
        for bits,(queries,x) in paths.items():
            i=x.index(0);j=x.index(1)
            t=(i,j,n)
            for b in (0,1):
                y=x+(b,)
                assert answer(y,t)==b
                new[bits+(b,)]=(queries+(t,),y)
        paths=new

def exact_rank(n):
    qs=list(combinations(range(n),3))
    concepts={tuple(answer(x,t) for t in qs) for x in __import__('itertools').product((0,1),repeat=n)}
    concepts=list(concepts)
    masks=[]
    for j in range(len(qs)):
        masks.append(sum(1<<i for i,c in enumerate(concepts) if c[j]))
    full=(1<<len(concepts))-1
    @lru_cache(None)
    def shatter(state,k):
        if not k:return True
        if state.bit_count()<(1<<k):return False
        for mask in masks:
            u=state&mask;v=state&~mask
            if u.bit_count() >= (1<<(k-1)) and v.bit_count()>=(1<<(k-1)) and shatter(u,k-1) and shatter(v,k-1):return True
        return False
    expected=(0 if n<3 else 1 if n==3 else n-1)
    assert shatter(full,expected)
    assert not shatter(full,expected+1)
    print('EXACT_MINIMAX',n,'distinct_concepts',len(concepts),'depth',expected,'states',shatter.cache_info().currsize,flush=True)

if __name__=='__main__':
    explicit_tree(11)
    for n in range(1,9):exact_rank(n)
    print('ALL_TERNARY_MAJORITY_ONLINE_CHECKS_PASS')
