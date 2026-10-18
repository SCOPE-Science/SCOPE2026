# Independent mathematical audit

## correctness

PASS

For finite connected complete multipartite graphs, geodesic 3-vertex sets at d>=2 are exactly part multiplicity 2+1; diameter <=2 makes this independent of d. Three-uniform clique maximum is 2 if no part has >=2, 3 if exactly one part has >=2, and 4 if at least two do. Monochromatic 2+1 avoidance gives chi=1 in the trivial all-singleton/edgeless cases; in two parts or with <=one nonsingleton part or max part<=2, explicit two-colorings work. K_(3,2,1) cannot use two colors because a pair must repeat in the three-part and forces a 2+1 triple in the remaining color; its omega is 4. Hereditary closure and the part-profile embedding show that any r>=3 with max>=3 and >=2 nonsingleton parts contains K_(3,2,1), and every smaller deletion avoids it. Independently enumerated 36 complete multipartite profiles through seven vertices and all induced profiles, corroborating the proof.

## originality

FAIL

The exact result follows directly from two already published exact formulas: Chandran et al. (2025) Theorem 5.1 gives chi_gp for EVERY complete multipartite part-size profile; by the 2+1 geodesic identity this equals chi_d^3 for d>=2. Published Oct 4 SCOPE clique theorem gives omega_d^3=2+min(2,s), s=#n_i>=2. Their inequalities imply chi=ceil(omega/2) for every induced multipartite subgraph iff max part<=2 or s<=1 (or <=2 parts). The unique forbidden K_(3,2,1) is the elementary minimal failing part profile. New perfection vocabulary and the number-independent-of-d statement do not create mathematical novelty from this known combined implication.

## value

FAIL

The proposed obstruction characterization is true but is a short direct arithmetic combination of the existing exact chromatic and clique formulas for the same natural class, with one minimal forbidden profile check. Under the required value bar this is a routine corollary/known-formula recombination, not a fresh valuable unknown invariant or motivated new structural result. It cannot be accepted under changed terminology merely because an older initiating article poses an open question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
