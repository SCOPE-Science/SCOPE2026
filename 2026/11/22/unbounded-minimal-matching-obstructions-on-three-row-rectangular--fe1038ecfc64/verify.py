#!/usr/bin/env python3
"""Standalone exact finite checks of boundary-frustrated grid matchings.

Runs independent perfect-matching search after fixing every proposed edge.
The mathematical all-n argument is in RESULT.md; finite tests are corroboration.
"""
from functools import lru_cache


def boundary_options(n, side):
    w=2*n
    if side=='left':
        a,b=0,1
    else:
        a,b=w-1,w-2
    def edge(v,x,u,y):
        return frozenset(((v,x),(u,y)))
    return (
        ('A','top_vertical',edge(0,a,1,a)),
        ('A','bottom_horizontal',edge(2,a,2,b)),
        ('B','bottom_vertical',edge(1,a,2,a)),
        ('B','top_horizontal',edge(0,a,0,b)),
    )


def spine(n):
    return tuple(frozenset(((1,2*j-1),(1,2*j))) for j in range(1,n))


def extension(n, chosen):
    w=2*n
    total=3*w
    forced_used=0
    for e in chosen:
        assert len(e)==2
        (a,b)=tuple(e)
        assert abs(a[0]-b[0])+abs(a[1]-b[1])==1
        assert 0<=a[0]<3 and 0<=b[0]<3
        assert 0<=a[1]<w and 0<=b[1]<w
        for v,c in e:
            bit=1<<(v*w+c)
            if forced_used&bit: return None
            forced_used|=bit
    adj=[[] for _ in range(total)]
    for r in range(3):
        for c in range(w):
            i=r*w+c
            if r+1<3:
                j=(r+1)*w+c
                adj[i].append(j);adj[j].append(i)
            if c+1<w:
                j=i+1
                adj[i].append(j);adj[j].append(i)
    all_mask=(1<<total)-1

    @lru_cache(None)
    def search(mask):
        if mask==all_mask: return ()
        rest=all_mask^mask
        i=(rest&-rest).bit_length()-1
        for j in adj[i]:
            if not mask>>j&1:
                tail=search(mask|(1<<i)|(1<<j))
                if tail is not None: return ((i,j),)+tail
        return None
    tail=search(forced_used)
    if tail is None: return None
    tiling=list(chosen)+[frozenset(((i//w,i%w),(j//w,j%w))) for i,j in tail]
    assert len(tiling)==3*n
    used=set()
    for e in tiling:
        assert not(used&set(e))
        used.update(e)
    assert len(used)==total
    return tiling


def main():
    verified=0
    for n in list(range(2,19))+[20,25,30,40]:
        D=spine(n)
        bad=0;good=0
        for L,ln,le in boundary_options(n,'left'):
            for R,rn,re in boundary_options(n,'right'):
                edges=D+(le,re)
                assert len(set(edges))==n+1
                witness=extension(n,edges)
                if L==R:
                    assert witness is not None,(n,ln,rn,'expected extendable')
                    good+=1
                else:
                    assert witness is None,(n,ln,rn,'unexpected extension')
                    bad+=1
                    for i in range(len(edges)):
                        assert extension(n,edges[:i]+edges[i+1:]) is not None,(n,ln,rn,'not minimal',i)
                    verified+=1
        assert (good,bad)==(8,8)
    print('PHASE_CLASSIFICATION_PASS 21 strip widths')
    print('EIGHT_DISTINCT_MINIMAL_BAD_MATCHINGS_EACH_WIDTH_PASS',verified)
    print('EVERY_SINGLE_DELETION_EXTENDABLE_PASS')
    print('VERIFY_OK')


if __name__=='__main__':main()
