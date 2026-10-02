---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For the PDNQP convexifying shift, a finite-step minimum Ritz value plus a fixed additive margin is not a deterministic positive-definiteness certificate; comparison-matrix weighted Gershgorin bounds give sparse-matvec lower certificates that monotonically approach the best positive diagonal-scaling bound and are exact for sign-switchable Z-matrices.

## Correctness — PASS

Rayleigh–Ritz gives the minimum Ritz value at least the true minimum eigenvalue, so the shifted minimum eigenvalue is exactly the margin minus the one-sided Ritz error. The diagonal family in the package has a benign m-dimensional invariant Krylov limit and continuity gives an open set of failing starts for every fixed m; an independent replay of the displayed m=8 example gave a shifted minimum eigenvalue about -0.989998629. The comparison-matrix quadratic-form inequality, weighted Gershgorin lower bound, monotone Collatz step, and sign-switchable exactness follow from the displayed matrix identities.

**Checked sources.** Assigned RESULT.md at tree 26e495e8f526d18680e7a4a86549204e75dfe0aa; artifacts/verify_convexification.py blob 45df15e4e83c687d88eeb7490df757640f073e79; Chen–Lu, arXiv:2609.19557; Urschel, arXiv:2003.09362

**Residual risks.** The record does not establish that any reported PDNQP experiment actually used an insufficient shift.

## Originality — FAIL

The mathematical content is mechanically assembled from standard extreme-Ritz ordering and classical comparison-matrix, diagonal-Gershgorin, Perron–Frobenius and Collatz–Wielandt facts. In addition, a separate published 2026-09-18 result gives a sharper PDNQP-specific finite-Lanczos certification boundary. The exact package wording need not appear in older literature for the audited claim to be covered by these stronger/general implications.

### Equivalent formulations

These are equivalent formulations of the two load-bearing mathematical steps, not merely related terminology.

### Broader coverage

The broader results dominate the assertion that a fixed finite Ritz estimate plus a small fixed margin cannot certify all symmetric matrices.

### Exact database or table

Database/table comparison is inapplicable because the result is a symbolic consequence of general matrix inequalities.

### Claim versus prior implication

The prior implications mechanically produce the headline obstruction and repair framework.

**Checked sources.** https://arxiv.org/abs/2609.19557; https://arxiv.org/abs/2003.09362; classical comparison-matrix and Collatz–Wielandt theory; published result dated 2026-09-18

**Residual risks.** The exact chronological ordering of the two same-day published records was not resolved; the classical theorem-level implication is sufficient for the originality failure independently of that ordering.

## Value — PASS

The source requires strong convexity, so distinguishing an estimate from a certificate is practically and mathematically motivated, and a sparse-matvec lower certificate is useful. The record fails acceptance because originality fails, not because the diagnostic problem is unimportant.

**Residual risks.** The repair can be conservative enough to be unattractive in matrices with favorable sign cancellation.

## Limitations

- The failure statement is conditional on the estimator being an ordinary Ritz value without a separate certified lower bound.
- The comparison-matrix certificate may be conservative and floating-point certification requires directed rounding or an explicit safety allowance.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
