# Independent mathematical audit

## correctness

PASS

A block of K5 edges is valid iff its union uses at most three ground elements: this is exactly the existence of a disjoint two-element witness, and edges on at most three elements are pairwise incident. Thus triple blocks are triangles, and admissible pairs give edges of T5. With two disjoint triangles the remaining edges give a C4 with two perfect matchings; three disjoint triangles are impossible because the corresponding complementary two-sets would be pairwise disjoint. Conditioning on 0,1,2 triangles gives the matching formula with factors 1,10,15 and exponent 10-2r-j for r triples and j doubletons. Independently /tmp/opencode/check_petersen_independent.py generated the allowed block masks directly by union size and exhausted disjoint covers by branching on the least uncovered edge; it reproduced coefficients (30,604,1575,1130,295,30,1) from degrees 4 through 10, the sole optimum shape (3,3,2,2), and a single 30-partition S5 orbit. Unlabelled blocks are counted once. Exact Horner evaluation at the six disjoint negative brackets reproduced every sign and endpoint value, giving six distinct negative roots of the degree-six quotient, with zero of multiplicity four in the full polynomial. Newton's normalized coefficient inequalities then imply strict log-concavity of the positive unnormalized coefficients.

## originality

PASS

The surviving originality is the full CD partition polynomial and consequently its rigorously determined simple negative spectrum. Credit the known scalar minimum 4 and the strong structural coverage of the optimum via the named two-rainbow configuration; do not claim independent novelty for the number 30 and single orbit by themselves. The closest broader CD theorem uses the same block-shape reduction and covers the minimum at n=5, but its exact counting claims and supporting census exclude that case. Its proofs and the other related tables do not supply the full polynomial.

## value

PASS

The Petersen graph is the canonical triangle-free small Kneser graph for comparing class-wise domination with proper and total-domination parameters. Its full unlabelled partition rank enumerator fills a meaningful gap beyond the scalar minimum and the optimum orbit analogue. The mixture of triangle-block choices and matchings gives an interpretable benchmark for root behavior of these constrained rank polynomials; matching polynomial real-rootedness alone does not imply real-rootedness of the combined enumerator. All six nonzero roots are simple negative, a definite distributional property beyond a short count table. No general real-rootedness or stronger originality for the optimum alone is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
