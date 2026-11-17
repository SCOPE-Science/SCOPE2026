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

# Reproduction and limits

Run `python check.py` with Python 3. The independent checker enumerates fixed-origin integer vertices of bounded-difference polytopes on product alphabets (2,2), (2,3), (3,3), and compares the exponential functional at several parameters with the claimed product constant. Directed incidence total unimodularity guarantees these integer points exhaust the vertices of those specific polytopes. It also tests the factor-ratio cut-size rule for 140 parameter/cardinality pairs and confirms the asymptotic Taylor envelope for 351 alphabet sizes.

All deterministic tests finish with `ALL_LIPSCHITZ_EXPONENTIAL_DIAGNOSTICS_PASSED`. No exhaustive computational inference is made for arbitrary product dimension, alphabet cardinality, or real parameter; the corresponding results follow from the written analytic proof. The arithmetic accumulation-set theorem relies on the density of irrational rotations, not finite numerical observations.
