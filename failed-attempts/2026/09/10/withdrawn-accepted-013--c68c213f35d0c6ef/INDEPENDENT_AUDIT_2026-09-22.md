# Independent audit — SCOPE-20260910-013

## Scope
Independent review of `2026/09/10/013` at Git tree `9cac7606ed2758ebc06e561a8365c27a30fea1dd` for task `20cb4fb0f42f361f7a14d25d084c5c02`. The current `main` tree matched the assigned source snapshot, so the scientific assessment used the assigned package without a stale-tree substitution.

## Correctness
**PASS**

Independent exact Fraction arithmetic reproduces vol(R_s)=(4s+7)/12 for s<=1/2 and s+1/4 for s>=1/2, the stated polar slab formulas, P(3/8)=8126/729, P(1/2)=11, P(5/8)=21728/1875, and threshold margin 17/75.

The two concavity certificates are valid: H''(u)=28u^2(5u-96/7)<0 on [4/3,2], and S''(t)=36t^2-24t-128<0 on [8/5,2]; endpoint values therefore prove P(s)>=11 with equality at s=1/2.

The committed verifier is self-contained and its exact claims agree with the independent arithmetic.

## Originality
**PASS_NARROW**

Targeted searches of the cited Mahler/Hanner stability literature did not locate this exact one-parameter family R_s=conv{±e_i,±s(1,1,1,1)} or the exact minimum 11. The formula appears to be a narrow explicit-family calculation rather than a restatement of a located theorem.

This is deliberately not an unconditional novelty claim: the search was targeted, and general local-minimality/stability theorems for the cube/Hanner orbit already cover the surrounding qualitative landscape.

## Scientific value
**FAIL**

The result treats only one elementary one-parameter stacking path and establishes no stability modulus, structural theorem, or progress on the four-dimensional symmetric Mahler conjecture. The arbitrary 1% decision threshold adds no intrinsic mathematical content beyond the exact minimum 11.

Prior work already proves strict local minimality of the cube/Hanner polytopes (and, by polarity, the cross-polytope) in broad neighborhoods. An exact exercise on one prescribed path can be useful as a benchmark but does not by itself meet the audit's scientific-value bar for an accepted finding.

## Reproducibility
Status: **reproduced**.
- Exact endpoint products and 17/75 threshold margin recomputed with rational arithmetic.
- Piecewise volume and polar-volume formulas independently algebra-checked.
- Concavity endpoint argument independently checked.
- Limitation: METADATA.json lists output/artifacts/verify_gap.py although the committed record path is artifacts/verify_gap.py; RESULT.md itself uses the correct committed path.

## Literature checked
- [A remark on the Mahler conjecture: local minimality of the unit cube](https://arxiv.org/abs/0905.0867): Proves the unit cube is a strict local minimizer of the symmetric Mahler product.
- [Minimal volume product near Hanner polytopes](https://arxiv.org/abs/1212.2544): Proves every Hanner polytope is a strict local minimizer; cube and cross-polytope share the Hanner minimum.
- [A Discrete KKT Variational Characterization of the Local Minimality of the Mahler Volume in Centrally Symmetric Polytopes](https://arxiv.org/abs/2606.14709): Provides a 2026 variational/local-stability treatment of the Hanner orbit, underscoring that broad local stability is already the substantive theorem-level object.
- [Symmetric Mahler's conjecture for the volume product in the three dimensional case](https://arxiv.org/abs/1706.01749): Establishes the symmetric conjecture in dimension three; dimension four remains the first unresolved symmetric dimension.

## Limitations
- The exact-family calculation may be a useful benchmark, but the audit does not infer global novelty from a failed exact-string search.

## Conclusion
The package is scientifically **failed** under the three-axis audit because at least one required axis fails. Relocate the complete original package atomically to the assigned failed path, preserving all original evidence. The relocation is a publication-status decision, not a claim that every underlying computation is false.
