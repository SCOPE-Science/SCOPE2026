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

## Reproduction

From the extracted directory run `python3 -m pip install -r requirements.txt` in an appropriate environment and then `python3 verify.py`. Exact symbolic identities for the cubic Hermite contact expression, moment matching and Gauss amplification are checked using SymPy, followed by 808 exact-rational supplementary sign checks.

## Logical boundaries

The sign of the explicit rational interpolation remainder proves the universal inequality over arbitrary Borel measures. A nonsingular confluent Vandermonde Jacobian and the implicit-function theorem establish existence of an admissible improving three-atom perturbation below the stated transition. Numerical tests only check selected instances, not the universal claims. The stability result concerns real negative scalar test parameters and independent stage choices; no general complex-half-plane or nonlinear claim is made.

Independent audit: not performed.
