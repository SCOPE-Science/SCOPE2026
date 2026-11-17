#!/usr/bin/env python3
"""Independent finite checks of the dihedral character of cyclic noncover complexes.

Standard library only. This test enumerates independent sets instead of using
quotient-graph path and cycle formulas. It checks all symmetries at lengths 4..18.
"""
from itertools import combinations
from math import gcd


def independent_faces(n):
    masks = []
    for mask in range(1 << n):
        if (mask & (((mask << 1) | (mask >> (n - 1))) & ((1 << n) - 1))) == 0:
            masks.append(mask)
    return masks


def permutation(n, a, reflection):
    if reflection:
        return [(a - v) % n for v in range(n)]
    return [(v + a) % n for v in range(n)]


def permutation_sign(p, indices):
    values = [p[i] for i in indices]
    return -1 if (sum(values[i] > values[j] for i in range(len(values)) for j in range(i+1,len(values))) % 2) else 1


def permute_mask(p, mask):
    out = 0
    for i,v in enumerate(p):
        if mask >> i & 1: out |= 1 << v
    return out


def lefschetz_ind(n, p, faces):
    # Reduced chain Lefschetz with the empty simplex in degree -1.
    total = 0
    for mask in faces:
        if permute_mask(p, mask) != mask: continue
        indices = [i for i in range(n) if mask >> i & 1]
        total += (-1 if not indices else (-1)**(len(indices)-1)) * permutation_sign(p, indices)
    return total


def predicted(n, a, reflection):
    if n % 3 == 0:
        if reflection: return 0
        return 2 if a % 3 == 0 else -1
    if reflection: return (-1)**(n//3)
    return 1


def noncover_faces(n):
    full=(1<<n)-1
    return [s for s in range(1<<n) if
            any(((full ^ s) >> i & 1) and ((full ^ s) >> ((i+1)%n) & 1)
                for i in range(n))]


def noncover_homology_degree(n):
    k, rem = divmod(n,3)
    return 2*k-2 if rem == 0 else 2*k-1


def independent_homology_degree(n):
    k, rem = divmod(n,3)
    return (k if rem == 2 else k-1)


def rank_mod_p(sparse_columns, p):
    pivots = {}
    for col in sparse_columns:
        col = dict(col)
        while col:
            pivot = max(col)
            if pivot not in pivots:
                mul = pow(col[pivot], -1, p)
                pivots[pivot] = {k:(v*mul)%p for k,v in col.items()}
                break
            mul=col[pivot]
            for k,v in pivots[pivot].items():
                vnew=(col.get(k,0)-mul*v)%p
                if vnew: col[k]=vnew
                else: col.pop(k,None)
    return len(pivots)


def betti_independence(n,p):
    faces=independent_faces(n)
    layers = {}
    for mask in faces: layers.setdefault(mask.bit_count()-1,[]).append(mask)
    ranks={}
    for deg in range(0,max(layers)+1):
        lows={m:i for i,m in enumerate(layers[deg-1])}
        cols=[]
        for m in layers.get(deg,[]):
            vertices=[v for v in range(n) if (m>>v)&1]
            d={lows[m & ~(1<<v)]:(-1 if j%2 else 1)%p for j,v in enumerate(vertices)}
            cols.append(d)
        ranks[deg]=rank_mod_p(cols,p)
    return {j: len(v)-ranks.get(j,0)-ranks.get(j+1,0) for j,v in layers.items() if len(v)-ranks.get(j,0)-ranks.get(j+1,0)}


def main():
    total=0
    for n in range(4,19):
        faces=independent_faces(n)
        q=independent_homology_degree(n)
        for refl in (False,True):
            for a in range(n):
                p=permutation(n,a,refl)
                lf=lefschetz_ind(n,p,faces)
                vp=permutation_sign(p,range(n))
                # For unique reduced degree, Ind-trace = (-1)^q * Lefschetz.
                theta_trace=vp*((-1)**q)*lf
                assert theta_trace == predicted(n,a,refl),(n,a,refl,theta_trace,predicted(n,a,refl))
                total+=1
        if n<=13:
            theta_faces=noncover_faces(n)
            for refl in (False,True):
                for a in range(n):
                    theta_lf=lefschetz_ind(n,permutation(n,a,refl),theta_faces)
                    theta_char=(-1)**noncover_homology_degree(n) * theta_lf
                    assert theta_char==predicted(n,a,refl),(
                        'direct noncover faces',n,a,refl,theta_char)
            expected_dim=(2 if n%3==0 else 1)
            expected_q=q
            for prime in (2,3,5):
                betti=betti_independence(n,prime)
                assert betti=={expected_q:expected_dim},(n,prime,betti)
        print('n=',n,'independent_faces=',len(faces),'D_n_checks=',2*n,'character_verified')
    print('TOTAL_SYMMETRIES_CHECKED',total)
    print('DIRECT_NONCOVER_SYMMETRIES_CHECKED',sum(2*n for n in range(4,14)))
    print('NONCOVER_CYCLE_DIHEDRAL_CHARACTER_PASS')

if __name__=='__main__': main()
