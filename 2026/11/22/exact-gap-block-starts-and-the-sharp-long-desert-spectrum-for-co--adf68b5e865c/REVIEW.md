# Self-review: consecutive-triangular semigroup gap blocks

**Correctness — PASS.** The Apéry normal form follows from two exact generator trades and pairwise distinct residues. Adjacent Apéry thresholds classify every gap start and give the parity-dependent block count. A separate q-coin layering argument classifies all blocks longer than \(n+1\); no numerical sample substitutes for either infinite proof. The attached `verify.py` matched the exact predictions through \(n=120\) for starts and \(n=60\) for full gap enumerations; it also uses separate coin-change DP through \(n=28\). The remaining shorter-block length histogram is not claimed.

**Originality — PASS on inspected comparisons.** Robles-Pérez–Rosales (2017) established the same Apéry rectangle, while Komatsu (2022) established different generalized Frobenius thresholds. The closest published result on isolated gaps of the same triangular family determines only singleton gaps; its full result and proof were inspected and the shared Apéry input is expressly acknowledged. Neither establishes the long-desert cutoff and full all-block-start count. The all-start part is close to the published rectangle; a general implicit theorem or unindexed table remains a priority risk.

**Mathematical value — PASS.** The exact number and positions of maximal intervals missing from a natural numerical semigroup convey genuinely different structural information from its Frobenius number and genus. The sharp \(n+1\) separation identifies every exceptional large desert by a coin-count-layer proof valid uniformly for all admissible indices.

**Scientific limitations.** The complete length spectrum of shorter blocks is not obtained, and general three-generator numerical semigroups are not classified. The statement is a self-review, not externally certified priority or independent verification.

Self-review: passed. Independent audit: not yet performed.
