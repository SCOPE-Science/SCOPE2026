#!/usr/bin/env python3
"""Finite, independently enumerated checks for a family of vertex-induced forest complexes.

Pure Python, deterministic. Enumerates subsets by graph-cycle tests rather than by
using the claimed face classification. Computes mod-two simplicial boundary ranks.
"""
from collections import defaultdict
from math import comb


def is_forest(vertices, p, q, t):
    parent=list(range(p+q))
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for i in range(p):
        if not (vertices>>i)&1:
            continue
        for j in range(q):
            if not (vertices>>(p+j))&1 or (i==j and i<t):
                continue
            a=root(i); b=root(p+j)
            if a==b:
                return False
            parent[a]=b
    return True


def faces(p,q,t):
    faces=defaultdict(list)
    for mask in range(1<<(p+q)):
        if is_forest(mask,p,q,t):
            faces[mask.bit_count()].append(mask)
    return faces


def rank_mod2(vectors):
    pivots={}
    for vec in vectors:
        while vec:
            j=vec.bit_length()-1
            if j in pivots:
                vec^=pivots[j]
            else:
                pivots[j]=vec
                break
    return len(pivots)


def betti_mod2(faces):
    ranks={1:1}  # augmentation C_0 -> Z, for a nonempty complex
    top=max(faces)
    for k in range(2,top+1):
        below={f:i for i,f in enumerate(faces[k-1])}
        columns=[]
        for f in faces[k]:
            boundary=0
            bits=f
            while bits:
                bit=bits&-bits; bits-=bit
                boundary^=1<<below[f^bit]
            columns.append(boundary)
        ranks[k]=rank_mod2(columns)
    return {k-1:len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in range(1,top+1)
            if len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0)>0}


def predicted(p,q,t):
    if t==0:
        return {2:(p-1)*(q-1)}
    b3=(t-1)*(p-1)*(q-1)-comb(t,2)*(p+q-2*t+1)-5*comb(t,3)
    b4=comb(t,3)
    assert b3>=0
    return ({3:b3} if b3 else {})|({4:b4} if b4 else {})


def run():
    tested=0
    checked_faces=0
    for p in range(2,7):
        for q in range(p,7):
            original=faces(p,q,0)
            for t in range(min(p,q)+1):
                current=faces(p,q,t)
                got=betti_mod2(current)
                want=predicted(p,q,t)
                assert got==want,(p,q,t,got,want)
                if t:
                    relative_3=len(current[4])-len(original[4])
                    relative_4=len(current[5])-len(original[5])
                    wanted_3=t*(p-1)*(q-1)-comb(t,2)
                    wanted_4=comb(t,2)*(p+q-4)
                    assert (relative_3,relative_4)==(wanted_3,wanted_4),(p,q,t,relative_3,relative_4)
                tested+=1
                checked_faces+=sum(len(v) for v in current.values())
                print(f'p={p} q={q} t={t} reduced_betti_F2={got}')
    signed_six_cycle_test()
    print(f'VERIFY_OK parameter_triples={tested} enumerated_faces={checked_faces} max_shore_size=6')
    print('LIMIT: finite mod-two computations corroborate the proof; integral homotopy and all parameters rely on written arguments.')


def determinant(matrix):
    # Integer Leibniz formula: used only for a 5-by-5 minor.
    from itertools import permutations
    n=len(matrix)
    total=0
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        prod=1
        for i,j in enumerate(perm):
            prod*=matrix[i][j]
        total+=(-1 if inversions%2 else 1)*prod
    return total

def signed_six_cycle_test():
    # The distinguished six vertices of three removed matching pairs form C6.
    p=q=t=3
    F=faces(p,q,t); Q=faces(p,q,0)
    rel4=sorted(set(F[5])-set(Q[5]))
    rel3=sorted(f for f in set(F[4])-set(Q[4]) if
                len({v if v<p else v-p for v in range(p+q) if f>>v&1})==3)
    assert len(rel4)==len(rel3)==6
    M=[[0]*6 for _ in range(6)]
    for j,facet in enumerate(rel4):
        selected=[v for v in range(p+q) if facet>>v&1]
        for idx,v in enumerate(selected):
            sub=facet^(1<<v)
            if sub in rel3:
                M[rel3.index(sub)][j]=(-1)**idx
    assert all(sum(x!=0 for x in col)==2 for col in zip(*M))
    assert abs(determinant([row[:5] for row in M[:5]]))==1
    # Signed top chain of the formal non-face five-simplex is a genuine 4-cycle.
    full=list(range(p+q))
    coeff={((1<<(p+q))-1)^(1<<v):(-1)**i for i,v in enumerate(full)}
    assert all(sum(M[i][j]*coeff[facet] for j,facet in enumerate(rel4))==0 for i in range(6))
    print('SIGNED_BLOCK_OK triple_matched_four_boundary rank=5 unit_minor=1 primitive=true')

if __name__=='__main__':
    run()
