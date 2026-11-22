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

Run `python checker.py` with Python 3.9 or later. It uses only the Python standard library, expands the coefficient polynomial separately from the inclusion–exclusion formula, evaluates the exact finite Fourier expression, tests the parity-dependent vanishing orders, compares numerical circular quadratures and arc leakage, and checks the Jackson-square asymptotic. On the packaged source the expected completion marker is `ALL_POWERED_FEJER_JACKSON_CHECKS_PASS`.

The infinite-dimensional BV inequality, the uniqueness of extremizers, and the all-degree parity rigidity are **proved analytically** in RESULT.md. Numerical quadrature and finite exact arithmetic are independent supporting checks only; they are not general-integer or universal-function certification. No external independent audit was performed.
