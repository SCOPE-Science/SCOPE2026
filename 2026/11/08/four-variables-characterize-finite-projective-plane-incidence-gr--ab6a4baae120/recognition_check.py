#!/usr/bin/env python3
"""Finite checks of the four-variable projective-plane Levi-graph criterion."""
from itertools import product

def cyclic_fano(complement=False):
    blocks = [{(t+d)%7 for d in (0,1,3)} for t in range(7)]
    if complement:
        blocks = [set(range(7))-b for b in blocks]
    return levi(7, blocks)

def levi(n_points, blocks):
    n=n_points+len(blocks)
    adj=[[False]*n for _ in range(n)]
    for j,b in enumerate(blocks):
        for i in b:
            adj[i][n_points+j]=adj[n_points+j][i]=True
    return adj

def pg_2_3():
    def norm(a):
        m=next(v for v in a if v)
        inv=1 if m==1 else 2
        return tuple((inv*v)%3 for v in a)
    vectors=sorted({norm(a) for a in product(range(3),repeat=3) if any(a)})
    assert len(vectors)==13
    blocks=[{i for i,p in enumerate(vectors) if sum(x*y for x,y in zip(p,l))%3==0} for l in vectors]
    return levi(len(vectors),blocks)

def recognizes(adj):
    n=len(adj)
    if not n or any(adj[x][x] for x in range(n)): return False
    if any(adj[x][y]!=adj[y][x] for x in range(n) for y in range(n)):return False
    common=[[sum(adj[x][z] and adj[y][z] for z in range(n)) for y in range(n)] for x in range(n)]
    S=[[x==y or common[x][y]>0 for y in range(n)] for x in range(n)]
    # The six defining clauses, in their order in the written result:
    if not any(not S[x][y] for x in range(n) for y in range(n)): return False
    if any(S[x][y] and S[y][z] and not S[x][z] for x in range(n) for y in range(n) for z in range(n)): return False
    if any(not S[x][y] and not S[x][z] and not S[y][z] for x in range(n) for y in range(n) for z in range(n)): return False
    if any(adj[x][y] and S[x][y] for x in range(n) for y in range(n)):return False
    if any(sum(adj[x])<3 for x in range(n)): return False
    if any(common[x][y]>1 for x in range(n) for y in range(x+1,n)):return False
    return True

fano=cyclic_fano()
complement=cyclic_fano(True)
plane3=pg_2_3()
assert len(fano)==14 and len(complement)==14 and len(plane3)==26
assert recognizes(fano)
assert not recognizes(complement)
assert recognizes(plane3)
for x in range(14):
    for y in range(x+1,14):
        changed=[row[:] for row in fano]
        changed[x][y]=changed[y][x]=not changed[x][y]
        assert not recognizes(changed)
print('FANO_PG(2,2): 14 vertices, 3-regular, recognized')
print('COMPLEMENT_FANO_2-(7,4,2): 14 vertices, 4-regular, rejected')
print('PG(2,3): 26 vertices, 4-regular, recognized')
print('SINGLE_EDGE_PERTURBATIONS_FANO: 91/91 rejected')
print('RECOGNITION_CHECK_PASS')
