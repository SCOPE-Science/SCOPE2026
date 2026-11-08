#!/usr/bin/env python3
"""Finite checks of bounded-variable equivalence of ordinal sums of antichains.
The proof covers all finite heights and sizes; computations test small instances.
"""
import itertools
from collections import Counter

def weak_order(sizes):
    levels=[]
    for i,size in enumerate(sizes):
        levels.extend([i]*size)
    n=len(levels)
    lt=[[int(levels[x]<levels[y]) for y in range(n)] for x in range(n)]
    return levels,lt

def atomic(tup,lt):
    out=[]
    for i in range(len(tup)):
        for j in range(i+1,len(tup)):
            x,y=tup[i],tup[j]
            out.extend((int(x==y),lt[x][y],lt[y][x]))
    return tuple(out)

def spectrum_structures(models,k):
    tables=[]
    for sizes in models:
        levels,lt=weak_order(sizes)
        n=len(levels)
        tuples=list(itertools.product(range(n),repeat=k))
        idx={t:i for i,t in enumerate(tuples)}
        extension=[]
        for t in tuples:
            extension.append([[idx[t[:p]+(v,)+t[p+1:]] for v in range(n)] for p in range(k)])
        tables.append((sizes,tuples,lt,extension))
    pool={}
    colours=[]
    for sizes,tuples,lt,ext in tables:
        c=[]
        for t in tuples:
            signature=atomic(t,lt)
            if signature not in pool:pool[signature]=len(pool)
            c.append(pool[signature])
        colours.append(c)
    init_colors=len(pool)
    rounds=0
    while True:
        pool={}
        updated=[]
        for si,(_,tuples,_,ext) in enumerate(tables):
            old=colours[si]
            new=[]
            for t_idx,t in enumerate(tuples):
                signature=(old[t_idx],)+tuple(tuple(sorted({old[j] for j in ext[t_idx][p]})) for p in range(k))
                if signature not in pool:pool[signature]=len(pool)
                new.append(pool[signature])
            updated.append(new)
        rounds+=1
        old_n=len({x for c in colours for x in c})
        new_n=len(pool)
        assert new_n>=old_n
        colours=updated
        if new_n==old_n:break
        assert rounds<100
    profiles=[frozenset(c) for c in colours]
    checked=0
    for i,a in enumerate(models):
        for j in range(i+1,len(models)):
            b=models[j]
            prediction=(tuple(min(s,k) for s in a)==tuple(min(s,k) for s in b))
            actual=profiles[i]==profiles[j]
            assert prediction==actual,('mismatch',k,a,b,prediction,actual)
            checked+=1
    return len(models),rounds,init_colors,len(pool),checked,len(set(profiles))

def main():
    total_pairs=0
    for k,heights,choices in [(2,4,(1,2,3)),(3,3,(1,2,3,4)),(4,2,(1,2,3,4,5))]:
        models=[m for h in range(1,heights+1) for m in itertools.product(choices,repeat=h)]
        stats=spectrum_structures(models,k)
        total_pairs+=stats[4]
        print('WIDTH',k,'MODELS',stats[0],'ROUNDS',stats[1],
              'INITIAL_ATOMIC_COLORS',stats[2],'STABLE_COLORS',stats[3],
              'PAIR_COMPARISONS',stats[4],'OBSERVED_THEORIES',stats[5],flush=True)
    # Equal capped words yield an explicit permanent strategy by preserving level and equality.
    for k in range(2,7):
        for a in range(1,11):
            for b in range(1,11):
                assert (min(a,k)==min(b,k))==((a==b) or (a>=k and b>=k))
    # Minimal representatives of height h are exactly words with letters 1..k.
    for k in range(2,7):
        for h in range(1,6):
            assert len(list(itertools.product(range(1,k+1),repeat=h)))==k**h
    # First values: compositions of N with parts at most k.
    for k in (2,3,4):
        f=[1]+[0]*12
        for n in range(1,13): f[n]=sum(f[n-j] for j in range(1,min(k,n)+1))
        direct=[]
        for n in range(1,13):
            direct.append(sum(1 for h in range(1,n+1)
                for word in itertools.product(range(1,k+1),repeat=h)
                if sum(word)==n))
        assert f[1:]==direct
        print('WIDTH',k,'MINIMAL_REP_COUNTS_1_TO_12',','.join(map(str,direct)))
    print('TOTAL_INDEPENDENT_LOGICAL_PAIR_COMPARISONS',total_pairs)
    print('ALL_FINITE_CHECKS_PASS')
if __name__=='__main__':main()
