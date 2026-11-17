# Independent mathematical audit

## correctness

PASS

The Greenberg-Hastings synchronous 3-state threshold-one successor map is explicitly defined for all 3^16 labeled configurations on the 4x4 rook and Shrikhande graphs. Their common SRG adjacency spectrum does not constrain the nonlinear functional-graph census. Reimplemented the entire state traversal independently in C++ from the adjacency difference sets (43,046,721 states per graph), obtained for rook primitive cycles: 1 fixed, 3,987,936 period-3, 98 period-4, periodic states 11,964,201, Tmax=8 with 54,144 maximal-delay states, 19 nonempty (T,P) classes; for Shrikhande: 1 fixed, 4,109,384 period-3, 6 period-4, periodic 12,328,177, Tmax=9 with 96 maximal-delay states, 21 classes. Independently checked complete class CSV and all counts, not sampling. Independently constructed all 1152 rook and 192 Shrikhande automorphisms and their actions on every primitive four-cycle: rook orbits 32,48,18 and Shrikhande orbit 6, stabilizers 36,24,64 and 32; checked distinct firing profiles. Since primitive 4-cycle counts differ, conjugacy of these *finite dynamical maps* is impossible. This exhaustive finite verification proves only these two graphs, not an infinite family.

## originality

PASS

Best-of-knowledge originality follows from statement-level and implication-level comparisons; no identified complete earlier theorem covers the stated surviving exact result. See structured checks, inspected source material and risks.

## value

PASS

The Shrikhande/rook pair is the canonical nonisomorphic cospectral strongly-regular comparison. An exact full nonlinear excitation-clock and symmetry census sharply separates their dynamics even though all ordinary adjacency spectral data agree. Complete finite classifications of natural graph dynamical systems can be useful independent of a general graph-family theorem; all 3^16 initial states and the automorphism orbits are certified, not arbitrary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
