# Review: the six-column multiple chessboard boundary

## Correctness

**PASS.** Two mathematically independent finite face descriptions produce the same 6,309 nonempty simplices, and the complete face histogram gives Euler characteristic 99. The deterministic checker verifies every one of the 3,105 disjoint codimension-one matched pairs, then independently checks acyclicity by topologically sorting all 6,309 faces of the 27,090-edge oriented Hasse diagram. Exactly one critical vertex and 98 critical four-cells remain. The integral discrete-Morse theorem therefore yields a CW complex with constant four-cell attaching maps and hence the stated sphere wedge. Direct mod-two boundary ranks agree but are not used to infer the integral homotopy type. Risks: any bug shared by the two methods is a residual implementation risk; the complete executable is supplied for replay.

## Originality

**PASS within searched literature, with residual risk.** The nearest primary treatment is Limonchenko–Yu's 2026 four-row family for seven or more columns, with parameters \((2,2,2,m-5)\). Their Theorem 5.5 assumes \(m\ge7\), while the six-column case here is \((2,2,2,1)\). Their torsion criterion in Theorem 1.3 requires four rows having capacity at least two, which this case lacks. Reiner–Roberts give rational homological machinery, and Jojić–Panina–Vrećica–Živaljević give discrete-Morse connectivity bounds, neither directly establishing this integral wedge type. No exact matching theorem was identified among the inspected sources. Residual risk: the specific endpoint calculation could be implicit in older general formulas or unindexed work, and a ranking search cannot establish uniqueness.

## Mathematical value

**PASS.** The six-column member is the natural missing endpoint in the principal four-row torsion family, not a detached parameter substitution. Its complete integral homotopy calculation exhibits a pure, nonshellable but torsion-free complex just before a family with forced two-torsion. The explicit perfect acyclic matching determines actual cell attachments, beyond Betti ranks or torsion absence. This gives a reproducible benchmark for the boundary between combinatorial homotopy and integral torsion phenomena, while remaining a finite classification rather than a claimed general theorem.

## Closest literature and limitations

Limonchenko–Yu, arXiv:2610.37827v1 (2026-10-27), Theorems 1.2, 1.3 and 5.5; Reiner–Roberts (2000), Theorem 3.3; Jojić et al., arXiv:2003.04018, Theorem 6.1. The result does not determine homotopy types outside the specified six-column complex. Overlap risk includes unpublished, unindexed, or implicit equivalent classification. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
