"""Independent finite checks of cyclic simplex-skeleton orbit cell complexes.
Python 3 and SymPy (used only for finite Smith normal forms)."""
from itertools import combinations
from math import comb, gcd
from collections import deque
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def cells_and_boundaries(n):
    faces = [tuple(s) for k in (1, 2, 3) for s in combinations(range(n), k)]
    indices = {f:i for i, f in enumerate(faces)}
    sizes = [len(f) for f in faces]
    imap = [indices[tuple(sorted((x+1)%n for x in f))] for f in faces]
    flags = [[(i,) for i in range(len(faces))], [], []]
    for a in range(len(faces)):
        A = set(faces[a]); sa=sizes[a]
        for b in range(len(faces)):
            if sa < sizes[b] and A.issubset(faces[b]):
                flags[1].append((a,b))
                if sa==1 and sizes[b]==2:
                    for c in range(len(faces)):
                        if sizes[c]==3 and set(faces[b]).issubset(faces[c]):
                            flags[2].append((a,b,c))
    def canonical(flag):
        best=flag; current=flag
        for _ in range(1,n):
            current=tuple(imap[i] for i in current)
            if current < best:best=current
        return best
    cells=[sorted({canonical(f) for f in layer}) for layer in flags]
    lookup=[{f:i for i,f in enumerate(layer)} for layer in cells]
    mats=[]
    for d in (1,2):
        mat=[[0]*len(cells[d]) for _ in cells[d-1]]
        for j,flag in enumerate(cells[d]):
            for k in range(d+1):
                i=lookup[d-1][canonical(flag[:k]+flag[k+1:])]
                mat[i][j]+=(-1)**k
        mats.append(mat)
    return cells,mats


def edge_tree_reduced_relators(cells, matrices):
    b1,b2=matrices
    vertices=len(cells[0]); edges=len(cells[1]); faces=len(cells[2]);adj=[[] for _ in range(vertices)]
    for j in range(edges):
        ends=[i for i in range(vertices) if b1[i][j]]
        assert len(ends)==2 and set(b1[i][j] for i in ends)=={-1,1}
        for i in ends:adj[i].append((j,ends[1] if ends[0]==i else ends[0]))
    tree=set();seen={0};q=deque([0]);
    while q:
        v=q.popleft()
        for e,w in adj[v]:
            if w not in seen:seen.add(w);q.append(w);tree.add(e)
    assert len(seen)==vertices and len(tree)==vertices-1
    non_tree=[j for j in range(edges) if j not in tree]
    # For an abelian presentation with a spanning tree contracted, each 2-cell
    # boundary yields exactly its non-tree edge coordinates.
    return Matrix([[b2[e][j] for j in range(faces)] for e in non_tree])


def check(n):
    cells,b= cells_and_boundaries(n)
    b1,b2 = map(Matrix,b)
    assert b1*b2==Matrix.zeros(b1.rows,b2.cols)
    chi=sum((-1)**i*len(cells[i]) for i in range(3))
    expected=(n*n-6*n+11)//6 if n%6 in (1,5) else None
    assert 6*chi==n*n-6*n+11+3*(n%2==0)+4*(n%3==0)
    rel=edge_tree_reduced_relators(cells,(b1.tolist(),b2.tolist()))
    if n<=9:
        sm=smith_normal_form(rel,domain=ZZ)
        diags=[abs(int(sm[i,i])) for i in range(min(sm.shape)) if sm[i,i]!=0]
        predicted=n//gcd(n,6)
        nz=[d for d in diags if d>1]
        assert nz == ([] if predicted==1 else [predicted]), (n,nz,predicted)
        assert len(cells[2])-len(diags)==chi-1
    print(f'n={n}; orbit cells={tuple(map(len,cells))}; Euler={chi}; expected pi1=C_{n//gcd(n,6)}, H2 rank={chi-1}',flush=True)

if __name__=='__main__':
    for n in (5,6,7,8,9,10,12):check(n)
    print('CYCLIC_KNESER_SINGULAR_QUOTIENT_CHECKS_OK')
