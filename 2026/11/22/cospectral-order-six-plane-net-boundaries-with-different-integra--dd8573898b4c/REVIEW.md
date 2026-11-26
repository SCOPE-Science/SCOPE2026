# Independent mathematical audit

## correctness

PASS

The cited cyclic and dihedral plane nets exist, with D_3≅S_3 here. The curve has a rational component per vertex; 6 or 3 distinct nodes on each component give stability, connectivity follows from the pairwise-class incidences, and the genus is 108−54+1=55. Nodal deformation parameters can be chosen simultaneously equal to a uniformizer by the unobstructed deformation theory of nodal stable curves; this gives local thickness one and regularity. Baker, arXiv:math/0701075 Appendix A, directly confirms Raynaud's identification for the reducible regular reduced case: the special-fiber intersection matrix is minus the unit-thickness graph Laplacian and the geometric component group is Div^0/Prin of the graph. For the spectrum, BB^T has eigenvalues 18,6,0 of multiplicities 1,15,2. The 16 nonzero singular modes yield (t)(t−9)(t²−9t+12)^15; the unpaired line and point kernel dimensions 2 and 20 give (t−6)^2(t−3)^20. Matrix-tree gives 2^31·3^36. Over F3 the row relations consist of a homomorphism to the additive field plus two independent constants, giving ranks 15 and 16, and hence Laplacian ranks 30 and 32. For a Laplacian the removed row and column are redundant by zero sums, so the rank is unchanged for any root. Independently rebuilt both groups with permutation multiplication and replayed characteristic polynomials, modular incidence ranks, exact cofactor determinants and all local Smith layers at two other roots, 4 and 40 (python /workspace/branches/independent_replay.py 3 with SymPy). The unit-pivot Schur-complement layers modulo p^4 terminate before precision is lost, and the prime products match both exact cofactors. Nonunit factors with multiplicities for C6 are 3^×8,6,12^×2,36^×10,72,216; for S3 they are 3^×6,6,36^×12,72,216. These groups describe the constructed marked-incidence curves, not the whole plane divisor or arbitrary thicknesses.

## originality

PASS

Prior work proves group-net realization and the graph-to-component-group correspondence. The particular equal-spectrum/different-group result for the order-six incidence graphs, including the homomorphism obstruction and these integral decompositions, is distinct in the evidence inspected.

## value

PASS

The two groups of order six arise from a natural geometric and combinatorial pair, and the complete integral invariant distinguishes their boundary curves where all spectral and spanning-tree data agree. The homomorphism criterion identifies a structural reason in characteristic three, and the Smith computation shows precisely what the common spectrum loses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
