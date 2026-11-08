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

# Reproducibility

Execute `python VERIFY.py` with Python 3.9 or newer and no third-party dependencies. The program checks direct pivoted elimination against exact rational arithmetic on 1,204 inputs, deterministic midpoint quadrature against independently evaluated Gaussian upper-tail targets for two thresholds, 450,000 seeded Gaussian input matrices, and the symbolic Gaussian/Laplace constants. The observed output terminates in `VERIFY_OK`. The program uses a fixed seed and explicit tolerances; its simulations are finite sample checks, not a mathematical proof of asymptotic or universal statements. The analytic argument establishing the theorem is contained in RESULT.md. There has been no independent mathematical audit.
