# Scientific review: Catalan matroid Hausdorff separation

## Correctness — PASS

The metric is the standard coordinate Euclidean norm on the common ambient space, not an intrinsic affine-model rescaling. The comparison polytope is the entire rank-\(n\) hypersimplex. Every Dyck word has fixed endpoints, and the simultaneous tight odd-prefix faces form an actual cube face, with all \(2^{n-1}\) binary vertices verified to be Dyck words. The Euclidean distance to this cube is calculated exactly pair by pair; its binary-vertex maximum is \(\lfloor(n+3)/2\rfloor\). A sharp projection normal certificate establishes that the ordered candidates attain the bound, while a feasible Dyck witness excludes every candidate with out-of-order pair types. Squared distance is convex, so the vertex bound holds for the entire hypersimplex, and equality confines the entire farthest locus to the specified vertex or edge. The constant common normal certifies all points of the even-rank edge. Independent SLSQP projection checks were exhaustive over hypersimplex vertices for ranks two through six; these computations are supplementary.

## Originality — PASS (provisional)

The closest prior published claims on these objects describe Catalan bases, lattice-path matroid face structures, alcoved triangulations, Gorenstein/Ehrhart invariants, and an intrinsic Euclidean inradius/incenter formula. These results do not state the proposed extrinsic Hausdorff gap or deepest-locus parity phenomenon, and their enumerative or inball conclusions do not logically determine that gap. Searches included metric-projection, Dyck/ballot, matroid proximity, and hypersimplex Hausdorff aliases in primary literature and published-finding corpus; neither exact equality nor dominating coverage was identified in accessible records. The full source title, relevant theorem statements, and pertinent sections of the cited primary texts were inspected, with residual risk that an alternative phrase or uncatalogued source contains the same theorem.

## Mathematical value — PASS

The problem compares two canonical geometric realizations of matroids and quantifies the worst possible Euclidean displacement induced by imposing the Dyck ballot constraints. The exact gap grows on the same \(\sqrt n\) scale as the ambient hypersimplex diameter. More substantively, the entire farthest-point locus changes dimension from zero to one according to rank parity; this requires identifying sharp projections on an exposed cube and excluding all other vertices and nonvertices. The result is a complete natural metric extremal classification, not merely a computational table or a restatement of the known face lattice.

## Closest literature, boundaries and risks

Ardila (2002) defines the Catalan matroid; Bidkhori (2012) and An–Jung–Kim (2017) analyze lattice-path matroid polytopes; Benedetti–Knauer–Valencia-Porras (initial preprint March 2023) study subdivisions and other polyhedral properties. The published Catalan inball result concerns an intrinsically measured radius **inside** the Catalan base polytope, rather than separation **from** the hypersimplex; neither statement implies the other. This work does not provide projections for arbitrary hypersimplex points. Priority is provisional until external independent mathematical and bibliographic review.

Self-review: passed. Independent audit: not yet performed.
