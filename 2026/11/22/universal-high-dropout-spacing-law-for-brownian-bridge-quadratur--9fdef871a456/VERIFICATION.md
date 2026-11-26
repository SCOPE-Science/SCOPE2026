---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

The claim concerns expected posterior mean-square error for the Brownian-bridge integral with independently lost exact readings, with a fixed budget of at least three sensors. The gap-cube formula, uniqueness on the ordered simplex and high-dropout spacing law are proved analytically in `RESULT.md`.

To perform the supplied finite numerical checks, install the dependencies in `requirements.txt` and run `python verify_dropout.py`. It compares floating-point covariance and conditional gap formulas for several finite examples, compares small-network numerical optimizers to the leading term, and checks the exact two-site stationarity equation as a reference case, not as a distinct finding. The tests are not a proof of the asymptotic statement or of global optimality.
