---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For uniform independent parent choices, E S_i(k)=k/i by the one-subtree Pólya urn. For i<j, A=1_{j descends from i}, E[A S_j(k)]=k/(ij), and expanding S_i(k+1)S_j(k+1) gives mixed-moment recurrence U_{k+1}=(1+2/k)U_k+1/(ij), solved by U_k=k²/(ij). The singleton subtree equals a leaf, and direct telescoping of forbidden parent choices gives joint leaf probability (i−1)(j−2)/((n−1)(n−2)) and strictly negative covariance in the stated interior range. Beta-binomial diagonal variance and ancestor double-counting yield exact path-length variance. Boundaries i=1, j=n and n=2 are treated. New exhaustive rational checks covered every n<=8 (35 birth-index vector cases).

## originality

FAIL

Published October 25 and November 2 theorems already prove the identical finite-sample diagonal covariance matrix, weighted and unweighted path-length variance decompositions, and strict dependence of every nondegenerate pair. The November 2 young-forest result is strictly stronger through conditional mean independence; the October 26 ancestry-conditioning theorem gives exact dependence witnesses. The only extra displayed leaf-indicator covariance is the elementary telescoping of independent parent-choice avoidances, not a separate motivated unknown theorem.

## value

FAIL

The full diagonal covariance and its path-length decomposition are natural and useful, but are already known in stronger form. An extra two-leaf joint probability obtained by a one-line product is not a motivated independent mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
