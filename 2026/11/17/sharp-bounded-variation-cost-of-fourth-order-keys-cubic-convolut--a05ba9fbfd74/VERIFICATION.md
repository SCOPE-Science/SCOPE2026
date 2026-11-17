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

Run `python checker.py` with Python 3 and SymPy installed. The checker reconstructs the five cubic response pieces from the kernel, symbolically verifies their reflection identity and cardinal partition of unity, verifies the exact stationary point and radical constant, checks the four-tap comparison, and independently stress-tests 125 finite-jump vectors by numerical integration. The exact identities all passed in the packaged source before acceptance.

The random stress test checks only finitely many examples and is not a proof of the sharp statement. The general, infinite-dimensional statement follows from the analytic jump decomposition in `RESULT.md`; the equality witness is an actual unit-step sequence, not an approximation to an unattained supremum. The proof establishes neither priority over all unindexed literature nor a statement for boundary-conditioned finite images.
