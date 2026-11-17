#!/usr/bin/env python3
"""Finite simplicial-chain checks for separated Hamming punctures.
No third-party dependencies; all incidence and boundary matrices are generated anew.
"""
from itertools import combinations
from math import comb
from collections import defaultdict

def faces_of_rips_cube(n):
    N=1<<n
    near=[sum(1<<b for b in range(a+1,N) if (a^b).bit_count()<=2) for a in range(N)]
    faces=defaultdict(list)
    def extend(face, candidates):
        if face:
            faces[len(face)-1].append(face)
        while candidates:
            b=candidates & -candidates
            candidates-=b
            v=b.bit_length()-1
            extend(face+(v,), candidates & near[v])
    extend((), (1<<N)-1)
    return dict(faces)

def mod2_rank(cols):
    pivots={}
    for x in cols:
        while x:
            key=x.bit_length()-1
            if key in pivots:
                x ^= pivots[key]
            else:
                pivots[key]=x
                break
    return len(pivots)

def reduced_betti(faces, deleted):
    banned=set(deleted)
    f={k:[simplex for simplex in fs if not banned.intersection(simplex)] for k,fs in faces.items()}
    rk={0:0}
    for k in sorted(f):
        if k==0:continue
        basis={sigma:i for i,sigma in enumerate(f[k-1])}
        columns=[]
        for simplex in f[k]:
            col=0
            for i in range(k+1):
                col ^= 1<<basis[simplex[:i]+simplex[i+1:]]
            columns.append(col)
        rk[k]=mod2_rank(columns)
    answer={k:len(fs)-rk[k]-rk.get(k+1,0) for k,fs in f.items()}
    answer[0]-=1
    return {k:v for k,v in answer.items() if v}

def test_local_pivot(n, code):
    """Distinct cubical 3-sphere cycles have unit local triangle pivots."""
    for p in code:
        pivots=set()
        for s in combinations(range(n),3):
            cube={p^mask for mask in range(1<<n) if mask & ~sum(1<<i for i in s)==0}
            assert len(cube)==8
            assert not (cube.intersection(code)-{p})
            # Antipodes of Q3 are nonedges; there are 16 facets (choose
            # one from each of the four opposite pairs).
            assert sum(1 for t in combinations(cube,4) if all((a^b).bit_count()<=2 for a,b in combinations(t,2)))==16
            # Triangle of all 2-flips appears exactly once in its local sphere.
            triangle=frozenset(p^(1<<i)^(1<<j) for i,j in combinations(s,2))
            assert triangle not in pivots
            pivots.add(triangle)
        assert len(pivots)==comb(n,3)

def main():
    cases=[(3,[0]),(4,[0,15]),(5,[0,15]),(6,[0,15,51,60])]
    for n,code in cases:
        assert all((a^b).bit_count()>=4 for a,b in combinations(code,2))
        f=faces_of_rips_cube(n)
        c=sum((1<<j)*comb(j+3,3) for j in range(n-2))
        assert reduced_betti(f,[])=={3:c}
        test_local_pivot(n,code)
        for t in range(len(code)+1):
            rank=c-t*comb(n,3)
            predicted={} if rank==0 else {3:rank}
            actual=reduced_betti(f,code[:t])
            assert actual==predicted,(n,code[:t],actual,predicted)
        print('PASS', 'n=',n,'punctures=',len(code),'total_faces=',sum(map(len,f.values())),
              'initial_rank=',c,'final_rank=',c-len(code)*comb(n,3))
    print('SEPARATED_HAMMING_PUNCTURES_CHECK_PASS')
if __name__=='__main__':main()
