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

The self-contained `check.py` uses Python 3 standard-library arithmetic and trapezoid integration. Execute `python3 check.py` from the directory containing that file. The replay result for the included code is `PASS: 5539 finite exact and quadrature diagnostics`. The exact checks independently implement finite moment recursions from the inverse transform; numerical checks probe the sharp comparison interval for multiple depths, parameters and Laplace values. The analytic proof in `RESULT.md` establishes the all-depth/all-argument claims. Numeric integration cannot certify uncountably many probability laws, and the checker does not attempt to do so. Independent audit: not performed.
