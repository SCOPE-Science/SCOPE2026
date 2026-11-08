# Mathematical assessment

**Correctness (PASS).** The proof handles the triangle separately, proves a local consecutive-four obstruction, constructs matching cyclic block witnesses, and builds a complete online depth-\((n-1)\) mistake tree. The chromatic-polynomial count and colour symmetry give a strict root-branch upper bound. Independent code verifies small cases and the constructions without replacing the all-order reasoning.

**Originality (PASS within accessible comparisons).** The closest concrete proper-colouring work, Blanca et al. (arXiv:1708.05118), concerns unknown-graph recovery from colouring samples, not fixed-cycle one-hot shattering. The zero-set theorem of Guingona et al. (arXiv:2109.04805) establishes equality of dimensions for a different class, and Walker's general tree-dimension theory (arXiv:2203.12211) does not determine the cyclic values. Path-colouring results do not imply a cycle's closure constraints. Semantic, alias, and literature searches did not establish prior equivalent coverage, but cannot exclude undiscovered earlier formulations.

**Mathematical value (PASS).** The theorem gives both exact dimensions uniformly on a natural connected graph family and quantifies how cyclic closure changes static and adaptive shattering relative to paths. It identifies a four-vertex local obstruction and a global online bound from colour-symmetry, explaining an unbounded gap rather than merely tabulating finite instances.

**Limits.** Three named colours and binary equality tests are essential. No all-support classification, historical completeness, or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
