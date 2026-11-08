# Scientific review: minimum global locating-domination in two strongly regular graphs

## Correctness — PASS

The precise object is the Shrikhande Cayley graph and the \(4\times4\) rook graph, both given by complete adjacency rules. The filter for globality is proved from complement-neighborhood traces, not assumed. Complete enumeration covers every subset of size at most five, so smaller counterexamples cannot be missed. All feasible five-codes, forbidden five-neighborhood sets, potential exchanges and all-pairs shortest-path distances were checked. Independent set-based and bitmask implementations agree. Automorphism-orbit counts are checked by explicit permutations, with upper bounds on vertex stabilizers proving completeness of the described groups. There is no claim beyond these two finite graphs.

## Originality — PASS (qualified)

The 2013 global location-domination work establishes the predicate and general bounds, not the complete two-graph minimum-code census. The 2014/2015 strongly-regular identifying-code work uses a strictly stronger closed-neighborhood predicate; its graph-parameter bounds do not force the enumerator of global location-domination codes. The 2023 binary locating-domination study bounds larger rook-product cases but does not report the four-by-four global optimum multiplicity. Previously documented calculations on the same graphs concern different invariants, such as identifying codes, metric/edge bases, independence complexes, and induced matchings; no statement-level implication yields the exact 1488-versus-1872 distinction and complete relocation data. An accessible abstract of the 2015 optimal-code ensemble paper is insufficient to exclude graph-specific results within its unavailable full text. Unindexed historical tables remain a priority risk. Index searches alone do not establish novelty; the conclusion rests on the specific comparisons and their disclosed limits.

## Value — PASS

The two graphs are a canonical nonisomorphic pair with identical strongly regular parameters; measuring an optimum-code enumerator naturally probes the limits of spectral/parameter data in domination theory. The exact 384-code discrepancy is a meaningful structural separator, not an arbitrary parameter slice. Exact exchanges and automorphism orbits refine the interpretation of the distinct optimal placement spaces. The result does not require an infinite extension to be useful, and the entirely enumerated configuration spaces make the finite conclusions reproducible.

## Scientific limitations

The theorem is a finite exact statement, not a universal enumeration method. Existing general inequalities and generic code-reconfiguration machinery remain background. Inaccessible full primary material and unindexed tables warrant cautious originality language. No external independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
