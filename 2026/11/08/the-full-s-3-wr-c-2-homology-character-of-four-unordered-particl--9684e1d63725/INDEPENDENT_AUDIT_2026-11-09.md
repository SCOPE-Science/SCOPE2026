# Independent mathematical audit

## correctness

PASS

PASS: The weight-four reduced Swiatkowski model for B4(K3,3) has exact chain dimensions (495,1980,2700,1440,240), differential from halfedge differences to edge-variable differences, and integral chain-square zero. Inspected source implements unimodular unit-pivot Schur reductions: ranks d1=494, d2=1482 with one invariant factor 2, d3=1199 and d4=240, yielding rational Betti (1,4,19,1,0) and integral H1 torsion Z/2. The 72-action on the weight-four chain model is implemented with local 2D halfedge-difference matrices and Koszul signs. An independently written orbit-determinant Lefschetz computation reproduced all nine supplied representative H2 traces when combined with the graph-cycle H1 character and the rank-one H3 action. Source top-cycle code uses a nonboundary mod-101 class, checks its image modulo im(d4) under all 72 elements, and uses the proved integral rank one to lift +1 signs. The exact integer Smith and 72-element top-cycle programs were inspected but not independently rerun in full; this is retained as a finite verification limitation, not represented as extra certification.

## originality

PASS

PASS (best of knowledge): Current exact claim not covered by a prior identified statement; remaining literature risks are explicit.

## value

PASS

PASS: The complete 72-symmetry rational second-homology representation and the exceptional third-homology orientation of four indistinguishable particles on K3,3 are natural exact invariants for an important minimal nonplanar graph. The 19-dimensional Betti number and geometric generators were known, but deriving the precise nine-class character and wreath-product irreducible decomposition requires nontrivial signed actions and identifies invariant sectors not implied merely by the ranks. No family-wide theorem is required for this exact motivated case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
