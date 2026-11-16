#!/usr/bin/env python3
"""Exact, dependency-free Walsh certificate for 3x3 periodic square ice."""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path

SIDE = 3
V = SIDE*SIDE
E = 2*V
SIZE = 1 << E

def vertex(row, col):
    return SIDE*(row%SIDE) + (col%SIDE)

def edges():
    out = []
    for row in range(SIDE):
        for col in range(SIDE):
            u = vertex(row,col)
            out.append((u,vertex(row,col+1))) # east
            out.append((u,vertex(row+1,col))) # south
    assert len(set(tuple(sorted(pair)) for pair in out)) == E
    return out

EDGES=edges()

def balanced_direct(mask):
    degree=[0]*V
    for e,(a,b) in enumerate(EDGES):
        if (mask>>e)&1:
            a,b=b,a
        degree[a]+=1
        degree[b]-=1
    return degree == [0]*V

def from_row_equations():
    # Solve h[r,c]+v[r,c]=h[r,c-1]+v[r-1,c] over the INTEGERS.
    # Choose all vertical edges and h[r,0] for each row; the remaining
    # horizontal edges are forced, subject to {0,1} and cyclic closure.
    ans=set()
    for vert_bits in range(1<<V):
        for seeds in range(1<<SIDE):
            horizontals=[0]*V
            good=True
            for r in range(SIDE):
                horizontals[vertex(r,0)]=(seeds>>r)&1
                for c in range(1,SIDE):
                    ind=vertex(r,c)
                    prev=vertex(r,c-1)
                    up=vertex(r-1,c)
                    h=horizontals[prev]+((vert_bits>>up)&1)-((vert_bits>>ind)&1)
                    if h not in (0,1):
                        good=False
                        break
                    horizontals[ind]=h
                if not good:
                    break
                ind=vertex(r,0)
                prev=vertex(r,SIDE-1)
                up=vertex(r-1,0)
                if horizontals[ind]+((vert_bits>>ind)&1) != horizontals[prev]+((vert_bits>>up)&1):
                    good=False
                    break
            if good:
                mask=0
                for v in range(V):
                    mask |= horizontals[v] << (2*v)
                    mask |= ((vert_bits>>v)&1) << (2*v+1)
                assert mask not in ans
                ans.add(mask)
    return ans

def hadamard(a):
    n=len(a)
    span=1
    while span<n:
        for start in range(0,n,2*span):
            for j in range(start,start+span):
                u=a[j];v=a[j+span]
                a[j]=u+v
                a[j+span]=u-v
        span*=2
    return a

def parity_dot(a,b):
    return (a&b).bit_count()&1

def run():
    direct=set(mask for mask in range(SIZE) if balanced_direct(mask))
    transferred=from_row_equations()
    assert direct==transferred
    assert len(direct)==148
    f=[0]*SIZE
    for mask in direct:
        f[mask]=1
    fourier=hadamard(f)
    hist=Counter(fourier)
    EXPECTED={-40:2304,-28:4608,-16:4608,-12:10752,-8:9984,-4:9216,
              0:162816,4:20736,8:9984,12:13824,16:4608,20:2304,
              40:2304,44:1536,68:2304,148:256}
    assert hist==EXPECTED,(hist,EXPECTED)
    assert sum(n for n in hist.values())==SIZE
    assert sum(v*v*n for v,n in hist.items()) == SIZE*148
    assert len(fourier)-hist[0]==99328
    assert all(v%4==0 for v in fourier)
    assert min(abs(v) for v in fourier if v)==4
    # An independently evaluated Fourier transform on representatives
    # of the quotient by the cut space (2^(V-1) frequencies per class).
    # The 1024 representatives are all submasks of the 10 non-tree edges.
    spanning_tree=set()
    # horizontal edges on rows 0,1,2 between columns 0 and 1 and 1 and 2
    spanning_tree.update(2*vertex(r,c) for r in range(3) for c in range(2))
    # vertical edges linking row0 -> row1 -> row2 in column 0
    spanning_tree.update(2*vertex(r,0)+1 for r in range(2))
    assert len(spanning_tree)==V-1
    remaining=[i for i in range(E) if i not in spanning_tree]
    assert len(remaining)==10
    cert=json.loads((Path(__file__).parent/"SPECTRUM.json").read_text(encoding="utf-8"))
    assert cert["tree_edge_indices"]==sorted(spanning_tree)
    assert cert["non_tree_edge_indices"]==remaining
    assert len(cert["frequency_values"])==1024
    direct_class_spectrum=Counter()
    for s in range(1<<len(remaining)):
        freq=sum(1<<e for k,e in enumerate(remaining) if (s>>k)&1)
        val=sum(1-2*parity_dot(freq,mask) for mask in transferred)
        assert val==fourier[freq]==cert["frequency_values"][s]
        direct_class_spectrum[val]+=1
    assert {val:n*256 for val,n in direct_class_spectrum.items()}==EXPECTED
    # Independent check that each of the 256 spanning-tree frequency
    # flips corresponds to a cut-character coset (with sign allowed).
    for u in range(SIZE):
        if u.bit_count()%2==1:
            assert fourier[u]==0
    extra_zeros=sum(1 for u,x in enumerate(fourier) if u.bit_count()%2==0 and x==0)
    assert extra_zeros==31744
    zero_two=set(u for u,x in enumerate(fourier) if u.bit_count()==2 and x==0)
    disjoint_perpendicular=set()
    for e in range(E):
        for j in range(e+1,E):
            a,b=EDGES[e]
            c,d=EDGES[j]
            if (e%2)!=(j%2) and len({a,b,c,d})==4:
                disjoint_perpendicular.add((1<<e)|(1<<j))
    assert zero_two == disjoint_perpendicular
    assert len(zero_two)==45
    # Unnormalized inverse transform of the nonzero-frequency mask.
    kern=hadamard([int(x!=0) for x in fourier])
    abs_sum=sum(abs(x) for x in kern)
    assert abs_sum==1822720
    assert Fraction(abs_sum,SIZE)==Fraction(445,64)
    assert kern[0]==99328
    print('ICE3_WALSH_EXACT_PASS orientations=148 frequencies=262144 zeros=162816 rank=99328 extra_even_zeros=31744 two_edge_zeros=45 min_nonzero=4 endpoint=445/64')
    return hist

if __name__=='__main__':
    run()
