# Self-review

## Correctness — PASS
The reduced Coxeter words are two disjoint adjacent-swap batches. The subword property identifies every vertex. A two-coordinate lemma bounds each output pair by 18 in the interior and 8 at a boundary, and characterizes equality. An endpoint indicator difference costs at least 3 or 5 locally while gaining at most 1, so it never improves the diameter. The four parity/orientation cases sum to the claimed exact formulas, and equality forces all first-batch swaps plus complementary second-batch choices. Strict convexity excludes continuous nonvertex maximizers. The checker verifies all local binary cases, every vertex pair for n=3 through 10, and larger reproducible witnesses. These finite computations are not the all-order proof.

## Originality — PASS, provisional historical priority
Tsukerman–Williams's 2014 Theorem 4.24 explicitly concerns *graph-theoretic* diameter, proven by edge-path lengths; its formula n-1 cannot supply the Euclidean theorem. Gaetz's 2022 article studies 1-skeleton lattices, normal fans and smoothness and uses inverse-permutation vectors rather than the ordinary one-line realization of this claim. The 2025 Coxeter subdivision paper studies regular subdivisions and Euler-number counts for zigzag elements, not Euclidean farthest-vertex pairs. Search queries for the Euclidean invariant, its equivalent two-layer-swap description and both explicit formulas produced no dominating result among the inspected sources. A prior equivalent result in another convention or an unindexed source remains possible. The complete structured comparison is in AUDIT.json.

## Mathematical value — PASS
The theorem supplies sharp geometry for an infinite and independently motivated family of generalized permutohedra: two exact Euclidean diameter laws, a parity-dependent two-unit squared-diameter gap, and the entire exponentially sized diametral-pair matching. This contrasts with the known orientation-independent combinatorial graph diameter, giving a concrete boundary between metric and combinatorial polytope invariants. It is not a finite-data extrapolation or a renaming of a graph-distance theorem.

## Scope and limitations
Only bipartite zigzag Coxeter words and the ordinary one-line embedding are covered. No face-lattice equivalence, all-Coxeter-element classification, historical priority certification or independent validation is claimed. The dated literature lead is Gaetz's 2022 preprint; the 2014 foundational definition is a separate background source. Exact source inspections and remaining risks are recorded in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
