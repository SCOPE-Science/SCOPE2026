"""Independent finite checks for matching-covered vertex traces of cycles."""
from functools import lru_cache
from collections import Counter

@lru_cache(None)
def concepts(n):
    edges=[(i,(i+1)%n) for i in range(n)]
    found={0}
    for mask in range(1<<n):
        used=0
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                if used & ((1<<u)|(1<<v)): break
                used|=(1<<u)|(1<<v)
        else: found.add(used)
    return tuple(sorted(found))

def crossing(n,S):
    crossing_edges=[(u,(u+1)%n) for u in range(n) if bool(S>>u&1)!=bool(S>>((u+1)%n)&1)]
    def go(k,used):
        if used&S==S: return True
        if k==len(crossing_edges): return False
        u,v=crossing_edges[k]
        return go(k+1,used) or (not used&((1<<u)|(1<<v)) and go(k+1,used|(1<<u)|(1<<v)))
    return go(0,0)

def exceptional(n,S):
    return (n%2==1 and S.bit_count()==(n+1)//2 and
            sum(bool(S>>u&1 and S>>((u+1)%n)&1) for u in range(n))==1 and
            all(S>>u&1 or S>>((u+1)%n)&1 for u in range(n)))

@lru_cache(None)
def ld(C,n):
    if len(C)<=1:return 0
    best=0
    for i in range(n):
        left=tuple(x for x in C if not(x>>i&1))
        right=tuple(x for x in C if x>>i&1)
        if left and right: best=max(best,1+min(ld(left,n),ld(right,n)))
    return best

if __name__=='__main__':
    for n in range(3,12):
        C=concepts(n)
        f=[];exc=[]
        for S in range(1<<n):
            shattered=len({x&S for x in C})==1<<S.bit_count()
            criterion=crossing(n,S) or exceptional(n,S)
            assert shattered==criterion,(n,S,shattered,criterion)
            if shattered:f.append(S)
            if exceptional(n,S):exc.append(S)
        assert len(exc)==(n if n%2 else 0)
        assert max(S.bit_count() for S in f)==(n+1)//2
        assert ld(C,n)==(n+1)//2
        print(f'CHECK_OK n={n} hypotheses={len(C)} shattered={len(f)} exceptional={len(exc)} VC=Ldim={(n+1)//2}')
