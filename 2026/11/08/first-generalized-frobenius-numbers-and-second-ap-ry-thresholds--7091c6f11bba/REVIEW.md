# Scientific review of the near-arithmetic first generalized Frobenius formulas

## Correctness — PASS
The proof explicitly enumerates residue-constrained coefficient pairs, excludes every other congruence branch by strict cost inequalities, and derives the four-piece second-Apéry table, maximum, divisibility correction and genus by a finite residue sum. It handles \(m=3\) and \(h=m-1\) and proves every quantifier rather than extrapolating from the reproducibility test. An independent dynamic-programming route confirmed 3,916 parameter pairs in `verify.py` and `checks.txt`.

## Originality — PASS within inspected evidence
Komatsu–Ying's complete published treatment (2022 arXiv / 2023 open-access paper) concerns the arithmetic triple \(\langle a,a+d,a+2d\rangle\); it provides general Apéry methodology but does not imply the explicit non-arithmetic two-parameter classification here. Exact-family and parameter-alias searches, accessible historical claims, and indexed published research returned no covering result. The small intersection \(m=3,h=2\) is already an arithmetic progression and is not independently novel. An unindexed prior specialization or a hidden corollary of general three-generator formulas remains possible.

## Mathematical value — PASS
The result closes an exact representation-sensitive classification for a natural near-multiple triple, simultaneously producing all second Apéry thresholds, a generalized Frobenius formula, and a generalized genus formula. It explains the precise arithmetic origin of an otherwise unexpected divisibility-dependent one-unit jump, not a numerical-table recomputation.

## Limitations
No formulas for higher representation thresholds are asserted. Search cannot prove uniqueness. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
