"""Independent incidence/homology check using KG(5,2), Python stdlib only."""
from itertools import combinations
from collections import Counter

V = list(combinations(range(5),2))
E = [(i,j) for i,j in combinations(range(10),2) if set(V[i]).isdisjoint(V[j])]
assert len(V)==10 and len(E)==15

# Explicit vertex isomorphism from the GP(5,2) 0..9 labeling.
ISO=(0,7,3,4,9,8,6,5,2,1)
G1 = sorted({tuple(sorted(x)) for x in (
    [(i, (i+1)%5) for i in range(5)]
    + [(i, i+5) for i in range(5)]
    + [(i+5, (i+2)%5+5) for i in range(5)])})
assert sorted(tuple(sorted((ISO[a],ISO[b]))) for a,b in G1) == E


def faces_for_k(k):
    bad=[]
    for seq in combinations(range(15),k):
        if len({v for i in seq for v in E[i]}) == 2*k:
            bad.append(sum(1<<i for i in seq))
    valid=[m for m in range(1<<15) if all(m & b != b for b in bad)]
    return valid


def rank_f2(columns):
    pivots={}
    for c in columns:
        while c:
            high=c.bit_length()-1
            p=pivots.get(high)
            if p is None:
                pivots[high]=c
                break
            c ^= p
    return len(pivots)


def betti_f2(faces):
    nonempty=sorted([m for m in faces if m], key=lambda m:(m.bit_count(),m))
    by_d={d:[m for m in nonempty if m.bit_count()==d+1]
          for d in range(max(m.bit_count() for m in nonempty))}
    ranks={0:0}
    for d in range(1,max(by_d)+1):
        lowindex={m:i for i,m in enumerate(by_d[d-1])}
        cols=[]
        for x in by_d[d]:
            col=0
            for bit in range(15):
                if x & (1<<bit):
                    col ^= (1<<lowindex[x^(1<<bit)])
            cols.append(col)
        ranks[d]=rank_f2(cols)
    betti={d:len(group)-ranks.get(d,0)-ranks.get(d+1,0)
           for d,group in by_d.items()}
    betti[0]-=1
    return {d:n for d,n in betti.items() if n},ranks

if __name__=='__main__':
    expected={2:{1:6},3:{3:9},4:{5:4},5:{9:5}}
    for k in range(2,6):
        faces=faces_for_k(k)
        b,ranks=betti_f2(faces)
        assert b==expected[k],(k,b)
        print('Kneser k',k,'faces',len(faces),'reduced_F2_betti',b,
              'boundary_ranks',ranks,flush=True)
    print('KNESER_INDEPENDENT_CHECKS_PASS')
