#!/usr/bin/env python3
"""Finite arithmetic sanity tests for signed-divisibility truncations.

The infinite assertions rely on the mathematical proof, not on these tests.
This script uses only the Python standard library.
"""
from itertools import product, combinations
from math import comb


def below(x,y):
    return all(a == 0 or (a*b > 0 and abs(a) <= abs(b)) for a,b in zip(x,y))


def sign(x):
    return tuple((u > 0) - (u < 0) for u in x)


def possible(r,k):
    return [v for v in product(range(-k,k+1), repeat=r)
            if 1 <= sum(map(abs,v)) <= k]


def face_levels(r,k):
    # Every face chooses at most one of i+ and i- for each coordinate i.
    # Faces are zero-indexed tuples with signed vertices 2*i,2*i+1.
    out={j:[] for j in range(k)}
    for q in range(1,k+1):
        for support in combinations(range(r),q):
            for signs in product((0,1),repeat=q):
                out[q-1].append(tuple(2*i+s for i,s in zip(support,signs)))
    return out


def rank_mod_p(rows, cols, data, p):
    # Sparse column Gaussian elimination. Returns rank of integer boundary mod p.
    pivots={}
    row_index={v:i for i,v in enumerate(rows)}
    for face in cols:
        vector={row_index[face[:i]+face[i+1:]]: ((-1)**i)%p
                for i in range(len(face))}
        while vector:
            pivot=min(vector)
            coeff=vector[pivot]
            if pivot not in pivots:
                inv=pow(coeff,-1,p)
                pivots[pivot]={i:(v*inv)%p for i,v in vector.items() if v%p}
                break
            prev=pivots[pivot]
            for i,v in prev.items():
                vnew=(vector.get(i,0)-coeff*v)%p
                if vnew:vector[i]=vnew
                elif i in vector:del vector[i]
    return len(pivots)


def verify():
    tests=0
    for r in range(1,6):
        for k in range(1,r+1):
            levels=face_levels(r,k)
            # Reduced C_-1 boundary of each vertex is +1, rank=1.
            for p in (2,3,5):
                boundaries={-1:1}
                for d in range(1,k):
                    boundaries[d]=rank_mod_p(levels[d-1],levels[d],levels[d],p)
                # b_{d}= dim C_d - rank partial_d - rank partial_{d+1}.
                for d,faces in levels.items():
                    down=1 if d==0 else boundaries[d]
                    up=boundaries.get(d+1,0)
                    observed=len(faces)-down-up
                    expected=sum((-1)**(k-j)*2**j*comb(r,j)
                                 for j in range(k+1)) if d==k-1 else 0
                    assert observed==expected,(r,k,p,d,observed,expected)
                    tests+=1
            assert sum((-1)**d*len(a) for d,a in levels.items()) == \
                   1+(-1)**(k-1)*sum((-1)**(k-j)*2**j*comb(r,j)
                                       for j in range(k+1))
            tests+=1
        # Verify the order-preserving, below-identity retraction at small length.
        for k in range(1,min(r,3)+1):
            pts=possible(r,k)
            for x in pts:
                s=sign(x)
                assert s in pts and below(s,x) and sign(s)==s
            for x in pts:
                for y in pts:
                    if below(x,y): assert below(sign(x),sign(y))
            tests+=1
    print('PASS:',tests,'exact finite homology and sign-retraction assertions')
    print('Parameters: r=1..5, k=1..r; mod 2,3,5 ranks; retraction at k<=3')

if __name__=='__main__':
    verify()
