#!/usr/bin/env python3
"""Finite checks for the diagonal-avoiding multiway relational product.
No external research sources or custom dependencies are required.
Run: python check.py
"""
import itertools
from collections import defaultdict
from fractions import Fraction as F


def cells_and_betti(n, r):
    allparts = range(1, 1 << n)
    cells = defaultdict(list)
    for tuple_parts in itertools.product(allparts, repeat=r):
        intersection = (1 << n) - 1
        for part in tuple_parts:
            intersection &= part
        if intersection:
            continue
        degree = sum(p.bit_count()-1 for p in tuple_parts)
        cells[degree].append(tuple_parts)
    ranks = {}
    for d in sorted(cells):
        if d==0:continue
        ind = {x:i for i,x in enumerate(cells[d-1])}
        pivots={}
        for x in cells[d]:
            col=0
            for axis in range(r):
                sub=x[axis]
                if sub.bit_count()==1:continue
                while sub:
                    bit=sub&-sub
                    sub-=bit
                    y=list(x)
                    y[axis] ^=bit
                    col^=1<<ind[tuple(y)]
            while col:
                k=col.bit_length()-1
                if k not in pivots:
                    pivots[k]=col
                    break
                col ^= pivots[k]
        ranks[d]=len(pivots)
    betti={d:len(v)-ranks.get(d,0)-ranks.get(d+1,0) for d,v in cells.items()}
    betti[0]-=1
    positive={d:v for d,v in betti.items() if v}
    expected={(n-1)*(r-1)-1:1}
    assert positive==expected,(n,r,positive,expected)
    return sum(map(len,cells.values())),positive


def permutation_sign(perm):
    return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))


def group_generated(n,r,gens):
    id_=(tuple(range(n)),tuple(range(r)))
    group={id_}
    queue=[id_]
    while queue:
        a,b=queue.pop()
        for c,d in gens:
            v=(tuple(c[a[i]] for i in range(n)),tuple(d[b[j]] for j in range(r)))
            if v not in group:
                group.add(v)
                queue.append(v)
    return group


def orbit_count(points,group,action):
    unseen=set(points)
    count=0
    while unseen:
        start=next(iter(unseen))
        orbit={action(g,start) for g in group}
        assert orbit.issubset(set(points))
        unseen-=orbit
        count+=1
    return count


def group_fixed_orbit_formula(n,r,group):
    nr=orbit_count([(i,j) for i in range(n) for j in range(r)],group,lambda g,p:(g[0][p[0]],g[1][p[1]]))
    nc=orbit_count(range(n),group,lambda g,i:g[0][i])
    rc=orbit_count(range(r),group,lambda g,j:g[1][j])
    return nr-nc-rc+1


def exact_geometry_and_actions(n,r):
    from sympy import Matrix,eye,zeros
    # W has the tensor-augmentation basis (e_i-e_last)⊗(e_j-e_last).
    basis=[]
    for i in range(n-1):
        for j in range(r-1):
            v=[[0 for _ in range(n)] for _ in range(r)]
            for ii,jj,val in ((i,j,1),(n-1,r-1,1),(n-1,j,-1),(i,r-1,-1)):
                v[jj][ii]=val
            basis.append(v)
    dim=len(basis)
    pn=tuple(list(range(1,n))+[0]); pr=tuple(list(range(1,r))+[0])
    gens=[(pn,tuple(range(r))),(tuple(range(n)),pr),
          (tuple([1,0]+list(range(2,n))),tuple(range(r))),
          (tuple(range(n)),tuple([1,0]+list(range(2,r))))]
    matrices=[]
    for a,b in gens:
        cols=[]
        for x in basis:
            y=[[0]*n for _ in range(r)]
            for j in range(r):
                for i in range(n): y[b[j]][a[i]]=x[j][i]
            cols.append([y[j][i] for i in range(n-1) for j in range(r-1)])
        M=Matrix.hstack(*[Matrix(c) for c in cols])
        assert M.det()==permutation_sign(a)**(r-1)*permutation_sign(b)**(n-1)
        matrices.append(M)
    samples=[]
    idn=tuple(range(n));idr=tuple(range(r))
    samples.append([])
    samples.append([gens[2]])
    samples.append([gens[3]])
    samples.append([gens[2],gens[3]])
    samples.append(gens)
    samples.append([gens[0],gens[1]])
    samples.append([(gens[2][0],gens[3][1])])
    checks=0
    for subgens in samples:
        gp=group_generated(n,r,subgens)
        formula=group_fixed_orbit_formula(n,r,gp)
        matrices_sub=[]
        for a,b in subgens:
            cols=[]
            for x in basis:
                y=[[0]*n for _ in range(r)]
                for j in range(r):
                    for i in range(n): y[b[j]][a[i]]=x[j][i]
                cols.append([y[j][i] for i in range(n-1) for j in range(r-1)])
            matrices_sub.append(Matrix.hstack(*[Matrix(c) for c in cols]))
        fixed=dim-(Matrix.vstack(*[M-eye(dim) for M in matrices_sub]).rank() if matrices_sub else 0)
        assert fixed==formula,(n,r,subgens,formula,fixed)
        checks+=1
    # A nontrivial exact point in W and its inverse, plus symmetry invariance.
    raw=[[F((2*j+1)*(i+1)+((i+j)%3),1) for i in range(n)] for j in range(r)]
    row_means=[sum(row,F(0))/n for row in raw]
    centered=[[raw[j][i]-row_means[j] for i in range(n)] for j in range(r)]
    col_means=[sum(centered[j][i] for j in range(r))/r for i in range(n)]
    z=[[centered[j][i]-col_means[i] for i in range(n)] for j in range(r)]
    f=-sum(min(z[j][i] for j in range(r)) for i in range(n))
    assert f>0
    z=[[v/f for v in row] for row in z]
    x=[[z[j][i]-min(z[k][i] for k in range(r)) for i in range(n)] for j in range(r)]
    assert all(sum(row)==1 and all(t>=0 for t in row) for row in x)
    assert all(min(x[j][i] for j in range(r))==0 for i in range(n))
    mean=[sum(x[j][i] for j in range(r))/r for i in range(n)]
    assert [[x[j][i]-mean[i] for i in range(n)] for j in range(r)] == z
    for a,b in gens:
        y=[[F(0) for _ in range(n)] for _ in range(r)]
        for j in range(r):
            for i in range(n):y[b[j]][a[i]]=x[j][i]
        assert all(sum(row)==1 and all(t>=0 for t in row) for row in y)
        assert all(min(y[j][i] for j in range(r))==0 for i in range(n))
    return checks,len(gens)


if __name__=='__main__':
    cases=[(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3)]
    total=0
    for n,r in cases:
        count,betti=cells_and_betti(n,r)
        total+=count
        print('cell_homology n=%s r=%s cells=%s betti=%s PASS'%(n,r,count,betti))
    fixed=det=0
    for n,r in [(2,3),(3,3),(3,4),(4,3)]:
        x,y=exact_geometry_and_actions(n,r)
        fixed+=x;det+=y
        print('symmetry n=%s r=%s subgroup_tests=%s generators=%s PASS'%(n,r,x,y))
    print('DIAGONAL_DOWKER_CHECK_PASS cases=%s cells=%s subgroup_tests=%s determinant_tests=%s'%(len(cases),total,fixed,det))
