# Independent mathematical audit

## correctness

PASS

The source program explicitly generates all matchings of the complement of each labeled cycle n=3..9 and creates every signed simplicial boundary in increasing edge order. The source elimination chooses only unit ±1 pivots and applies integer row and column additions, clearing a pivot row and column without divisions; zero residual proves all nonzero Smith invariant factors are units. This saturates each boundary image in the corresponding free chain lattice, hence integral homology is torsion-free. At n9 f0..f3=(27,216,555,324), boundary ranks r1,r2,r3=(26,190,323); the exact kernel-minus-image rank formulas give b2=42, b3=1, and vanish in other nonnegative degrees. Earlier cases give n5..n7 only Htilde1=Z^1,Z^6,Z^1 and n8 Htilde2=Z^42; n3 empty and n4 simplex. Independent generation and mod2 matrix elimination confirmed the f-vectors, ranks and Betti numbers n3..9; mod2 corroboration alone would not exclude integral torsion, which depends on the inspected unimodular integer algorithm.

## originality

PASS

Best-of-knowledge original after comparing exact statements and implications, excluding the mirror of this very submission as independent prior; primary-source limitations and exact residual risks below.

## value

PASS

The complement-of-cycle (antihole) family is canonical and occurs naturally when forbidding cyclic nearest-neighbor edges in graph matchings. The first occurrence of integral homology in two adjacent positive degrees, including the exact rank-42 H2 and rank-one H3, is a sharp complete finite cutoff that signals new topology beyond one-degree patterns. These are precise reusable invariants, not an arbitrary sample, and no stronger homotopy wedge type is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
