# Scientific review

## Correctness — PASS

The objects and quantifiers are explicit: one finite twelve-vertex graph defined by its twenty-four edges, the dominance complex of subsets whose complements dominate every vertex, and the rational action of the full graph automorphism group. Two logically equivalent face predicates agree on all 4096 subsets. A deterministic pivot matching pairs 3084 of the 3098 nonempty simplices, leaving exactly one vertex and thirteen six-dimensional cells. An exhaustive topological sort of all 16,648 oriented face-poset covering relations shows the matching is acyclic. Forman's theorem supplies the integral wedge homotopy equivalence. Exact graph automorphism backtracking obtains eight elements, and signed reduced Lefschetz traces computed on all 3098 simplices determine the rational character. The irreducible character multiplicities are nonnegative integers with total dimension thirteen. Separate mod-two boundary elimination corroborates the Betti numbers without being used as an integral proof.

The program `verify_chvatal_dominance.py` is self-contained and the exact output is recorded in `verification_output.txt`. The proof is finite and exhaustive, not experimental extrapolation. All reference orientations, the reduced-chain empty-face contribution, the two-generator dihedral relations, and the graph's degree and independence bounds are checked. The conclusion is *not* an integral representation decomposition or equivariant homotopy equivalence.

## Originality — PASS relative to inspected sources

The mathematical novelty is the exact dominance-complex integral homotopy type and full rational dihedral character, not the graph itself or its independence/neighborhood topology. A previously available exact same-graph result proves an equivariant collapse of the Chvátal independence complex onto its ordinary neighborhood complex, each a two-sphere. Neither statement determines the forbidden-closed-neighborhood complex. The ordinary neighborhood complex appearing in the Alexander dual of the dominance complex belongs to the **complement graph**, not the original graph. These are not interchangeable.

Marietti–Testa determine dominance complexes for forests, and Taylan for chordal graphs. Neither class contains the Chvátal graph. Matsushita gives a general connectivity estimate rather than an exact classification; Matsushita–Wakatsuki give the complement-neighborhood Alexander duality but not this case or its symmetry character. Published same-graph independence and neighborhood results were materially inspected and compared at the face-definition and implication levels. Searches for the named graph, dominance complex, dominating-set complement, closed-neighborhood avoidance, Alexander dual, sphere multiplicity and dihedral character found no inspected covering theorem. Matching a neighboring title or failing to find a text is not evidence of uniqueness.

**Residual risks:** an unindexed exact calculation, an implicit extraction from a not-yet-inspected classification, or independently known dihedral character. The original 1970 article was not read in full; it defines the graph rather than dominance-complex homotopy. No definitive priority certificate is claimed.

## Mathematical value — PASS

The Chvátal graph is a canonical minimal regular triangle-free four-chromatic example, so computing its dominance complex is a natural graph-topology test rather than selecting an arbitrary labeled graph. The calculation supplies a previously unavailable exact integral homotopy type and a complete symmetry character, strictly more information than Euler characteristic, mod-two homology, vertex-cover parameters or the known independence-complex two-sphere. The strict bound \(\operatorname{conn}(\operatorname{Dom}(G))+2=7<8=\tau(G)\) is a motivated consequence. The finite classification is meaningful in its own right; no downstream general theorem is asserted.

## Closest literature and limits

The closest comparison is the exact same-graph independence-to-neighborhood equivariant collapse and character, but its objects differ at the level of defining faces. Marietti–Testa (2007), Taylan (2015), Matsushita (2020), and Matsushita–Wakatsuki (2023) provide increasingly general dominance methods but not the present specific computation. The proof applies only to one graph and does not settle integral module splitting, infinite-family behavior, or unindexed-publication priority.

Self-review: passed. Independent audit: not yet performed.
