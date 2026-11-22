#!/usr/bin/env python3
"""Exact normalized cellular-chain verification of the first exceptional cycle lengths.

Needs Python >=3.10 and SymPy >=1.10. The construction uses the cycle shortest-
path metric and ordered simplices with total consecutive length bounded by L.
All calculations are over the integers or exact rationals; no floating point.
"""
from itertools import product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

EXPECTED = {
 3: ((3,6,12,24),(2,4,8),(0,16),8),
 4: ((4,12,32,32),(3,9,23),(0,9),7),
 5: ((5,20,60,40),(4,16,35),(9,5),5),
 6: ((6,30,72,48),(5,25,42),(5,6),6),
}

def simplices(n, cutoff):
    distance=lambda a,b:min((a-b)%n,(b-a)%n)
    answer=[]
    for k in range(cutoff+1):
        answer.append([s for s in product(range(n), repeat=k+1)
           if all(s[i]!=s[i+1] for i in range(k))
           and sum(distance(s[i],s[i+1]) for i in range(k))<=cutoff])
    return answer

def chain(n, cutoff):
    b=simplices(n,cutoff)
    d=[]
    for k in range(1,cutoff+1):
        r={s:i for i,s in enumerate(b[k-1])}
        matrix=Matrix.zeros(len(b[k-1]),len(b[k]))
        for j,s in enumerate(b[k]):
            for i in range(k+1):
                face=s[:i]+s[i+1:]
                if any(face[t]==face[t+1] for t in range(k-1)):
                    continue  # degenerate face is zero in normalized chains
                matrix[r[face],j]+=(-1)**i
        d.append(matrix)
    return b,d

def unit_smith_rank(M):
    diag=smith_normal_form(M,domain=ZZ)
    vals=[abs(int(diag[i,i])) for i in range(min(diag.rows,diag.cols)) if diag[i,i]]
    assert all(t==1 for t in vals), 'non-unit Smith invariant: '+str(vals)
    return len(vals)

def assert_zero_composition(ds):
    for k in range(len(ds)-1):
        assert ds[k]*ds[k+1] == Matrix.zeros(ds[k].rows,ds[k+1].cols)

def inclusion_h2_rank(s2,d2,s3,d3):
    src_cycles=d2[1].nullspace()  # integral free-space generators over Q
    coordinates={s:i for i,s in enumerate(s3[2])}
    image=Matrix.zeros(len(s3[2]),len(src_cycles))
    for col,z in enumerate(src_cycles):
        for row,s in enumerate(s2[2]):
            image[coordinates[s],col]=z[row]
    assert d3[1]*image==Matrix.zeros(d3[1].rows,image.cols)
    return d3[2].row_join(image).rank()-d3[2].rank()

def verify():
    for n in range(3,7):
        b,d=chain(n,3)
        assert_zero_composition(d)
        ns=tuple(map(len,b))
        ranks=tuple(unit_smith_rank(m) for m in d)
        bh2=ns[2]-ranks[1]-ranks[2]
        bh3=ns[3]-ranks[2]
        bh1=ns[1]-ranks[0]-ranks[1]
        assert (ns,ranks,(bh2,bh3))==EXPECTED[n][:3], (n,ns,ranks,bh2,bh3)
        assert bh1==0
        a,da=chain(n,2)
        assert_zero_composition(da)
        aranks=tuple(unit_smith_rank(m) for m in da)
        initial_h1=len(a[1])-aranks[0]-aranks[1]
        initial_h2=len(a[2])-aranks[1]
        assert initial_h2==EXPECTED[n][3]
        image_rank=inclusion_h2_rank(a,da,b,d)
        assert image_rank==0, (n,image_rank)
        print(f'C{n}: cell_counts={ns}, boundary_ranks={ranks}, '
              f'H2={bh2}, H3={bh3}; cutoff2_H1={initial_h1}, '
              f'cutoff2_H2={initial_h2}, inclusion_H2_rank={image_rank}; '
              'd_squared=0, all_Smith_invariants=1')
    print('VERIFIED: all four integer chain complexes and integral inclusion maps')

if __name__=='__main__':
    verify()
