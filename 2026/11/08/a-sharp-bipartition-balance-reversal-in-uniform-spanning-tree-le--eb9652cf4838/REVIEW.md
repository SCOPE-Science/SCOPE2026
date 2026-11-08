# Mathematical review

**Correctness — PASS.** For \(a\ge2,b\ge1\), the proof explicitly derives the weighted effective resistance by Kirchhoff's current equations, applies the exact one-edge tree-update identity, extracts each leaf probability from the degree-generating polynomial, and establishes the sign boundary with strict integer monotonicity. The difficult boundary cases are checked separately, including \((a,b)=(2,1)\). A self-contained exact-arithmetic implementation independently verifies weighted cofactors, exhaustive small-instance leaf expectations, and the finite sign grid. The checker does not certify the infinite claim; that is supplied by the symbolic proof.

**Originality — PASS, with priority risk.** Klee–Stamps/Clark provide the unperturbed complete-multipartite weighted enumerator; this work does not claim that identity as new. Dong–Ge give forest-containing counts in the original bipartite graph, and Rapoport gives general finite-graph degree formulae. The inspected papers and targeted research-record searches did not identify the all-parameter, within-part-edge expected-leaf response or its exact sign reversal. The present theorem is not the same as an existing-edge conductance tilt, which leaves the graph's edge set unchanged. Broad enumerator tools permit derivation but do not state the evaluated result; an unlocated earlier specialization remains possible.

**Value — PASS.** Edge addition need not monotonically change the expected number of leaves in a uniform spanning tree. The answer has a natural full-dimensional classification for every bipartition shape, a sharp balance boundary and one exceptional equality, rather than an arbitrary finite sample or an isolated counterexample. This complements classical spanning-tree enumeration by resolving a concrete random-tree sensitivity invariant.

**Limits.** Only one added within-part edge and the expectation of the number of leaves are settled. No statement about stochastic domination or multi-edge perturbations is implied. Historical priority is not independently established.

Self-review: passed. Independent audit: not yet performed.
