#!/usr/bin/env python3
"""Independent finite checks for three-by-n categorical-product general-position complexes.

No mathematical generalization is inferred from finite tests: the all-n theorem
requires the accompanying topological proof.
"""
from collections import defaultdict, deque
from itertools import combinations, permutations
from math import comb


def faces_from_shape_classification(n):
    cell = lambda r, c: 1 << (r*n+c)
    facets = []
    for r in range(3):
        facets.append(sum(cell(r, c) for c in range(n)))
    for c in range(n):
        facets.append(sum(cell(r, c) for r in range(3)))
    for rows in combinations(range(3), 2):
        for cols in combinations(range(n), 2):
            facets.append(sum(cell(r, c) for r in rows for c in cols))
    for cols in permutations(range(n), 3):
        facets.append(sum(cell(r, cols[r]) for r in range(3)))
    faces = {0}
    for f in facets:
        sub = f
        while sub:
            faces.add(sub)
            sub = (sub-1) & f
    return faces


def distances(n):
    N=3*n
    adj=[[] for _ in range(N)]
    for v in range(N):
        for w in range(N):
            if v//n != w//n and v%n != w%n:
                adj[v].append(w)
    d=[]
    for v in range(N):
        dd=[N+1]*N
        dd[v]=0
        q=deque([v])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if dd[y]>dd[x]+1:
                    dd[y]=dd[x]+1
                    q.append(y)
        assert max(dd)==2
        d.append(dd)
    return d


def faces_from_graph(n):
    N=3*n
    d=distances(n)
    forbidden=[]
    for a,b,c in combinations(range(N),3):
        if (d[a][b]+d[b][c]==d[a][c] or
            d[b][a]+d[a][c]==d[b][c] or
            d[a][c]+d[c][b]==d[a][b]):
            forbidden.append((1<<a)|(1<<b)|(1<<c))
    # Direct graph-distance interpretation, not the shape classification.
    valid=bytearray(1<<N)
    valid[0]=1
    for mask in range(1,1<<N):
        v=(mask&-mask).bit_length()-1
        rest=mask^(1<<v)
        if not valid[rest]:
            continue
        valid[mask]=int(not any((mask&t)==t for t in forbidden if t&(1<<v)))
    return {i for i,b in enumerate(valid) if b}


def free_collapses(n, faces):
    active=set(faces)
    cell=lambda r,c:1<<(r*n+c)
    checks=0
    # Inside each row, pair all faces not containing the anchor column 0
    # with their coface containing it, in decreasing number of cells.
    for r in range(3):
        for size in range(n-1,2,-1):
            for cols in combinations(range(1,n),size):
                low=sum(cell(r,c) for c in cols)
                high=low|cell(r,0)
                assert low in active and high in active
                for v in range(3*n):
                    w=low|(1<<v)
                    if w!=low and w in active:
                        assert w==high, (n,r,size,low,w,high)
                active.remove(low)
                active.remove(high)
                checks+=1
    # Every rectangle's lower-left three-corner face is a free codim-1 face.
    for rows in combinations(range(3),2):
        for cols in combinations(range(n),2):
            high=sum(cell(r,c) for r in rows for c in cols)
            low=high^cell(rows[1],cols[1])
            assert low in active and high in active
            for v in range(3*n):
                w=low|(1<<v)
                if w!=low and w in active:
                    assert w==high, (n,rows,cols,low,w,high)
            active.remove(low)
            active.remove(high)
            checks+=1
    assert max(k.bit_count() for k in active)==3
    return checks,len(active)


def triangle_fill_checks(n, faces):
    # Every forbidden triangle has a 5-triangle nullhomotopy disk.
    d=distances(n)
    cell=lambda r,c:1<<(r*n+c)
    checked=0
    for a,b,c in combinations(range(3*n),3):
        mask=(1<<a)|(1<<b)|(1<<c)
        if mask in faces:
            continue
        verts=[(v//n,v%n) for v in (a,b,c)]
        disk=None
        for x,y,z in permutations(verts,3):
            if x[0]==y[0] and x[1]!=y[1] and z[0]!=x[0] and z[1] not in (x[1],y[1]):
                A=cell(*x);B=cell(*y);C=cell(*z)
                X=cell(z[0],x[1]);Y=cell(z[0],y[1])
                disk=[A|B|X, B|X|Y, B|Y|C, X|Y|C, A|X|C]
                break
            if x[1]==y[1] and x[0]!=y[0] and z[1]!=x[1] and z[0] not in (x[0],y[0]):
                # transpose rows and columns; same five triangles.
                A=cell(*x);B=cell(*y);C=cell(*z)
                X=cell(x[0],z[1]);Y=cell(y[0],z[1])
                disk=[A|B|X, B|X|Y, B|Y|C, X|Y|C, A|X|C]
                break
        assert disk is not None, (n,verts)
        assert all(t in faces for t in disk), (n,verts)
        edge_parity={}
        for t in disk:
            bits=[i for i in range(3*n) if t>>i&1]
            for e in combinations(bits,2):
                v=sum(1<<i for i in e)
                edge_parity[v]=edge_parity.get(v,0)^1
        expected={(1<<a)|(1<<b),(1<<a)|(1<<c),(1<<b)|(1<<c)}
        assert {k for k,v in edge_parity.items() if v}==expected
        checked+=1
    return checked


def gf2_rank(cols):
    piv={}
    for col in cols:
        while col:
            p=col.bit_length()-1
            if p in piv: col^=piv[p]
            else: piv[p]=col;break
    return len(piv)


def ranks_mod2(faces,n):
    dims=defaultdict(list)
    for face in faces:
        if face:dims[face.bit_count()-1].append(face)
    boundaries={0:0}
    for k in range(1,max(dims)+1):
        index={face:i for i,face in enumerate(dims[k-1])}
        cols=[]
        for face in dims[k]:
            col=0
            bits=face
            while bits:
                b=bits&-bits
                bits^=b
                col^=1<<index[face^b]
            cols.append(col)
        boundaries[k]=gf2_rank(cols)
    return {k:len(v)-boundaries.get(k,0)-boundaries.get(k+1,0)-(1 if k==0 else 0) for k,v in dims.items()}


def main():
    for n in range(3,9):
        F=faces_from_shape_classification(n)
        if n<=6:
            graph_faces=faces_from_graph(n)
            assert graph_faces==F,(n,len(graph_faces),len(F),len(graph_faces^F))
        triangles=triangle_fill_checks(n,F)
        pairs,remaining=free_collapses(n,F)
        f=defaultdict(int)
        for mask in F:
            if mask:f[mask.bit_count()-1]+=1
        beta=(2*n**3-3*n*n-3*n+4)//2
        euler=sum((-1)**k*count for k,count in f.items())
        assert euler==1+beta
        hom=ranks_mod2(F,n)
        assert hom.get(2)==beta and all(x==0 for k,x in hom.items() if k!=2), (n,hom,beta)
        print(f'n={n}: faces={len(F)-1}; collapse_pairs={pairs}; remaining={remaining-1}; '
              f'missing_triangle_disks={triangles}; H2_rank={beta}; '
              f'geodesic_check={"passed" if n<=6 else "not_run"}; F2_homology=passed')
    print('ALL CHECKS PASSED')

if __name__=='__main__': main()
