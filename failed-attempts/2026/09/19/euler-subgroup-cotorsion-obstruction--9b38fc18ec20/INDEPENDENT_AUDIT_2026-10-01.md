# Independent audit — SCOPE-20260919-9b38fc18ec20

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For every subgroup \(B\leq\mathbb Z\), the Euler-subgroup restriction preserves complete ideal cotorsion while object completeness holds exactly for \(B=\mathbb Z\), including the zero-Euler case and idempotent-completion statement.

## Correctness

**PASS** — The exact-category and cotorsion arguments reconstruct correctly. Euler additivity gives the Frobenius subcategories; the stalk/adjacent-stalk tests detect the orthogonals, the explicit cone constructions give special ideal approximations for every \(B=d\mathbb Z\) including \(B=0\), and the long exact sequence gives precisely the two truncation-Euler conditions. The witnesses with Euler characteristic zero show both directions fail for every proper subgroup, and the direct-summand constructions give the asserted idempotent completion.

## Originality

**FAIL** — FAIL because the published 2026-09-18 SCOPE record `euler-subgroup-cotorsion-obstructions--43f18172987b` already gives this theorem one day earlier, including the same category, object ideals, complete ideal cotorsion pair, exact two obstruction classes, completeness iff \(B=\mathbb Z\), and idempotent completion. The 2026-09-17 finite-Grothendieck-quotient record already covers the finite-index portion as well.

The audit separately checked equivalent formulations, broader coverage, exact database/table overlap, and claim-versus-prior implication. Full source-inspection details and residual risks are recorded in the companion JSON.

## Scientific value

**PASS** — PASS in intrinsic mathematical value: a sharp all-subgroup classification, including the zero-Euler case and exact object-approximation obstructions, is a natural structural result. It nevertheless cannot be accepted because it is already covered.

## Disposition

**FAILED.** A validated finding requires correctness, originality, and value all to pass. The original scientific files and reproducibility artifacts are retained with the failed-attempt package.
