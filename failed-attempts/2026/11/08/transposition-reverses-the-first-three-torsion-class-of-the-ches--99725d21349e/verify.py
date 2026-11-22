"""Exact finite-field certificate for the 5x5 chessboard complex.

Python 3 stdlib only. A 60-term 3-chain certificate is stored separately.
"""
import itertools
import json
from pathlib import Path

P = 3
N = 5
faces = {
    d: [tuple(zip(rows, cols)) for rows in itertools.combinations(range(N), d)
        for cols in itertools.permutations(range(N), d)]
    for d in range(1, N + 1)
}
lookup = {d: {f: j for j, f in enumerate(faces[d])} for d in faces}


def add(a, b, factor=1):
    out = dict(a)
    for k, v in b.items():
        w = (out.get(k, 0) + factor * v) % P
        if w: out[k] = w
        else: out.pop(k, None)
    return out


def differential(face):
    d = len(face)
    if d == 1: return {0: 1}
    return {lookup[d-1][face[:j] + face[j+1:]]: (1 if j % 2 == 0 else 2)
            for j in range(d)}


def basis_for_columns(d):
    basis = {}
    for face in faces[d]:
        v = differential(face)
        while v and min(v) in basis:
            pivot = min(v)
            v = add(v, basis[pivot], -v[pivot])
        if v:
            pivot = min(v)
            inv = pow(v[pivot], -1, P)
            basis[pivot] = {i: c*inv % P for i,c in v.items()}
    return basis


def reduce(v,basis):
    v = dict(v)
    while v and min(v) in basis:
        pivot = min(v)
        v = add(v,basis[pivot],-v[pivot])
    return v


def wedge(a,b):
    out={}
    for x,s in a.items():
        for y,t in b.items():
            u=x+y
            sign=(-1)**sum(u[i]>u[j] for i in range(len(u)) for j in range(i+1,len(u)))
            f=tuple(sorted(u))
            out[f]=(out.get(f,0)+s*t*sign)%P
    return {f:s for f,s in out.items() if s}


def difference(a,b): return {(a,):1,(b,):2}

z=wedge(wedge(difference((0,0),(1,0)),difference((2,1),(3,1))), difference((4,2),(4,3)))


def transform(chain, kind):
    out = {}
    for face,s in chain.items():
        if kind=='row': u=tuple((1-r if r in (0,1) else r,c) for r,c in face)
        elif kind=='col': u=tuple((r,5-c if c in (2,3) else c) for r,c in face)
        elif kind=='transpose': u=tuple((c,r) for r,c in face)
        else: raise ValueError(kind)
        parity=sum(u[i]>u[j] for i in range(len(u)) for j in range(i+1,len(u))) % 2
        f=tuple(sorted(u));out[f]=(out.get(f,0)+s*(-1)**parity)%P
    return {f:s for f,s in out.items() if s}


def coordinate(chain): return {lookup[3][f]:s for f,s in chain.items()}


def chain_boundary(chain,dimension):
    out={}
    for col,coeff in chain.items():
        out=add(out,differential(faces[dimension][col]),coeff)
    return out


def main():
    base=Path(__file__).resolve().parent
    certificate=json.loads((base/'certificate.json').read_text(encoding='utf-8'))
    assert certificate['field']=='F3'
    assert certificate['face_indexing']=='lexicographic row-combination then column-permutation'
    assert {d:len(faces[d]) for d in faces}=={1:25,2:200,3:600,4:600,5:120}
    B2=basis_for_columns(2)
    B3=basis_for_columns(3)
    assert len(B2)==24 # d1: 25 vertices, 200 edges
    # Here B2 is d1, and B3 is d2 (600 triangles -> 200 edges).
    assert len(B3)==176
    B4=basis_for_columns(4)
    assert len(B4)==423
    assert len(faces[3])-len(B3)-len(B4)==1
    assert len(z)==8
    z_vec=coordinate(z)
    assert not chain_boundary(z_vec,3)
    assert reduce(z_vec,B4) # nonboundary
    tz_vec=coordinate(transform(z,'transpose'))
    assert reduce(add(tz_vec,z_vec,-1),B4) # not +1
    assert not reduce(add(tz_vec,z_vec,1),B4) # -1
    for kind in ('row','col'):
        g=coordinate(transform(z,kind))
        assert not reduce(add(g,z_vec,1),B4)
        assert reduce(add(g,z_vec,-1),B4)
    chain={int(i):int(c) for i,c in certificate['chain_3_indices_coefficients']}
    assert len(chain)==certificate['nonzero_terms']==60
    assert all(0<=i<len(faces[4]) and c in (1,2) for i,c in chain.items())
    assert chain_boundary(chain,4)==add(tz_vec,z_vec,1)
    assert not chain_boundary(chain_boundary(chain,4),3)
    print('ALL_VERIFY_OK faces=25,200,600,600,120 boundary_ranks=24,176,423 mod3_H2=1 z_nonzero=1 transpose=-1 rows=-1 cols=-1 chain3_certificate=60')

if __name__ == '__main__': main()
