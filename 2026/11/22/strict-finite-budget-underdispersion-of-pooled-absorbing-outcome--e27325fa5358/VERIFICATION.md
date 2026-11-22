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

The finite-budget theorem is proved by direct marked-renewal transform inversion and an everywhere positive hyperbolic power series. `check_variance.py` is self-contained apart from `mpmath` and independently generates second moments using a two-state tilted Markov generator. Its exact 61 consistency tests cover heterogeneous outcome rates, the equal-rate boundary, the long-time correction and series coefficients. A separate symbolic simplification verified the intermediate hyperbolic identity. These finite tests are not substitutes for the analytic proof and provide no external certification.

Run: `python check_variance.py`.

The underlying conditional exponential renewal model, first moments, and finite-deadline selection-bias mechanism are previously known and are not new claims. The historical prior comparison is documented in `REVIEW.md`; an older abstract-only source leaves an explicit priority risk. No independent scientific audit has been performed.
