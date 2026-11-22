#!/usr/bin/env python3
"""Finite checks for signed-support Grothendieck-poset punctures.

Uses only the Python standard library. The general statements are proved
symbolically; exhaustive finite tests here guard low-rank boundary cases.
"""
from itertools import product, permutations
from math import comb

def leq(a,b):
    return all(x == 0 or (x*b_i > 0 and abs(x) <= abs(b_i)) for x,b_i in zip(a,b))

def sign(a):
    return tuple((1 if z>0 else -1 if z<0 else 0) for z in a)

def neg(a):return tuple(-z for z in a)

def boundary_faces(r):
    vertices=list(range(2*r))
    faces={k:[] for k in range(r)}
    for s in product((-1,0,1),repeat=r):
        if not any(s):continue
        f=tuple(2*i+(0 if t==1 else 1) for i,t in enumerate(s) if t)
        faces[len(f)-1].append(f)
    for k in range(r):
        assert len(faces[k])==2**(k+1)*comb(r,k+1)
    return faces

def rank_f2(columns):
    pivots={}
    for c in columns:
        while c:
            b=c.bit_length()-1
            if b not in pivots:
                pivots[b]=c
                break
            c^=pivots[b]
    return len(pivots)

def homology(r):
    faces=boundary_faces(r)
    ranks={0:0,r:0}
    for k in range(1,r):
        pos={f:i for i,f in enumerate(faces[k-1])}
        cols=[]
        for f in faces[k]:
            c=0
            for j in range(k+1):c ^=1<<pos[f[:j]+f[j+1:]]
            cols.append(c)
        ranks[k]=rank_f2(cols)
    beta={k:len(faces[k])-ranks[k]-ranks[k+1] for k in range(r)}
    # Reduced degree-zero homology subtracts one in the connected cases.
    beta[0]-=1
    if r==1:
        beta[0]=len(faces[0])-1
    assert beta == {k:(1 if k==r-1 else 0) for k in range(r)}, (r,beta)
    return beta

def check_rank(r,max_mag):
    domain=[x for x in product(range(-max_mag,max_mag+1),repeat=r) if any(x)]
    S={x for x in product((-1,0,1),repeat=r) if any(x)}
    assert len(S)==3**r-1
    assert all(sign(x) in S and leq(sign(x),x) for x in domain)
    for x in domain:
        for y in domain:
            if leq(x,y):assert leq(sign(x),sign(y))
    # Every higher element has a unique set of immediate predecessors.
    signatures={}
    for x in domain:
        if sum(map(abs,x))==1:continue
        pred=[]
        for i,z in enumerate(x):
            if z:
                y=list(x);y[i]-=(1 if z>0 else -1)
                if any(y):pred.append(tuple(y))
        sig=frozenset(pred)
        assert sig not in signatures, (r,x,signatures.get(sig))
        signatures[sig]=x
    atoms=[x for x in domain if sum(map(abs,x))==1]
    assert len(atoms)==2*r
    for x in atoms:
        for y in atoms:
            compatible=any(leq(x,z) and leq(y,z) for z in S)
            assert compatible == (y!=neg(x)),(x,y)
    # Explicit group action and its orientation multiplier.
    facets=[tuple(s) for s in product((-1,1),repeat=r)]
    fundamental={s:__import__('math').prod(s) for s in facets}
    for perm in permutations(range(r)):
        inversions=sum(perm[i]>perm[j] for i in range(r) for j in range(i+1,r))
        parity=(-1)**inversions
        for flips in product((-1,1),repeat=r):
            factor=parity*__import__('math').prod(flips)
            for s,coeff in fundamental.items():
                target=tuple(flips[i]*s[perm[i]] for i in range(r))
                image_coeff=coeff*parity
                assert image_coeff == factor*fundamental[target]
    return len(domain),len(S),beta

if __name__=='__main__':
    for r,mag in ((1,3),(2,3),(3,2),(4,2)):
        beta=homology(r)
        result=check_rank(r,mag)
        print(f'rank={r} max_magnitude={mag} vectors={result[0]} sign_vectors={result[1]} reduced_mod2_betti={beta} signed_symmetries={2**r*__import__("math").factorial(r)}')
    print('PASS: order retraction, face counts, mod-2 homology, antipodal atom relation, signed orientation character')
