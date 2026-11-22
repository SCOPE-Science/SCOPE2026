#!/usr/bin/env python3
"""Direct labelled finite-extension census for Henson graphs over complete bicliques.

Every possible adjacency bit string to the named vertices and among the new
ordered vertices is considered. The forbidden clique test is generated from
actual vertex subsets; it does not use the closed formula to count diagrams.
"""
from itertools import combinations
from math import comb

def formula(m, a, b, s):
    assert m>=4 and a>=1 and b>=1 and 0<=s<=m-2
    n=a+b
    all_diagrams=1 << (s*n+comb(s,2))
    if s < m-2:
        return all_diagrams
    q=1 << s
    return all_diagrams-(q**a-(q-1)**a)*(q**b-(q-1)**b)

def direct(m, a, b, s):
    n=a+b
    # Vertices 0,...,a-1 and a,...,n-1 form the two old sides;
    # n,...,n+s-1 are new, distinguishable, ordered coordinates.
    fixed_edges={frozenset((u,v)) for u in range(a) for v in range(a,n)}
    variable_edges=[(u,v) for u in range(n+s) for v in range(u+1,n+s)
                    if u>=n or v>=n]
    assert len(variable_edges)==n*s+comb(s,2)
    bit_for_edge={frozenset(edge):i for i,edge in enumerate(variable_edges)}
    required=[]
    for vertices in combinations(range(n+s),m):
        fixed_missing=False
        mask=0
        for u,v in combinations(vertices,2):
            edge=frozenset((u,v))
            if u<n and v<n:
                if edge not in fixed_edges:
                    fixed_missing=True
                    break
            else:
                mask |= 1<<bit_for_edge[edge]
        if not fixed_missing:
            required.append(mask)
    total=1<<len(variable_edges)
    return sum(not any((diagram&mask)==mask for mask in required)
               for diagram in range(total))

def main():
    tests=0
    for m in [4,5,6,7]:
        max_n={4:6, 5:5, 6:3, 7:2}[m]
        for n in range(2,max_n+1):
            for a in range(1,n):
                b=n-a
                for s in range(0,m-1):
                    # On the largest cases only the first detecting arity is
                    # material; all smaller arities are tested for smaller m.
                    if (m==7 and s!=m-2) or (m==6 and s<m-3):
                        continue
                    got=direct(m,a,b,s)
                    expected=formula(m,a,b,s)
                    assert got==expected,(m,a,b,s,got,expected)
                    tests+=1
    inversion=0
    for m in range(4,12):
        for n in range(2,101):
            numbers={}
            for a in range(1,n):
                b=n-a
                value=formula(m,a,b,m-2)
                other=numbers.get(value)
                assert other is None or other==(min(a,b),max(a,b)),(m,n,a,b,other)
                numbers[value]=(min(a,b),max(a,b))
                inversion+=1
    assert formula(4,1,3,2)==475 and formula(4,2,2,2)==463
    assert formula(5,1,3,3)==32599 and formula(5,2,2,3)==32543
    print('BRUTE_FORCE_FINITE_EXTENSION_CASES_PASS',tests)
    print('ARITHMETIC_RECONSTRUCTION_CASES_PASS',inversion)
    print('FIRST_SEPARATING_EXAMPLES_PASS',4)
    print('FINITE_CHECKS_SUPPORT_NOT_REPLACE_PROOF')

if __name__=='__main__':
    main()
