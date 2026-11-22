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

The local-corner proof in RESULT.md is the mathematical evidence. The standalone `CHECK.py` (Python 3, `mpmath`) replays 23 finite corroborating assertions for the exact reflection identity, four projected singular coefficients at several parameters, the logarithmic increment at the critical exponent, and the inverse geometric formulas. Execute `python CHECK.py` from the same directory.

No simulation establishes the infinite-parameter theorem by itself. All claims require strictly positive rates, athermal stationary dynamics, and the generic projection assumption; reconstructing physical rates separately from the ratio requires an independent calibration of the trap relaxation rate. External audit has not been performed.
