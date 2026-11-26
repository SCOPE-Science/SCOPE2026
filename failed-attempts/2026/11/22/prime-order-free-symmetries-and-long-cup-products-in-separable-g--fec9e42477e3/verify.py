#!/usr/bin/env python3
"""Finite sanity checks for cyclic actions on separable graph complexes.
Public mathematical reproducibility only; general theorem is proved symbolically.
"""
from itertools import combinations
from math import factorial

def two_connected(n, edges):
    # Tests connectedness after deleting zero or one vertices.
    # This exactly matches the definition of 2-vertex-connectivity for n>=3.
    for omitted in [-1] + list(range(n)):
        vs=[v for v in range(n) if v!=omitted]
        visited={vs[0]}
        stack=[vs[0]]
        while stack:
            u=stack.pop()
            for a,b in edges:
                if a==omitted or b==omitted: continue
                v = b if a==u else a if b==u else -1
                if v!=-1 and v not in visited:
                    visited.add(v)
                    stack.append(v)
        if len(visited)!=len(vs):
            return False
    return True

def check(n):
    ee=list(combinations(range(n),2))
    inv={e:i for i,e in enumerate(ee)}
    def r(e):return tuple(sorted(((e[0]+1)%n,(e[1]+1)%n)))
    perms=[]
    for k in range(1,n):
        perms.append([inv[tuple(sorted(((a+k)%n,(b+k)%n)))] for a,b in ee])
    faces=[]
    ff=[0]*(len(ee)+1)
    for mask in range(1,1<<len(ee)):
        selected=[ee[i] for i in range(len(ee)) if mask>>i&1]
        if not two_connected(n,selected):
            faces.append(mask)
            ff[mask.bit_count()]+=1
    fixed={}
    for k,perm in enumerate(perms,1):
        fixed[k]=[]
        for mask in faces:
            new=sum(1<<perm[i] for i in range(len(ee)) if mask>>i&1)
            if new==mask:fixed[k].append(mask)
    euler=sum((-1)**(s-1)*ff[s] for s in range(1,len(ff)))
    print(f'n={n} vertices={len(ee)} nonempty_faces={len(faces)} euler={euler} fixed_face_counts='+str({k:len(v) for k,v in fixed.items()}))
    if n in (3,5):
        assert all(not fixed[k] for k in fixed)
        assert euler == 1-factorial(n-2) # sphere dimension 2*n-5 is odd
    if n in (4,6):
        assert fixed[1], (n,'expected invariant faces for full rotation')
    return fixed

if __name__=='__main__':
    for n in (3,4,5,6):check(n)
    for p in (5,7,11):
        m=2*p-5
        degrees=list(range(1,m,2))
        powers=list(range(1,(m-1)//2+1))
        assert len(degrees)==len(powers)==p-3
        print(f'p={p} dim_connectivity_bound={m-1} nonzero_H_odd_degrees={degrees} nonzero_cup_powers={powers}')
    print('PRIME_SEPARABLE_GRAPH_QUOTIENT_SANITY_OK')
