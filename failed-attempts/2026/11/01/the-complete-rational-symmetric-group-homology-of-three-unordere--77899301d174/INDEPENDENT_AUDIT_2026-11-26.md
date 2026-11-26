# Independent mathematical audit

## correctness

PASS

The reduced half-edge-difference model is justified by the natural comparison (Theorem 4.5 and Proposition 4.9 of arXiv:1708.02351), with no isolated vertices. A separate exact cubical computation subdivides each Petersen edge into two, giving paths between distinct essential vertices of length at least 2 and cycles of length at least 10. This fits the unordered three-point discrete-configuration comparison as stated in Ko–Park §1; inclusion, not necessarily the deformation retraction, is equivariant. Unordered cubes consist of disjoint closed edge factors and complementary vertices. Oriented edge endpoint signs and coordinate permutations give chain dimensions (2300,7590,8190,2880), F3 ranks (2299,5285,2880). Integrally the first rank is at most 2299 by augmentation, and the columns of the top boundary are independent. The 12 graph pentagons span the six-dimensional graph cycle space; a particle can traverse each cycle with two stationary elsewhere. The induced total-motion map on H1 is natural for relabelings (sum motion paths, independent of ordering), giving the matching rational upper bound 5285 for the middle rank. H1 is therefore the graph cycle module, S^(3,1,1). With the orientation signs included, seven cubical Hopf traces give H2=(25,-3,-2,1,1,0,0) in the frozen order, with Specht multiplicities (0,0,0,1,1,2,1) in frozen order; Betti numbers are (1,6,25,0). The orbit argument applies here: triangulate the triple graph product with its diagonals equivariantly (cut product cubes by same-edge coordinate equalities); in the complement of the diagonal subcomplex, barycentric subdivision gives an equivariant retraction to the face-chain subcomplex on nondiagonal faces. It descends under the particle permutation action and under the graph action. After removing simplex inversions, rational orbit homology is invariant homology by exact averaging. No contractibility or integral torsion classification follows. Independent replay: python -B /workspace/review_evidence/1_cubical.py; output 1_cubical.txt. No uploaded script executed.

## originality

FAIL

Distinct earlier record a27f53bdd4d3 has the exact same degree-two action under the same relabelings. It also proves the full Betti vector, identifies H1 equivariantly with graph cycles and writes its full character in the proof. A distinct same-day record covers all Specht modules explicitly; the decision does not infer order or public priority from that date. The quotient is an invariant-homology corollary, not an uncovered representation.

## value

FAIL

This natural representation would be a useful benchmark if unknown, but the exact invariant has already been calculated in the same space and the quotient claim directly follows from that representation. A fresh implementation corroborates the computation without yielding a scientific remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
