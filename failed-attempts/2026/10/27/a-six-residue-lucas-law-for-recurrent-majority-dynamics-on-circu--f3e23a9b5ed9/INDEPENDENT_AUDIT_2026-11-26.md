# Independent mathematical audit

## correctness

PASS

The exact all-size counting formulas and growth conclusions are correct. The two-time majority rule enforces y=F(x) and x=F(y); a closed walk counted in the trace has a specified starting position, as required for labelled vertices, and each x determines exactly one y. True recurrence is limited to periods one and two: with ±1 spins and symmetric adjacency A, the next state is the unique maximizer of zᵀAx over z, so the adjacent-time bilinear form increases strictly unless the next state equals the previous one. Mixed columns in a fixed prism force the same mixed column on both neighbors, giving two such patterns. Pure columns produce cyclic binary words without isolated bits. Independent exact replay /workspace/reproductions/5.py constructs the complete graph with tuple predicates, computes SCCs by mutual reachability and characteristic polynomials by Newton identities on integer traces, and confirms all relevant polynomials and 400 transitions. There is a non-load-bearing error at RESULT.md line 34: there are 220 loopless singleton components, not 222 (the six live blocks contain 36 vertices; 222 counts both looped singletons too). They contribute zero at any positive power. The live spectra give L_(2n)+2+2cos(2nπ/3) for odd n and L_(2n)+(4+4c)L_n+8+10c for even n, where c=cos(nπ/3). The two cases evaluate to the displayed residue laws. This confirms the Finding independently of the sentence miscount and without relying on the finite n=3,…,10 table.

## originality

FAIL

The 2026/10/26 Möbius-ladder record gives the identical no-isolated-symbol cyclic word count used by the fixed-prism reduction. Adding the two uniform mixed configurations gives the fixed-prism formula. The bipartite double-cover identity then gives the entire recurrent-prism law directly, with no new transfer spectrum needed. The separate November 1 result states equivalent prism formulas explicitly, but its later date is not used to establish earlier coverage.

## value

FAIL

The labelled recurrent census on a natural cubic graph is a meaningful invariant. In this package the entire census, including the growth-rate difference, is mechanically recovered from the prior cyclic-word count and the double cover; the larger transfer certificate does not deliver a distinct claim or additional dynamical consequence. Correcting the loopless-component miscount would not cure that shortfall.

The dated certificate retains the supplied scientific assessment, sources and limitations.
