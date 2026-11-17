# Independent mathematical audit

## correctness

PASS

Writing S=A∪F* makes domination equivalent to V\V(F)⊆A, since every unselected middle edge-vertex has an incident selected original vertex or a different selected incident middle edge. For each selected root vertex use one adjacent root neighbor and domination to find a distinct selected vertex at distance≤2; for each selected middle edge use an extra incident edge (guaranteed by connectedness and n≥3) plus domination to find a selected distance-two witness. This proves all-set equivalence, not merely equality of minimum sizes. Summing choices of A for fixed F gives ∑_F z^{|F|+n-|V(F)|}(1+z)^{|V(F)|}. Coverage-capacity equality yields only perfect matchings at even order and two disjoint odd-order cases (one root vertex plus matching, or one doubly covered root) with counts P_n:1 or n and C_n:2 or 2n. Independent exhaustive checks all connected labeled roots n=3,4, and all path/cycle optimizer sets through n=7 corroborate. K2 is a genuine excluded boundary.

## originality

PASS

PASS best knowledge: earlier minimum independent/semitotal domination and minimum edge-cover results do not imply all-set equivalence or every polynomial coefficient. A 2026 result about TOTAL (adjacency-only) domination of middle graphs also computes a different polynomial, not semitotal. The arbitrary-dominating-set witness is nontrivial and new relative to inspected antecedents.

## value

PASS

PASS: a genuine all-feasible-set collapse of a distance-two domination condition on the natural middle-graph construction is stronger than a previously known scalar coincidence. An exact polynomial and complete parity-sensitive optimizer counts for paths and cycles are independently useful natural invariants, not unmotivated small-case recomputations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
