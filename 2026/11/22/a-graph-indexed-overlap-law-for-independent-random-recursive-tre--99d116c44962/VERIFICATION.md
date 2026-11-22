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

# Verification steps and limits

Run `python3 verify.py` with the Python standard library from the directory containing this file and the checker. The direct-enumeration and independent per-arrival convolution paths agree for every tested complete overlap vector, and the graphic-rank, cycle-cumulant, forest-factorization, and Stirling marginal checks yield `VERIFY_OK 355 exact-rational assertions`.

The mathematical proof of the all-size PGF, cyclic cumulant, asymptotic Gaussian convergence, and analytic infinite product is in RESULT.md. Exact finite checks are reproducibility tests, not an infinite certificate. Historical priority is qualified by the stated residual risks. No independent mathematical audit has been performed.
