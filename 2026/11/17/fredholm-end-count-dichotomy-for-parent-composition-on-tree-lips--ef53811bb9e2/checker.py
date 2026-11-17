"""Finite reproducibility checks for tree parent-shift identities.

Finite checks are not substitutes for the infinite-dimensional proof.
"""
from fractions import Fraction
import cmath


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        piv = next((i for i in range(r,len(a)) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv] = a[piv],a[r]
        z = a[r][c]
        a[r] = [v/z for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x-z*y for x,y in zip(a[i],a[r])]
        r += 1
    return r


def levels(degrees, depth):
    vertices=[(0,-1)]
    fronts=[0]
    for n in range(depth):
        nxt=[]
        for u in fronts:
            for j in range(degrees.get(u,1)):
                v=len(vertices)
                vertices.append((n+1,u))
                nxt.append(v)
        fronts=nxt
    return vertices,fronts


def test_tree(degrees, depth):
    vertices, leaves = levels(degrees,depth)
    # Parent duplication on edge coordinates of the truncated tree.
    m=len(vertices)-1
    M=[[0]*m for _ in range(m)]
    for v in range(1,len(vertices)):
        p=vertices[v][1]
        if p>0:M[v-1][p-1]=1
    rank_d=rank(M)
    # At a finite cutoff, the rank deficiency equals number of depth-(depth-1)
    # vertices plus contributions from early branching: all leaves of truncated tree.
    all_parents={vertices[v][1] for v in range(1,len(vertices))}
    terminal=[v for v in range(len(vertices)) if v not in all_parents]
    # Rank D equals number of nonroot vertices having children.
    assert rank_d==sum(v>0 and v in all_parents for v in range(len(vertices)))
    assert m-rank_d==len(terminal)
    return m


if __name__=='__main__':
    cases=0
    for d in range(2,9):
        for profile in ({},{0:2},{0:3,1:2},{0:2,1:2,3:2},{0:2,1:3,2:2}):
            test_tree(profile,d);cases+=1
    for lam in (0, Fraction(1,3),Fraction(-2,5),Fraction(3,4)):
        for length in range(2,40):
            # h0(Dg)=0, h_j(Dg)=h_{j-1}(g); finite supported h
            h=[Fraction((j*7+3)%13-6) for j in range(length)]
            L=sum(lam**j*h[j] for j in range(length))
            DL=sum(lam**j*h[j-1] for j in range(1,length+1))
            assert DL==lam*L
            cases+=1
    for N in range(2,70):
        h=[max(0,min(n/N,(2*N-n)/N)) for n in range(2*N+2)]
        assert max(abs(h[n-1]-h[n]) for n in range(1,len(h)))<=1/N+1e-12
        assert max(h)==1.0
        cases+=1
    print('PASS finite consistency cases:',cases)
