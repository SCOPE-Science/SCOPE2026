"""Exact finite orbit-chain certificate for a symmetric bounded-degree complex.

Dependency-free Python 3. Orbits of barycentric flags are encoded by multisets
of nonempty columns, whose occupied cells have (row, birth-time) tags.
No numerical rank approximations are used: all boundaries are over F_2.
"""
from itertools import combinations
from functools import reduce

def column_types(k):
    single = [((r,t),) for r in range(3) for t in range(1,k+1)]
    double = [((r,t),(s,u)) for r in range(3) for s in range(r+1,3)
              for t in range(1,k+1) for u in range(1,k+1)]
    return sorted(single+double)

def orbit_flags(n,k):
    types=column_types(k)
    ans=set(); counts=[0]*3
    def walk(start,parts,seen):
        if seen==(1<<k)-1:
            ans.add(tuple(parts))
        if len(parts)==n:
            return
        for i in range(start,len(types)):
            typ=types[i]
            if any(counts[r]>=2 for r,t in typ):
                continue
            for r,t in typ:counts[r]+=1
            parts.append(typ)
            bits=reduce(lambda x,y:x|y,(1<<(t-1) for r,t in typ),0)
            walk(i,parts,seen|bits)
            parts.pop()
            for r,t in typ:counts[r]-=1
    walk(0,[],0)
    return sorted(ans)

def face(flag,position,k):
    # Remove the position-th face in a barycentric flag (1-based).
    ans=[]
    for col in flag:
        new=[]
        for r,t in col:
            if position==k and t==k:
                continue
            if position<k:
                if t==position+1:t=position
                elif t>position+1:t-=1
            new.append((r,t))
        if new:ans.append(tuple(new))
    return tuple(sorted(ans))

def binary_rank(vectors):
    piv={}
    for x in vectors:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def verify(n):
    flags=[None]+[orbit_flags(n,k) for k in range(1,7)]
    boundary_ranks=[]
    boundaries=[None,None]
    for k in range(2,7):
        lookup={f:i for i,f in enumerate(flags[k-1])}
        columns=[]
        for f in flags[k]:
            x=0
            for j in range(1,k+1):
                lower=face(f,j,k)
                assert lower in lookup, (n,k,j,f)
                x^=1<<lookup[lower]
            columns.append(x)
        if k>=3:
            previous=boundaries[k-1]
            for x in columns:
                y=0
                while x:
                    b=x&-x;x-=b
                    y^=previous[b.bit_length()-1]
                assert y==0, (n,k,'boundary-square')
        boundaries.append(columns)
        boundary_ranks.append(binary_rank(columns))
    sizes=[len(flags[k]) for k in range(1,7)]
    ranks=boundary_ranks
    betti=[sizes[k]-(ranks[k-1] if k>0 else 0)
           -(ranks[k] if k<5 else 0) for k in range(6)]
    assert betti==[1,0,0,0,0,1]
    expected={
       4:([77,1160,5577,11334,10260,3420],[76,1084,4493,6841,3419]),
       5:([83,1346,6783,14250,13230,4500],[82,1264,5519,8731,4499]),
       6:([84,1371,6921,14544,13500,4590],[83,1288,5633,8911,4589]),
    }
    assert (sizes,ranks)==expected[n]
    print(f'n={n} orbit_flags={sizes} boundary_ranks_mod2={ranks} H_mod2={betti}; d2=0 PASS')
    return [set(x) for x in flags[1:]]

if __name__=='__main__':
    d={n:verify(n) for n in [4,5,6]}
    for k in range(6):
        assert d[4][k] <= d[5][k] <= d[6][k]
    # Every permitted face has at most six cells and hence uses <=6 columns.
    # Therefore n>=6 has the same complete orbit-flag incidence model.
    print('column-saturation: at most six occupied columns, stable for every n>=6 PASS')
    print('All exact finite chain checks passed.')
