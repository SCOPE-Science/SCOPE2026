"""Exact finite checks for coordinate controllability of multipartite line graphs.

Run with Python >=3.9: python verify.py
Uses integer/fraction arithmetic throughout; no external dependencies.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
from random import Random


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    nr, nc = len(a), len(a[0])
    row = 0
    for col in range(nc):
        pivot = next((i for i in range(row, nr) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        p = a[row][col]
        for j in range(col, nc):
            a[row][j] /= p
        for i in range(row + 1, nr):
            p = a[i][col]
            if p:
                for j in range(col, nc):
                    a[i][j] -= p * a[row][j]
        row += 1
        if row == nr:
            break
    return row


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    assert all(len(row)==n for row in a)
    answer = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j]), None)
        if pivot is None: return 0
        if pivot != j:
            a[j],a[pivot]=a[pivot],a[j]
            answer=-answer
        v=a[j][j]
        answer*=v
        for i in range(j+1,n):
            if a[i][j]:
                f=a[i][j]/v
                for h in range(j+1,n): a[i][h]-=f*a[j][h]
                a[i][j]=0
    assert answer.denominator==1
    return int(answer)

def signless_matrix(r,k,edges):
    n=r*k
    q=[[0]*n for _ in range(n)]
    for a,b in edges:
        q[a][a]+=1; q[b][b]+=1
        q[a][b]+=1; q[b][a]+=1
    return q

def data(r,k):
    n=r*k
    parts=[i//k for i in range(n)]
    edges=[(a,b) for a in range(n) for b in range(a+1,n)
           if parts[a]!=parts[b]]
    # Eigenspaces of the signless Laplacian, represented by integer columns.
    within=[]
    for h in range(r):
        for j in range(k-1):
            col=[0]*n
            col[h*k+j]=1
            col[h*k+k-1]=-1
            within.append(col)
    contrast=[]
    for h in range(r-1):
        col=[0]*n
        for j in range(k):
            col[h*k+j]=1
            col[(r-1)*k+j]=-1
        contrast.append(col)
    constant=[[1]*n]
    return edges,[within,contrast,constant]


def col_restriction_rank(edges, chosen, basis):
    if not basis: return 0
    mat=[[x[a]+x[b] for x in basis] for i,(a,b) in enumerate(edges) if i in chosen]
    return rank(mat)


def full_signed_incidence_rank(edges, chosen, n):
    f=[edges[i] for i in chosen]
    return rank([[int(a==v or b==v) for a,b in f] for v in range(n)])


def odd_unicyclic_components(edges, chosen, n):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    for i in chosen:
        a,b=edges[i]
        pa,pb=find(a),find(b)
        if pa!=pb: parent[pa]=pb
    components={}
    for v in range(n): components.setdefault(find(v),[]).append(v)
    edge_sets={z:[] for z in components}
    for i in chosen:
        a,b=edges[i]
        edge_sets[find(a)].append((a,b))
    for root,verts in components.items():
        ev=edge_sets[root]
        if len(ev)!=len(verts): return 0
        adj={v:[] for v in verts}
        for a,b in ev:
            adj[a].append(b); adj[b].append(a)
        colors={verts[0]:0}
        queue=[verts[0]]
        for a in queue:
            for b in adj[a]:
                if b not in colors:
                    colors[b]=1-colors[a]; queue.append(b)
                elif colors[b]==colors[a]:
                    # An odd cycle occurs. The component is unicyclic.
                    break
            else:
                continue
            break
        else:
            return 0
    return len(components)


def test_small():
    r,k=3,2
    edges,bases=data(r,k)
    n=r*k; m=len(edges)
    all_good=[]; candidates=0; exceptions=[]; cdist={}
    for F in combinations(range(m),n):
        F=set(F)
        c=odd_unicyclic_components(edges,F,n)
        # Compare graph-theoretic and exact unsigned-incidence tests.
        rank_condition=(full_signed_incidence_rank(edges,F,n)==n)
        assert bool(c)==rank_condition
        if not c: continue
        candidates+=1
        cdist[c]=cdist.get(c,0)+1
        U=set(range(m))-F
        checks=[col_restriction_rank(edges,U,b) for b in bases]
        required=[len(b) for b in bases]
        if checks==required: all_good.append(F)
        else: exceptions.append((F,c,tuple(checks)))
    assert candidates==500
    assert len(all_good)==496
    assert len(exceptions)==4
    assert cdist=={1:496,2:4}
    assert all(c==2 and fail==(2,2,1) for _,c,fail in exceptions)
    assert sum(4**c*v for c,v in cdist.items())==2048
    for F,_,_ in exceptions:
        # The only failures are partitions into two disjoint triangles.
        assert all(len([j for j in F if v in edges[j]])==2 for v in range(n))
    print('EXHAUSTIVE r=3,k=2: 924 tested; 500 odd-pseudoforests; 496 controllable; 4 excluded.')


def test_samples():
    rng=Random(874321)
    for r,k in [(3,3),(4,2),(4,3),(5,2)]:
        edges,bases=data(r,k)
        n=r*k; m=len(edges)
        tested=0
        # A spanning triangle with a pendant edge to every remaining vertex.
        starters=[0,k,2*k]
        F=[]
        for a,b in combinations(starters,2):
            F.append(edges.index((a,b)))
        for v in range(n):
            if v in starters:continue
            a=next(z for z in starters if z//k!=v//k)
            F.append(edges.index((min(a,v),max(a,v))))
        assert len(F)==n and len(set(F))==n
        assert odd_unicyclic_components(edges,set(F),n)==1
        chosen=set(range(m))-set(F)
        assert all(col_restriction_rank(edges,chosen,b)==len(b) for b in bases)
        for z in range(80):
            FI=set(rng.sample(range(m),n))
            c=odd_unicyclic_components(edges,FI,n)
            assert bool(c)==(full_signed_incidence_rank(edges,FI,n)==n)
            if c:
                chosen=set(range(m))-FI
                assert all(col_restriction_rank(edges,chosen,b)==len(b) for b in bases)
            tested+=1
        d=(r-1)*k
        assert (m-n)>=max(r*(k-1),r-1,1)
        qdet=(2*d)*(d**(r*(k-1)))*(((r-2)*k)**(r-1))
        assert qdet>0
        assert determinant(signless_matrix(r,k,edges))==qdet
        print('CONSTRUCTION/SAMPLES r=%d,k=%d: %d sampled complements; determinant=%d.'%(r,k,tested,qdet))

if __name__=='__main__':
    test_small()
    test_samples()
    print('ALL CHECKS PASSED')
