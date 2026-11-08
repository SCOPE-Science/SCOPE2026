#!/usr/bin/env python3
"""Reproduce face counts and mod-two homology of small bilinear-forms triangle complexes.

Uses independent matrix-rank adjacency enumeration, triangle intersection enumeration,
and sparse binary boundary reduction; no precomputed graph tables.
"""
from itertools import product

def rank_one(entries, rows, cols, prime):
    mat = [entries[i*cols:(i+1)*cols] for i in range(rows)]
    pivot_row = next((r for r in mat if any(r)), None)
    if pivot_row is None:
        return False
    j = next(j for j,z in enumerate(pivot_row) if z)
    inv = pow(pivot_row[j],-1,prime)
    for r in mat:
        scalar = r[j]*inv % prime
        if any((r[k]-scalar*pivot_row[k])%prime for k in range(cols)):
            return False
    return True

def reduce_binary(columns):
    pivots = {}
    for v in columns:
        while v:
            j = v.bit_length()-1
            if j in pivots:
                v ^= pivots[j]
            else:
                pivots[j] = v
                break
    return len(pivots)

def verify(rows,cols,prime):
    verts=list(product(range(prime),repeat=rows*cols))
    V=len(verts)
    rank_one_diffs = {
        d for d in verts if rank_one(d,rows,cols,prime)
    }
    neighbors = [set() for _ in range(V)]
    lookup={v:i for i,v in enumerate(verts)}
    for i,v in enumerate(verts):
        for d in rank_one_diffs:
            w=tuple((x+y)%prime for x,y in zip(v,d))
            j=lookup[w]
            if i!=j: neighbors[i].add(j)
    edges=[(i,j) for i in range(V) for j in neighbors[i] if i<j]
    edge_idx={e:k for k,e in enumerate(edges)}
    triangles=[]
    for i,j in edges:
        for k in neighbors[i]&neighbors[j]:
            if k>j: triangles.append((i,j,k))
    de=(prime**rows-1)*(prime**cols-1)//(prime-1)
    common=prime**rows+prime**cols-prime-2
    assert len(edges)==V*de//2
    assert len(triangles)==V*de*common//6
    columns=(
        (1<<edge_idx[i,j])^(1<<edge_idx[i,k])^(1<<edge_idx[j,k])
        for i,j,k in triangles
    )
    rank_boundary_2=reduce_binary(columns)
    betti_1=len(edges)-(V-1)-rank_boundary_2
    beta_2=len(triangles)-rank_boundary_2
    expected_beta_2=V-len(edges)+len(triangles)-1
    assert betti_1==0
    assert beta_2==expected_beta_2
    print(f'q={prime} a={rows} b={cols}: V={V} E={len(edges)} T={len(triangles)} rank_d2_F2={rank_boundary_2} beta1_F2={betti_1} beta2_F2={beta_2}')

def main():
    for params in [(2,2,2),(2,3,2),(3,3,2),(2,2,3)]: verify(*params)
    print('BILINEAR_TRIANGLE_CHECKS_OK')
if __name__=='__main__':main()
