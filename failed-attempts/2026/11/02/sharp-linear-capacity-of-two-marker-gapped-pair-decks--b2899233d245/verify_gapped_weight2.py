#!/usr/bin/env python3
"""Finite independent verification of two-marker gapped pair-deck theorem.
No external dependencies. Uses literal admissible pair enumeration and independently
sums pair-label observations; checks the closed formula and sharp boundary.
"""
from collections import defaultdict
from itertools import combinations

def deck_by_positions(n, s, i, j):
    # Index positions are 1,...,n; 0 at all positions other than i,j.
    counts = [0,0,0,0]  # index 2*first + second
    for p in range(1,n+1):
        for q in range(p+s,n+1):
            a = int(p == i or p == j)
            b = int(q == i or q == j)
            counts[2*a+b] += 1
    return tuple(counts)

def analytical_deck(n,s,i,j):
    h=int(j-i>=s)
    B=sum(max(p-s,0) for p in (i,j))-h
    C=sum(max(n-p-s+1,0) for p in (i,j))-h
    total=max(0,(n-s)*(n-s+1)//2)
    return (total-B-C-h, B, C, h)

def theorem_capacity(n,s):
    if s == 2 and n >=5: return 5*n-15
    if s >=3 and n >=3*s-1: return (2*s+2)*n-(3*s*s+2*s+3)
    raise ValueError('Outside the theorem')

def boundary_capacity(n,s):
    if s >=3 and n ==3*s-2:
        return (2*s+2)*n-(3*s*s+2*s+3)+1
    if s==2 and n==4: return 6
    raise ValueError('Outside boundary')

def verify():
    exact_instances=0
    boundary_instances=0
    cases=0
    literal_pairs=0
    position_pairs=0
    for s in range(2,19):
        for n in range(max(s+1,3),min(3*s+25,100)):
            spectra=set()
            for i,j in combinations(range(1,n+1),2):
                expected=analytical_deck(n,s,i,j)
                if n <= 19:
                    actual=deck_by_positions(n,s,i,j)
                    assert actual==expected,(n,s,i,j,actual,expected)
                    literal_pairs += 1
                spectra.add(expected)
                position_pairs += 1
            cases+=1
            if (s==2 and n>=5) or (s>=3 and n>=3*s-1):
                expected=theorem_capacity(n,s)
                assert len(spectra)==expected,(n,s,len(spectra),expected)
                exact_instances+=1
            if (s>=3 and n==3*s-2) or (s==2 and n==4):
                expected=boundary_capacity(n,s)
                assert len(spectra)==expected,(n,s,len(spectra),expected)
                boundary_instances+=1
    print(f'VERIFY_OK gap_values=2..18 cases={cases} literal_pair_observations={literal_pairs} position_pairs={position_pairs} theorem_instances={exact_instances} sharp_boundary_instances={boundary_instances}')
    for s in [2,3,4,5,7,10]:
        n=max(3*s-1,5)
        print(f'EXACT s={s} n={n} capacity={theorem_capacity(n,s)} next={theorem_capacity(n+1,s)}')

if __name__=='__main__': verify()
