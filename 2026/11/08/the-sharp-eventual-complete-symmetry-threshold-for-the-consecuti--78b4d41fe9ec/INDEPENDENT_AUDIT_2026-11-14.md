# Independent mathematical audit

## correctness

PASS

The definition r(n) counts nonnegative solutions 17x+18y+19z=n, with S_p={n:r(n)>p}; complete symmetry means a terminal ray. In the actual RESULT.md the rational generating function D(X)=((1-X)-B(X))/(XB(X)) (B=product(1-X^a)) and exact integer polynomial identity certify d(n+5814)=d(n)+1 for ALL n. Since the first 5814 d-values have only 120 negative positions, minimum -1 and largest pre-drop r=505 at n=2394, no later d can be negative. Thus for every p>=505 a first drop out of S_p is impossible, and r(2394)=505>504=r(2395) shows sharp failure at p=504. Independently reimplemented coin-change integer dynamic programming and checked all 5814 period shifts and exact boundary counts; finite evidence complements, not substitutes for, the polynomial identity.

## originality

PASS

Best-of-knowledge originality survives: the published example (17,18,19) and the notions of p-complete symmetry are prior, but the explicit least universal cutoff 505 and proof that all larger levels form a terminal ray are not supplied by the inspected Komatsu papers or other semantic matches. An unindexed exact table remains a live priority risk.

## value

PASS

Computes the sharp threshold for a specific, previously published nonmonotone example and supplies a rigorous finite-to-infinite descent certificate, answering an interpretable high-level p-complete-symmetry question. The natural invariant is the LAST possible level where a representation-threshold set ceases to be a tail; the sharp 505 is neither a routine substitution of a known formula nor an arbitrary unexplained integer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
