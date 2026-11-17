"""Exact finite diagnostics for the two-shore-plus-clique Poincare theorem.

The infinite integer-parameter theorem is proved analytically in RESULT.md;
these finite tests are supplementary, not exhaustive verification.
"""
from fractions import Fraction
from itertools import combinations

cases = 0
cuts = 0
triangles = 0
for m in range(3, 13):
    for c in range(1, 10):
        N = 2*m + c
        edge_count = m*m + 2*m*c + c*(c-1)//2
        pair_count = N*(N-1)//2
        lam = Fraction(m-1, m+c-1)
        rho = Fraction(edge_count, pair_count)
        metric_q = Fraction(2*(m-1),m+2*c)
        metric_constant = rho*(1+metric_q)
        l1_constant = rho*(1+lam)
        assert metric_constant/l1_constant - 1 == Fraction((m-1)*(m-2),(m+2*c)*(2*m+c-2))
        expected_eq = {(1,1,0),(m-1,m-1,c)}
        observed_eq = set()
        for x in range(m+1):
            for y in range(m+1):
                for z in range(c+1):
                    s = x+y+z
                    if s == 0 or s == N:
                        continue
                    nonedge_cross = x*(m-x)+y*(m-y)
                    cut_edges = s*(N-s)-nonedge_cross
                    assert cut_edges > 0
                    quotient = Fraction(nonedge_cross,cut_edges)
                    assert quotient <= lam, (m,c,x,y,z,quotient,lam)
                    if quotient == lam:
                        observed_eq.add((x,y,z))
                    cuts += 1
        assert observed_eq == expected_eq, (m,c,observed_eq,expected_eq)
        # Metric witness: each pair within a shore has distance 2,
        # every pair from different shores has distance 1,
        # all clique vertices map to the same target point.
        def dist(i,j):
            if i==j: return 0
            si=0 if i<m else (1 if i<2*m else 2)
            sj=0 if j<m else (1 if j<2*m else 2)
            if si==sj:
                return 0 if si==2 else 2
            return 1
        for i,j,k in combinations(range(N),3):
            dij,djk,dik=dist(i,j),dist(j,k),dist(i,k)
            assert dij<=dik+djk and dik<=dij+djk and djk<=dij+dik
            triangles += 3
        total = sum(dist(i,j) for i,j in combinations(range(N),2))
        energy = sum(dist(i,j) for i,j in combinations(range(N),2) if (i<m<=j or (m<=i<2*m<=j) or (i<2*m and j>=2*m) or (i>=2*m and j>=2*m)))
        # The edge expression covers cross-shore, shore-clique, and clique-clique.
        assert energy == m*m+2*m*c
        assert Fraction(total,energy)*rho == metric_constant
        cases+=1
print(f'JOINED_BICLIQUE_EXACT_OK {cases} parameter pairs; {cuts} exact cuts; {triangles} triangle inequalities')
