#!/usr/bin/env python3
"""Finite exhaustive majority-dynamics certificates for two cubic graphs.
Only standard Python is required. Vertices are labelled (u_i,v_i)."""
from collections import Counter

N=10

def compute(k):
    # Build two explicit bipartite vertex sets, using the parity of ring indices.
    A = [('u',i) for i in range(N) if i%2==0] + [('v',i) for i in range(N) if i%2==1]
    B = [('u',i) for i in range(N) if i%2==1] + [('v',i) for i in range(N) if i%2==0]
    def neighbors(v):
        kind,i=v
        return ([('u',(i-1)%N),('u',(i+1)%N),('v',i)] if kind=='u'
                else [('v',(i-k)%N),('v',(i+k)%N),('u',i)])
    def update_domain(src,dst):
        loc={v:j for j,v in enumerate(src)}
        addr=[tuple(loc[w] for w in neighbors(v)) for v in dst]
        assert all(len(set(t))==3 for t in addr)
        return [sum(1<<i for i,ids in enumerate(addr)
                    if sum((x>>j)&1 for j in ids)>=2) for x in range(1<<10)]
    U=update_domain(B,A) # update on shore A, reading B
    V=update_domain(A,B) # update on shore B, reading A
    TA=[U[V[x]] for x in range(1024)]
    TB=[V[U[x]] for x in range(1024)]
    assert all(TA[TA[TA[x]]]==TA[TA[x]] for x in range(1024))
    assert all(TB[TB[TB[x]]]==TB[TB[x]] for x in range(1024))
    fixA={x for x in range(1024) if TA[x]==x}
    fixB={x for x in range(1024) if TB[x]==x}
    assert len(fixA)==len(fixB)==124
    def terminal(T,fix):
        out=[]; depths=[]
        for x in range(1024):
            y=x; d=0
            while y not in fix:
                y=T[y];d+=1
                assert d<=20
            out.append(y);depths.append(d)
        return out,depths
    limA,depthA=terminal(TA,fixA)
    limB,depthB=terminal(TB,fixB)
    assert max(depthA)==max(depthB)==2
    basinA=Counter(limA);basinB=Counter(limB)
    fixed_basin=sum(basinB[b]*basinA[U[b]] for b in fixB)
    # A fixed F-state is uniquely (a,V[a]) for a fixed by T_A.
    weight=Counter((a.bit_count()+V[a].bit_count()) for a in fixA)
    flip=Counter()
    for a in fixA:
        for b in fixB:
            # First state: (a,b); successor (U[b],V[a]).
            delta=(a^U[b]).bit_count()+(b^V[a]).bit_count()
            if delta:flip[delta]+=1
    assert sum(weight.values())==124
    assert sum(flip.values())==124*124-124
    # Count least first 2-return time without materializing the million-state map.
    hist=Counter()
    for a in range(1024):
        for b in range(1024):
            x,y=a,b
            for t in range(22):
                if TA[x]==x and TB[y]==y:
                    p=1 if U[y]==x and V[x]==y else 2
                    hist[(t,p)]+=1
                    break
                # After a single F update, A and B swap through U,V.
                x,y=U[y],V[x]
            else:raise AssertionError((k,a,b))
    print('GP(10,{}) K_A={} K_B={} fixed={} primitive_two={} basin_fixed={} basin_two={} max_entry={}'.format(
       k,len(fixA),len(fixB),sum(weight.values()),sum(flip.values())//2,
       fixed_basin,1048576-fixed_basin,max(t for t,p in hist)))
    print(' fixed_weight',sorted(weight.items()))
    print(' two_flip_orbits',sorted((i,n//2) for i,n in flip.items()))
    print(' entry_period',sorted(hist.items()))
    # reduced fixed F-state counts obtained by one-shore fixed point sum
    assert sum((1 if U[b]==a else 0) for a in fixA for b in fixB)==124
    assert fixed_basin==sum(v for (t,p),v in hist.items() if p==1)
    return weight,flip,hist

if __name__=='__main__':
   compute(1);compute(3)
