# Independent mathematical audit

## correctness

PASS

Expanding the universal-type/existential-witness recursion gives the stated pair and singleton tests. A qualifying same-shore pair needs a spare same-shore vertex and four opposite-shore profiles, so rank at least three at the root forces at least four vertices per shore. Four edges would all be incident with one qualifying left pair, but the qualifying right pair needs three distinct nonzero left rows. In the displayed witness, using zero-based labels, left vertex 2 has same-shore partner 3 and mixed partners at right vertices 0 and 2 with opposite incidence values; right vertex 0 has same-shore partner 1 and mixed partners at left vertices 2 and 3 with opposite values. Thus the witness attains both lower bounds. The independent replay applies the definition bottom-up on all 65,536 matrices, and checks every recorded orbit and the fixed-point matrix. It gives 9,672 labelled matrices, 29 orbits of sizes 72/96/288/576 with multiplicities 1/4/16/8, the stated seven edge counts, and the Burnside sum 16,704. The 576 five-edge matrices form one orbit, represented by a six-vertex path and the two isolates. The census is for rank at least three, with named shores, at host order eight only.

## originality

PASS

The rank framework is prior work, as are sharp rank-three extremal problems for related ages and the unfiltered binary-matrix census. The distinct contribution is the named-shore bounds and the complete rank-filtered first-order census, including the unique minimum-edge orbit. No inspected result gives that combination by equivalence or implication.

## value

PASS

For the natural two-sorted random bipartite age this identifies the smallest finite hosts supporting three successive rounds of every requested extension, a constraint not visible from ambient 4×4 isomorphism counts. The all-order edge obstruction and its unique smallest-order extremizer explain the sparse end of the problem. The complete filtered orbit census describes every optimal-order witness and demonstrates how much stronger rank is than merely having enough vertices on both shores.

The dated certificate retains the supplied scientific assessment, sources and limitations.
