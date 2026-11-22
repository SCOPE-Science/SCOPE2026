#!/usr/bin/env python3
"""Independent flip-graph enumeration and row-wise Boolean sampling rank."""
from itertools import combinations
from collections import deque
from math import comb

def normalized(a,b):
    return (a,b) if a < b else (b,a)

def flip_neighbors(T,n):
    boundary = {normalized(i,(i+1)%n) for i in range(n)}
    E = boundary | set(T)
    for a,c in T:
        opposite = [b for b in range(n) if b not in (a,c)
                    and normalized(a,b) in E and normalized(b,c) in E]
        assert len(opposite) == 2, (n,T,(a,c),opposite)
        new_edge = normalized(*opposite)
        yield frozenset((set(T) - {(a,c)}) | {new_edge})

def enumerate_by_flips(n):
    seed = frozenset((0,j) for j in range(2,n-1))
    seen = {seed}
    todo = deque([seed])
    while todo:
        T=todo.popleft()
        for S in flip_neighbors(T,n):
            if S not in seen:
                assert len(S) == n-3
                seen.add(S)
                todo.append(S)
    return tuple(sorted(seen,key=lambda s:tuple(sorted(s))))

def row_rank_mod2(states,degree):
    face_set=set()
    for T in states:
        T=sorted(T)
        for k in range(degree+1):
            face_set.update(combinations(T,k))
    faces = sorted(face_set)
    ids = {f:i for i,f in enumerate(faces)}
    pivots={}
    for T in states:
        T=sorted(T)
        row=0
        for k in range(degree+1):
            for f in combinations(T,k):
                row |=1<<ids[f]
        while row:
            p=row.bit_length()-1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p]=row
                break
    return len(pivots),len(faces)

def parity_cube(n):
    r=(n-2)//2
    base={(0,j) for j in range(2,n-1)}
    flips=[((0,2*j),(2*j-1,2*j+1)) for j in range(1,r+1)]
    signed=[]
    for bits in range(1<<r):
        T=set(base)
        for j,(old,new) in enumerate(flips):
            if bits & (1<<j):
                T.remove(old);T.add(new)
        signed.append((frozenset(T),(-1)**bits.bit_count()))
    return signed, [new for old,new in flips]

def verify_cube(n,states):
    r=(n-2)//2
    signed,new=parity_cube(n)
    assert len(set(T for T,w in signed))==2**r
    assert all(T in set(states) for T,w in signed)
    diagonals=sorted(set().union(*states))
    for k in range(r):
        for idxs in combinations(diagonals,k):
            assert sum(w for T,w in signed if set(idxs)<=T)==0
    prob_event=sum(w for T,w in signed if set(new)<=T)
    assert abs(prob_event)==1


def main():
    for n in range(4,11):
        states=enumerate_by_flips(n)
        count=comb(2*(n-2),n-2)//(n-1)
        assert len(states)==count, (n,len(states),count)
        threshold=(n-2)//2
        if n>=6:
            verify_cube(n,states)
        k,features=row_rank_mod2(states,threshold)
        assert k==count, (n,k,count)
        print('n=%d states=%d degree=%d row_rank_mod2=%d nonzero_features=%d' %
              (n,count,threshold,k,features))
    print('PASS flip graph, parity lower bound, and independent row-rank certificate')

if __name__=='__main__':
    main()
