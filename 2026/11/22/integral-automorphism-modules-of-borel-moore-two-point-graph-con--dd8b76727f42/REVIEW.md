# Self-review

**Correctness — PASS.** The compact symmetric-square pair computes Borel–Moore homology of the complement, the diagonal acts as multiplication by two on first homology, and an integral rectangle-basis cross-product argument constructs the natural second exterior power. The result is functorial under graph homeomorphisms. Exact cellular, Smith normal-form and signed-Lefschetz checks in `verify_bm.py` support the derivation but are not the infinite-family proof.

**Originality — PASS, with explicit residual risk.** Khan's 2026 Theorem 3.4 covers only the *abstract untwisted groups*. The October 2026 public exchange-sign Borel–Moore result identifies a different local coefficient system and a divided-square rather than exterior-square integral symmetry module; its full RESULT.md was read, including the untwisted rank-normalization remark. Classical symmetric-product functoriality supplies natural input and may make this refinement a short formal corollary; complete priority over unindexed or uninspected work cannot be certified. The new claim is the explicit *untwisted* integral automorphism-module pair, not the groups or the sign-twisted theorem.

**Mathematical value — PASS.** The module identifications determine arbitrary graph-automorphism actions on both torsion and free top BM homology, and distinguish a cycle-exchanging symmetry's negative top trace from a trivial action despite equal Betti ranks. They are uniform over all finite connected graphs and compute characters without configuration-cell enumeration.

**Limits.** No statement is made about ordinary singular homology, three-particle configurations, other local systems, or maps that merge particles. The code checks selected finite examples; the natural pair proof establishes the universal assertion. See RESULT.md for full sources and mathematical argument.

Self-review: passed. Independent audit: not yet performed.
