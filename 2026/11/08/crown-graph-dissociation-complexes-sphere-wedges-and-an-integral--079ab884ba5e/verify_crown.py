#!/usr/bin/env python3
"""Finite checks for the crown-graph second-independence theorem.

Pure Python 3; no external dependencies. Finite checks corroborate the
separate all-n proof using two successive good covers.
"""
from itertools import combinations, permutations
from math import comb, factorial
from collections import defaultdict


def contains_p3(n, mask):
    """Graph theoretic criterion: some selected vertex has two neighbors."""
    for i in range(n):
        if mask >> i & 1:
            if sum(bool(mask >> (n+j) & 1) for j in range(n) if j != i) >= 2:
                return True
        if mask >> (n+i) & 1:
            if sum(bool(mask >> j & 1) for j in range(n) if j != i) >= 2:
                return True
    return False


def cover_facets(n):
    """Two monochromatic simplices and tetrahedra over unordered pairs."""
    left = (1 << n) - 1
    right = left << n
    out = [left, right]
    for i,j in combinations(range(n), 2):
        out.append((1 << i)|(1 << j)|(1 << (n+i))|(1 << (n+j)))
    return out


def enumerate_covered(n):
    """Independent subset-enumeration method via simplex union."""
    f = {0}
    for facet in cover_facets(n):
        sub=facet
        while sub:
            f.add(sub)
            sub=(sub-1)&facet
    return f


def ranks_over_f2(faces):
    """Reduced simplicial homology, with augmented boundary d_0."""
    by = defaultdict(list)
    for f in faces:
        by[f.bit_count()-1].append(f)
    ranks = {}
    for k in sorted(by):
        if k<0:continue
        if k==0:
            ranks[0]=1
            continue
        row={x:i for i,x in enumerate(by[k-1])}
        pivots={}
        for f in by[k]:
            col=0
            remaining=f
            while remaining:
                bit=remaining&-remaining
                remaining-=bit
                col^=1<<row[f-bit]
            while col:
                p=col.bit_length()-1
                if p in pivots:col^=pivots[p]
                else:
                    pivots[p]=col
                    break
        ranks[k]=len(pivots)
    homology={}
    for k in sorted(by):
        if k<0:continue
        b=len(by[k])-ranks.get(k,0)-ranks.get(k+1,0)
        if b:homology[k]=b
    return homology


def inversion_sign(indices):
    p=sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))
    return -1 if p%2 else 1


def reduced_lefschetz(faces,n,sigma,swap):
    """Lefschetz number from signed action on the augmented face chains."""
    action = [(sigma[i]+(n if swap else 0)) for i in range(n)] + [sigma[i]+(0 if swap else n) for i in range(n)]
    result=-1  # empty-face augmentation contributes (-1)^(-1)
    for face in faces:
        if not face:continue
        indices=[j for j in range(2*n) if face>>j & 1]
        images=[action[j] for j in indices]
        if set(indices)==set(images):
            result+=(-1 if len(indices)%2==0 else 1)*inversion_sign(images)
    return result


def main():
    for n in range(2,8):
        faces={m for m in range(1<<(2*n)) if not contains_p3(n,m)}
        covered=enumerate_covered(n)
        assert faces==covered, (n,'cover characterization', faces^covered)
        beta=ranks_over_f2(faces)
        expected = {} if n==2 else {2:comb(n-1,2)}
        assert beta==expected,(n,'homology',beta,expected)
        # A collection of pair-facets intersects iff the corresponding
        # two-element index sets share one common index.
        pairs=list(combinations(range(n),2))
        for k in range(1,min(n,5)+1):
            for chosen in combinations(range(len(pairs)),k):
                actual=(1<<(2*n))-1
                index_intersection=set(range(n))
                for e in chosen:
                    i,j=pairs[e]
                    actual &= (1<<i)|(1<<j)|(1<<(n+i))|(1<<(n+j))
                    index_intersection.intersection_update((i,j))
                assert bool(actual)==bool(index_intersection)
        count=0
        for sigma in permutations(range(n)):
            f=sum(sigma[i]==i for i in range(n))
            t=sum(i<sigma[i] and sigma[sigma[i]]==i for i in range(n))
            character=comb(f,2)-t-f+1
            for swap in (False,True):
                actual=reduced_lefschetz(faces,n,sigma,swap)
                assert actual == character * (-1 if swap else 1), (n,sigma,swap,actual,character)
                count+=1
        assert count==2*factorial(n)
        print(f'n={n} faces_including_empty={len(faces)} mod2_betti={beta} automorphisms_checked={count} PASS')
    print('CROWN_DISSOCIATION_EQUIVARIANT_PASS')

if __name__=='__main__':main()
