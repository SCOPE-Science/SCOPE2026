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

# Reproduction and verification

Run `python3 verify.py` with Python 3 standard library. Expected output: `VERIFY_OK 720 exact matrix and optimum cases; 72720 rational rate bounds`. Exact rational checks verify all reported candidate costs, a full spanning set of eigenvectors, and the scalar feasible bound over 101 budget-grid points in each case. The boundary price equality is included among those cases for suitable parameters, including explicit interval checks.

The general theorem, the price threshold, and global optimality rest on the analytic concavity reduction and two-variable linear program written in RESULT.md, not on a finite computation. The checker does not establish full literature priority, classify all nonsymmetric optima, or perform independent mathematical audit.
