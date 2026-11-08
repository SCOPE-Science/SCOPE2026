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

# Verification record

The package contains `verify.py`, an executable self-contained Python 3 program. From the directory containing the extracted files, run `python3 verify.py` using Python's standard library. This run returned `PASS: 952 exact-rational and deterministic consistency checks`.

The checker independently enumerates two-label candidate sequences for four rational corruption probabilities and batch sizes one through eight, checks both rows of the exact transition matrix, verifies the stationary mass and second eigenvalue for fixed batch size, and checks finite-horizon probability propagation for several nonconstant schedules. It also checks the strict order of the two critical logarithmic slopes for four numerical corruption parameters.

The almost-sure conclusions are analytic consequences of the explicit two-state kernel, Borel--Cantelli, infinite-product criteria and divergence of power series at exponent one. The code is a finite algebraic consistency test, not a computer proof of infinity or a replacement for the mathematical arguments in `RESULT.md`. Numerical parameter spot checks are not exhaustive. No independent audit was conducted.
