#!/usr/bin/env python3
"""Exact certificate for Shidoku degree-limited binary Fourier sampling.

Requires only the Python standard library. Run in the same directory as
projector_data.zlib. It checks exact integer projector identities and finite-field
rank lower bounds. No floating point or unpublished external data are needed.
"""
from array import array
from collections import Counter
from itertools import permutations, product, combinations
from math import comb
from pathlib import Path
import sys
import zlib

SIZE=288
P=1009
DEGREES=(1,2,3)
SCALES={1:288,2:2880,3:2880}
RANKS={0:1,1:25,2:151,3:264,4:288}


def boards():
    options=list(permutations(range(4)))
    for grid in product(options,repeat=4):
        if any(len({grid[r][c] for r in range(4)})!=4 for c in range(4)):
            continue
        if any(len({grid[r][c] for r in rr for c in cc})!=4
               for rr in ((0,1),(2,3)) for cc in ((0,1),(2,3))):
            continue
        yield tuple(x for row in grid for x in row)


def integer_gram(configs,degree):
    return [[sum(comb(t,j) for j in range(min(t,degree)+1))
              for t in (sum(a==b for a,b in zip(left,right))
                        for right in configs)]
            for left in configs]


def rank_mod(mat,prime=P):
    a=[[x%prime for x in row] for row in mat]
    n=len(a);m=len(a[0]);rank=0
    for col in range(m):
        k=next((k for k in range(rank,n) if a[k][col]),None)
        if k is None:continue
        a[rank],a[k]=a[k],a[rank]
        inv=pow(a[rank][col],-1,prime)
        a[rank][col:]=[(x*inv)%prime for x in a[rank][col:]]
        pivot=a[rank]
        for i in range(rank+1,n):
            factor=a[i][col]
            if factor:
                a[i][col:]=[(x-factor*y)%prime for x,y in zip(a[i][col:],pivot[col:])]
        rank+=1
        if rank==n:break
    return rank


def get_projectors():
    raw=zlib.decompress(Path(__file__).with_name('projector_data.zlib').read_bytes())
    assert sys.byteorder == 'little', 'certificate uses little-endian int16'
    assert len(raw)==3*SIZE*SIZE*2
    outputs={}
    for i,d in enumerate(DEGREES):
        arr=array('h')
        arr.frombytes(raw[i*SIZE*SIZE*2:(i+1)*SIZE*SIZE*2])
        outputs[d]=[arr[j*SIZE:(j+1)*SIZE] for j in range(SIZE)]
    return outputs


def verify_projector(K,X,scale,dim):
    n=len(K)
    assert all(X[i][j]==X[j][i] for i in range(n) for j in range(n))
    assert sum(X[i][i] for i in range(n))==scale*dim
    XT=[tuple(row[j] for row in X) for j in range(n)]
    for i in range(n):
        for j in range(n):
            assert sum(a*b for a,b in zip(K[i],XT[j]))==0, (i,j,'annihilation')
            assert sum(a*b for a,b in zip(X[i],XT[j]))==scale*X[i][j],(i,j,'idempotence')


def direct_gf2_ranks(configs):
    sets=[frozenset(4*pos+val for pos,val in enumerate(board)) for board in configs]
    pivots={}
    ranks=[]
    for degree in range(5):
        for sub in combinations(range(64),degree):
            col=sum(1<<i for i,b in enumerate(sets) if all(x in b for x in sub))
            while col:
                p=col.bit_length()-1
                if p not in pivots:
                    pivots[p]=col
                    break
                col^=pivots[p]
            if len(pivots)==SIZE:
                break
        ranks.append(len(pivots))
        if len(pivots)==SIZE:break
    return ranks


def run():
    configs=list(boards())
    assert len(configs)==SIZE and len(set(configs))==SIZE
    X=get_projectors()
    ranks={}
    for degree in range(5):
        K=integer_gram(configs,degree)
        r=rank_mod(K)
        assert r==RANKS[degree],(degree,r)
        if degree in X:
            verify_projector(K,X[degree],SCALES[degree],SIZE-r)
        ranks[degree]=r
        print('degree',degree,'rational rank',r,'modular lower bound checked',
              'kernel certificate checked' if degree in X else 'full rank or trivial')
    assert direct_gf2_ranks(configs)==[1,25,150,264,288]
    counts={}
    for degree in (2,3,4):
        counter=Counter(sub for row in configs
                        for sub in combinations(sorted(4*i+x for i,x in enumerate(row)),degree))
        counts[degree]=sum(1 for v in counter.values() if v==1)
    assert counts=={2:0,3:0,4:25728},counts
    print('all exact rational ranks certified:',ranks)
    print('independent direct characteristic-2 monomial ranks:',[1,25,150,264,288])
    print('unique clues of size 2,3,4:',counts)
    print('PASS: all integer identities and finite-field bounds')

if __name__=='__main__':run()
