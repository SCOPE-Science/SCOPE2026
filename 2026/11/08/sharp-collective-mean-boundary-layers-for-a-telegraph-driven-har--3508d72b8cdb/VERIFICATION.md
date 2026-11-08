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

The proof is an analytic derivation from the stationary conditional-Gaussian decomposition. `check.py` is an independently executable numerical diagnostic requiring Python 3 and `mpmath`. It performs high-precision beta-density quadrature and comparisons with the boundary-layer, exterior, and conditional-center formulas. The recorded run passed 40 primary and 6 supplemental assertions, including the exact uniform-center special case at three particle numbers. These tests do not prove uniform-in-parameter or infinite-\(N\) assertions.

To reproduce: run `python check.py` in a directory containing the extracted standalone file and an installed `mpmath` package. No external paper or research ledger is an input to the checker. The exact formulas and limitations are stated in `RESULT.md`.
