---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With c cyclic vertices fixed and m=n−c>0, deleting the root rows/columns from the outgoing forest Laplacian with s forbidden targets gives (n−s)I−1aᵀ with aᵀ1=m−s. Its determinant is c(n−s)^(m−1), so the ratio to c n^(m−1) supplies exactly the subset-avoidance probabilities; inclusion–exclusion supplies the full indicator law. For c=n all vertices are hit. The successive mean difference also works at c=n−1. Conditional on a fixed vertex being unhit, the uniform mapping on the complement has the same cyclic count as the full mapping, yielding the exact covariance. Telescoping gives h_n(c)−E R_n=−q^(n−1)+∑_{j<c}(j/n)q^(n−j−2), uniformly giving the claimed limit for admissible c_n=O(√n). The bound 1+c²/(2n) also holds at c=n: the last summand exceeds its j/n bound by exactly 1/n, covered by the slack. The exact cyclic tail is (n)_c/n^c, giving Rayleigh moment convergence by the birthday bound. Thus the covariance coefficient is e^(−1)Cov(X,X²)/2=e^(−1)√(π/8), and Var(R_n)/n=q^n(1−q^n)+(n−1)[(1−2/n)^n−q^(2n)] tends to e^(−1)−2e^(−2). The stated correlation follows. The frozen exact and numerical test code was inspected, not executed.

## originality

FAIL

An earlier distinct published record, Resultary 007c2a04bfe9, already gives the same exact conditional occupancy law, a conditional leaf-mean expansion implying the same centered quadratic regression, and the same signed square-root covariance after R=n−L. It also gives the exact cyclic marginal. Multiplying that marginal by the known conditional leaf mean and simplifying immediately gives the asserted finite-size expression; the correlation normalization is routine. The failure is established prior coverage, not an access risk.

## value

FAIL

The conditional law and quadratic regression are meaningful mathematical facts, but the frozen claim offers no independently substantive addition beyond the earlier exact leaf result. The image reformulation, one-line collapse of its finite covariance sum and routine normalization by the marginal variances do not supply an independent research contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
