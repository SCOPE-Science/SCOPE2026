# Independent mathematical audit

## correctness

PASS

The target graphs are explicitly R=K4 square K4 and S=Shrikhande on (Z/4)^2, both (16,6,2,2), and Hom(C5,H) uses five nonempty sets with complete bipartite adjacent-coordinate conditions; the source is the unfilled cycle and no dihedral quotient is taken. I independently constructed both graphs and all Hom cells by growing from every singleton homomorphism; subset heredity proves the enumeration exhaustive. Each produced exactly [7680,30720,45120,36480,20160,6720,960] cells by dimensions 0..6, total 147840; two 3840-vertex components and 23042 independent integral graph cycles. The signed cellular 2-boundary is the alternating product-simplex boundary. An independently implemented sparse integer-column unit-pivot reduction (true unimodular operations) gave for the rook 22950 unit pivots followed by a rank-2 matrix with gcd entries 2 and gcd maximal 2x2 minors 4, hence Smith factors 2,2, free rank 23042-22950-2=90. For Shrikhande it gave 22982 unit pivots, zero residual, free rank 60. Separate independent exact GF2/GF3 cycle-lattice rank computations gave rook first Betti 92/90 and Shrikhande 60/60, agreeing with torsion. This is an exhaustive computation of precisely these finite cells, not an inference about general strongly regular graphs.

## originality

PASS

PASS best-of-knowledge. The square-free-codomain graph-Hom theorems cannot apply: each of R and S contains 4-cycles (nonadjacent pairs share two common neighbors). Earlier spectral clique-complex, open-neighborhood, forest and cut-complex computations on the same cospectral graph pair are mathematically different functors; none of the read material supplies Hom(C5,R/S) integer H1 with two Z/2 classes versus torsion-free H1. The equal full face vector plus different integral H1 is a specific natural graph-Hom invariant, not a recomputation of a known table.

## value

PASS

The Shrikhande and rook graphs are the canonical nonisomorphic strongly regular parameter twins. Equality of every polyhedral Hom cell count yet unequal free ranks and actual integral 2-torsion shows exactly what combinatorial face counts and strongly regular parameters fail to determine. First integral homology of the ordinary Hom complex of an odd cycle is a natural unknown invariant that future graph-topology work could require, and exact finite classification is worthwhile independently of higher-homology completion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
