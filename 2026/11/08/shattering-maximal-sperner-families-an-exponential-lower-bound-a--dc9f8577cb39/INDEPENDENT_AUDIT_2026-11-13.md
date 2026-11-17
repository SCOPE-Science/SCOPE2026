# Independent mathematical audit

## correctness

PASS

The fixed-atom rank-r support is shattered: for each positive T retain those rank-r sets; for each omitted x introduce x\{a} at rank r-1, an antichain incomparable with the retained sets, then extend to a maximal antichain; each omitted x is blocked by its subset. Sperner width bounds every shattered support by C(n,floor(n/2)), giving Theta(2^n/sqrt n) with the attained C(n-1,floor((n-1)/2)) lower bound. Exact n=1..5 maximal-clique/trace recursion, independently implemented in independent_checks.py, gave maximal-antichain totals (2,3,7,29,376) and shattered vectors (1,2), (1,4), (1,8,9), (1,16,55,52), (1,32,285,1090,1780,1224,310). The independent orbit check independently computed all 310 six-supports and 11 S5 orbits of sizes 5,5,10,15,15,20,30,30,60,60,60. The provided ORBIT_CLASSES.json and finite verifier were inspected; no exact n>=6 dimension asserted.

## originality

PASS

PASS qualified: The Boolean-lattice maximal Sperner-family incidence class has a rank-star exponential lower bound and an exact five-atom shattering polynomial/orbit classification. Earlier works enumerate maximal antichains or their possible sizes, not the incidence traces over all 2^|S| labelings, so they do not entail the 310 shattered six-supports or 11 orbits. Ignatov's inaccessible full body is an explicitly retained historical risk.

## value

PASS

A natural, independent VC-complexity invariant of maximal Sperner families is resolved asymptotically and given a complete nontrivial five-atom support/orbit census, identifying the first VC dimension larger than the number of atoms. This is useful beyond counting individual maximal antichains, although the general upper bound is classical Sperner and the exact n>=6 values remain unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
