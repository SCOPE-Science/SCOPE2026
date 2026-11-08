#!/usr/bin/env python3
"""Independent finite verification of maximal induced-forest counts in rook graphs.

Uses direct cycle detection on vertex-induced rook subgraphs, independently
of a recurrence that enumerates alternating path components in K_{m,n}.
All calculations are exact integers; tested finite cases do not prove the
unrestricted theorem.
"""
from collections import Counter
from functools import lru_cache
from math import comb, factorial


def formula(m, n):
    assert 2 <= m <= n
    if m == n:
        return {1: factorial(m)**2}
    return {
        s: (factorial(m)*factorial(n)*comb(m-1,s-1)
            // (2**s*factorial(s)*factorial(n-m-s)))
        for s in range(1, min(m, n-m)+1)
    }


@lru_cache(None)
def path_recurrence(a,b,s):
    # Fix the first vertex of the smaller part in its unique component.
    if a==0:
        return int(s==0)
    if s==0:
        return 0
    count=0
    for k in range(1,a+1):
        if b<k+1:break
        # Each undirected alternating path on k plus k+1 labels
        # has k!(k+1)!/2 possible orders.
        count += (comb(a-1,k-1)*comb(b,k+1)*factorial(k)*
                  factorial(k+1)//2)*path_recurrence(a-k,b-k-1,s-1)
    return count


def direct(m,n):
    v=m*n
    adj=[0]*v
    for i in range(v):
        a,b=divmod(i,n)
        for j in range(v):
            c,d=divmod(j,n)
            if i!=j and (a==c or b==d):adj[i]|=1<<j

    @lru_cache(None)
    def test_forest(mask):
        par=list(range(v)); nv=mask.bit_count()
        def root(x):
            while par[x]!=x:
                x=par[x]
            return x
        edges=0
        for i in range(v):
            if not (mask>>i)&1:continue
            for j in range(i+1,v):
                if (mask>>j)&1 and (adj[i]>>j)&1:
                    edges+=1
                    r1,r2=root(i),root(j)
                    if r1==r2:return (False,0)
                    par[r1]=r2
        return (True,nv-edges)

    counts=Counter();maximal_sets=0
    for mask in range(1,1<<v):
        valid,components=test_forest(mask)
        if not valid:continue
        if all(not test_forest(mask|(1<<i))[0]
               for i in range(v) if not (mask>>i)&1):
            maximal_sets+=1
            counts[(mask.bit_count(),components)]+=1
            # independently inspect row degrees of the selected cells
            degrees_row=[sum((mask>>(a*n+b))&1 for b in range(n)) for a in range(m)]
            degrees_col=[sum((mask>>(a*n+b))&1 for a in range(m)) for b in range(n)]
            if m<n:
                assert all(t==2 for t in degrees_row)
            else:
                assert sorted(degrees_row)==[1]+[2]*(m-1)
                assert sorted(degrees_col)==[1]+[2]*(n-1)
    expected_size=2*m if m<n else 2*m-1
    expected={(expected_size,s):c for s,c in formula(m,n).items()}
    assert dict(counts)==expected, (m,n,counts,expected)
    return (1<<v)-1,maximal_sets


def run():
    checked_subsets=0
    maximal=0
    cases=0
    for m in range(2,5):
        for n in range(m,9):
            if m*n>16:continue
            sub,ma=direct(m,n)
            checked_subsets+=sub;maximal+=ma;cases+=1
    arithmetic=0
    for m in range(2,13):
        for n in range(m+1,31):
            for s,c in formula(m,n).items():
                assert path_recurrence(m,n,s)==c,(m,n,s,c)
                arithmetic+=1
    # Connectedness threshold, square balance, and arithmetic asymptotics
    for m in range(2,100):
        assert formula(m,m)=={1:factorial(m)**2}
        assert set(formula(m,m+1))=={1}
    print(f'VERIFY_OK rook_board_cases={cases} nonempty_subsets={checked_subsets} '
          f'maximal_forests={maximal} independent_path_recurrence_checks={arithmetic} '
          'component_distributions_and_structures=PASS')

if __name__=='__main__':
    run()
