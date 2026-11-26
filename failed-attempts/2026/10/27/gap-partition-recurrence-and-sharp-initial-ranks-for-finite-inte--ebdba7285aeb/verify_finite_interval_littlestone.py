#!/usr/bin/env python3
"""Exact finite-interval Littlestone rank; standalone Python 3, standard library only."""
from functools import lru_cache

# A state is the sorted positive lengths of gaps not yet excluded by a zero.
@lru_cache(maxsize=None)
def rank(gaps):
    if not gaps:
        return 0
    best=0
    for i,m in enumerate(gaps):
        fixed=gaps[:i]+gaps[i+1:]
        for a in range(m):
            b=m-a-1
            pos=(a+1).bit_length()-1+(b+1).bit_length()-1
            nxt=tuple(sorted(fixed+tuple(z for z in (a,b) if z)))
            best=max(best,1+min(pos,rank(nxt)))
    return best

def split_witness(gaps,d,start_blocks=None):
    """Build d-depth complete shattered tree as a nested tuple (query, zero, one)."""
    if not d:
        return None
    if start_blocks is None:
        start_blocks=[]
        c=0
        for m in gaps:
            start_blocks.append((c,m))
            c+=m+1
    assert rank(tuple(sorted(m for _,m in start_blocks)))>=d
    for i,(start,m) in enumerate(start_blocks):
        rest=start_blocks[:i]+start_blocks[i+1:]
        for a in range(m):
            b=m-a-1
            pos=(a+1).bit_length()-1+(b+1).bit_length()-1
            children=sorted(rest+[(start,a)] * (a>0)+[(start+a+1,b)]*(b>0))
            if pos>=d-1 and rank(tuple(sorted(length for _,length in children)))>=d-1:
                x=start+a
                return (x,split_witness(None,d-1,children),build_positive(start,x,start+m-1,d-1))
    raise AssertionError(('no witness',gaps,d))

def build_positive(lo,x,hi,d):
    if not d:return None
    return build_product(lo,x,x,hi,d)

def build_product(la,lb,ra,rb,d):
    if not d:return None
    ell=(lb-la+1).bit_length()-1
    rrr=(rb-ra+1).bit_length()-1
    assert ell+rrr>=d
    if ell:
        y=la+(1<<(ell-1))-1
        assert y<lb
        return (y,build_product(y+1,lb,ra,rb,d-1),build_product(la,y,ra,rb,d-1))
    y=ra+(1<<(rrr-1))
    assert y<=rb
    return (y,build_product(la,lb,ra,y-1,d-1),build_product(la,lb,y,rb,d-1))

def check_tree(n,t,d):
    assert (t is None)==(d==0)
    if d==0:return 1
    leaves=[]
    def walk(node,depth,tests):
        if depth==0:
            assert node is None
            leaves.append(tuple(tests));return
        assert node is not None
        x,a,b=node
        assert 0<=x<n
        walk(a,depth-1,tests+[(x,0)])
        walk(b,depth-1,tests+[(x,1)])
    walk(t,d,[])
    assert len(leaves)==2**d
    for path in leaves:
        assert any(all((aa<=x<=bb)==bool(v) for x,v in path)
                   for aa in range(n) for bb in range(aa,n)) or all(v==0 for _,v in path)
    return len(leaves)

def generic_rank(n):
    # Independent recursion on actual sets of interval hypotheses, rather than gap partitions.
    H=[(a,b) for a in range(n) for b in range(a,n)]+[(1,0)]
    masks=[sum(1<<i for i,(a,b) in enumerate(H) if a<=x<=b) for x in range(n)]
    @lru_cache(None)
    def f(S):
        if not S or S&(S-1)==0:return 0
        return max([1+min(f(S&M),f(S&~M)) for M in masks if S&M and S&~M] or [0])
    return f((1<<len(H))-1)

def main():
    expected=[1,2,4,6,9,13,19,27,39,55]
    # Direct implementation, independently testing up through length 16.
    for n in range(1,17):
        assert rank((n,))==generic_rank(n),(n,rank((n,)),generic_rank(n))
    print('INDEPENDENT_RANK_REPLAY_OK n=1..16',flush=True)
    # Check each threshold against its immediately preceding chain length.
    threshold=[]
    for d,n in enumerate(expected,1):
        below=rank((n-1,)) if n>1 else rank(())
        at=rank((n,))
        assert below==d-1 and at==d,(d,n,below,at)
        threshold.append(n)
        t=split_witness((n,),d)
        paths=check_tree(n,t,d)
        print('THRESHOLD_OK',d,n,'rank_before',below,'rank_at',at,'leaf_paths',paths,flush=True)
    assert threshold==expected
    print('TOTAL_CACHED_PARTITION_STATES',rank.cache_info().currsize,flush=True)
    print('ALL_VERIFICATION_OK',flush=True)

if __name__=='__main__':main()
