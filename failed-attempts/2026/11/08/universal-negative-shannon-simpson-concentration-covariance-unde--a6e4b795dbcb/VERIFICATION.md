---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The differentiated Dirichlet mixed moments give the exact decomposition with A=sum alpha_i, B=sum alpha_i^2 and weighted digamma covariance. Pairwise polarization and positive trigamma prove strict negativity for m>=2 and sharp equality iff all alpha_i coincide. Four independently evaluated beta quadratures checked the formula; finite calculations are not used as the all-real proof.

## originality

FAIL

The complete formula and sign/equality theorem were already proved on October 26 and re-proved on November 2 for every finite positive unequal Dirichlet concentration vector. The October formula with kappa=sum_{i<j}alpha_i alpha_j is algebraically identical after using 2*kappa=A^2-sum alpha_i^2. All asserted symmetric cases and Gini-Simpson sign are corollaries. This is decisive same-claim prior coverage.

## value

FAIL

Exact Shannon/Simpson dependence for heterogeneous Dirichlet posteriors is intrinsically worthwhile but the submitted claim is a verbatim rederivation of an earlier established exact function, sign and equality condition. No distinct unknown invariant, new boundary, interpretation or motivated mathematical contribution survives prior-coverage removal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
