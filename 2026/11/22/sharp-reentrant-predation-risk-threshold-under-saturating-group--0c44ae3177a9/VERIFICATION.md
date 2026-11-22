---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible mathematical checks

The proof is contained in RESULT.md. It states the exact positive domain and derives the quadratic \(G\), the strict logarithmic concavity identity for \(H\), equality cases, and two explicit boundary asymptotics. The supplied standalone program CHECK.py (Python 3.9+; standard library only) was run from this package and reported **15,159 diagnostic assertions passed**. The program exercises exact-rational derivative identities, positive-hump discriminant conditions, strict log-curvature signs, two stationary points for one explicit parameter set, and numerical consistency with both asymptotic limits.

Checks in the script are finite and do **not** prove a theorem about all real parameters. The analytical identities and sign arguments in RESULT.md are required evidence; the checks are a reproducibility supplement. No formal prover, external certification, independent audit, empirical fitting, or historical priority certification was performed. Inaccessible full texts and model restrictions are specified in REVIEW.md.
