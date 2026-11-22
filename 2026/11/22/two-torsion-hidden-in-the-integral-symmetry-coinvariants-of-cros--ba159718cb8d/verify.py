#!/usr/bin/env python3
"""Independent finite combinatorial and integral coinvariant checks.

Standard-library graph construction; SymPy only for independent integer Smith form.
"""
from itertools import combinations, product
from math import comb
from collections import defaultdict, deque
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def signed_flip_action_matrix(r, coord):
    q=1<<r
    b=[i for i in range(1,q)]
    n=(q-1)**2
    cols=[]
    for i in b:
        for j in b:
            v=[0]*n
            mask=1<<coord
            if coord<r:
                a=i ^ mask; a0=mask; c=j; c0=0
            else:
                a=i; a0=0; c=j ^ (1 << (coord-r)); c0=(1 << (coord-r))
            # (e_a-e_a0) tensor (e_c-e_c0), expressed in basis e_i-e_0
            left={a:1,a0:-1};right={c:1,c0:-1}
            for x,sx in left.items():
                if x==0:continue
                for y,sy in right.items():
                    if y==0:continue
                    v[(x-1)*(q-1)+(y-1)]+=sx*sy
            cols.append(v)
    return Matrix(n,n,lambda x,y:cols[y][x])


def check_r(r):
    q=1<<r; k=comb(2*r,r)//2
    # Complete direct face construction from disjoint r-element subsets.
    supports=list(combinations(range(2*r),r))
    vertices=[]
    for I in supports:
        for vals in product((0,1),repeat=r):
            vertices.append((I,vals))
    by_support=defaultdict(list)
    for z,(I,v) in enumerate(vertices):by_support[I].append(z)
    adjacency=[set() for _ in vertices]
    edges=0
    for I in supports:
        J=tuple(x for x in range(2*r) if x not in I)
        if I<J:
            for a in by_support[I]:
                for b in by_support[J]:
                    adjacency[a].add(b);adjacency[b].add(a);edges+=1
    seen=set(); components=[]
    for i in range(len(vertices)):
        if i in seen:continue
        todo=[i]; seen.add(i);comp=[]
        while todo:
            j=todo.pop();comp.append(j)
            for v in adjacency[j]:
                if v not in seen:seen.add(v);todo.append(v)
        components.append(comp)
    assert len(components)==k
    assert sorted(len(c) for c in components)==[2*q]*k
    assert edges==k*q*q
    b1=edges-len(vertices)+len(components)
    assert b1==k*(q-1)**2
    # Explicit bipartite cycle generators, each a four-cycle.
    I=supports[0];J=tuple(x for x in range(2*r) if x not in I)
    left=by_support[I];right=by_support[J]
    cycles=[((left[i],right[j]),(left[i],right[0]),(left[0],right[j]),(left[0],right[0])) for i in range(1,q) for j in range(1,q)]
    for cyclic in cycles:
        assert all(b in adjacency[a] for a,b in cyclic)
    # Coordinate flips induce integer matrices on the explicit cycle basis.
    # The relations (flip-1) span the integral coinvariant quotient.
    n=(q-1)**2
    rel=Matrix.hstack(*(signed_flip_action_matrix(r,i)-Matrix.eye(n) for i in range(2*r)))
    d=smith_normal_form(rel,domain=ZZ)
    diagonal=[abs(int(d[i,i])) for i in range(min(d.shape))]
    assert diagonal.count(2)==r*r,(r,diagonal)
    assert all(x in (1,2) for x in diagonal),(r,diagonal)
    assert len(diagonal)==n
    print(f'r={r} components={k} vertices={len(vertices)} edges={edges} b1={b1} component_torsion_2rank={diagonal.count(2)} total_coinvariant_2rank={k*r*r}')


def check_full_hyperoctahedral_coinvariants(r):
    if r != 2:
        return
    # Directly construct the full 27-dimensional integral cycle representation.
    import itertools
    supports=list(itertools.combinations(range(2*r),r))
    parts=[(I,tuple(x for x in range(2*r) if x not in I)) for I in supports
           if I<tuple(x for x in range(2*r) if x not in I)]
    q=1<<r
    b=(q-1)**2
    pairs={(I,J):k for k,(I,J) in enumerate(parts)}
    N=len(parts)*b
    def bitmap_perm(x,I,pi):
        src={c:(x>>p)&1 for p,c in enumerate(I)}
        dest=sorted(pi[c] for c in I)
        return sum(src[pi.index(c)]<<p for p,c in enumerate(dest))
    def action(pi):
        M=Matrix.zeros(N,N)
        for k,(I,J) in enumerate(parts):
            A=tuple(sorted(pi[c] for c in I));B=tuple(sorted(pi[c] for c in J))
            swapped=A>B
            out=(B,A) if swapped else (A,B)
            t=pairs[out]
            for i in range(1,q):
                for j in range(1,q):
                    li=bitmap_perm(i,I,pi);rj=bitmap_perm(j,J,pi)
                    if swapped:li,rj=rj,li
                    coef=-1 if swapped else 1
                    if li and rj:
                        M[t*b+(li-1)*(q-1)+(rj-1),k*b+(i-1)*(q-1)+(j-1)]+=coef
        return M
    rel=[]
    # Each flip acts only on its own component, mapped to local coordinates there.
    for coord in range(2*r):
        F=Matrix.zeros(N,N)
        for k,(I,J) in enumerate(parts):
            if coord in I:local=I.index(coord)
            else:local=r+J.index(coord)
            B=signed_flip_action_matrix(r,local)
            for x in range(b):
                for y in range(b):F[k*b+x,k*b+y]=B[x,y]
        rel.append(F-Matrix.eye(N))
    for i in range(2*r-1):
        pi=list(range(2*r));pi[i],pi[i+1]=pi[i+1],pi[i]
        rel.append(action(pi)-Matrix.eye(N))
    d=smith_normal_form(Matrix.hstack(*rel),domain=ZZ)
    diag=[abs(int(d[i,i])) for i in range(N)]
    assert diag.count(2)==1 and all(x in (1,2) for x in diag),diag
    print(f'full_signed_permutation_coinvariants_r=2: Z/2 (Smith 1^{diag.count(1)}, 2^{diag.count(2)})')


if __name__=='__main__':
    check_r(2)
    check_r(3)
    check_full_hyperoctahedral_coinvariants(2)
    print('ALL_TESTS_PASS')
