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
# Verification

Execute `python3 checker.py` using Python 3.8 or later (standard library only). Expected output: `VERIFY_OK 850 finite assertions`.

The checker numerically diagonalizes real-symmetric three-by-three pencils; it checks the quadratic coefficient on 180 deterministic triples at two small couplings, verifies two sharp Frobenius bounds on 120 triples, and checks the two closed-form families at five couplings. The analytical proof in RESULT.md is the basis for the full theorem. The numerical checks do not establish originality or higher-dimensional generalizations.

The theorem uses real diagonal perturbations; exact global width oscillation applies at arbitrary real coupling. The disk-distance formula for general diagonals is asymptotic. No external mathematical audit has been performed.
