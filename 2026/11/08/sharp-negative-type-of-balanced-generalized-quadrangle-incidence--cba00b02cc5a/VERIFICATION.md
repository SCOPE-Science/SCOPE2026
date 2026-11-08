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

Reproduce the finite checks by running `python checker.py` using Python 3.9+ and NumPy. It constructs genuine symplectic point–line incidence graphs over the finite fields of orders two, three, and four; enumerates graph distances from every vertex; tests integer walk-polynomial identities and distance-shell cardinalities for every matrix entry; and tests the full real symmetric powered-distance spectrum at zero, half-threshold, threshold, reciprocal order, and exponent one. Successful output ends with `GQ_NEGATIVE_TYPE_EXACT_AND_SPECTRAL_CHECKS_PASS`.

The exact formula for all existing orders follows analytically from the recurrence identities, five-eigenspace decomposition and the uniform sign inequalities in RESULT.md. Finite checks do not prove the infinite family. Independent audit and independent validation are not performed.
