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

# Reproducible finite checks
Run `python3 verify.py` using only the Python standard library. The expected marker is:

`BOUNDED_PARTITION_SHATTERING_PASS 22 202014 16 140`

The first count corresponds to parameter pairs with complete direct trace tests through six vertices, the second to examined query supports, the third to exact finite online-rank cases, and the fourth to independently enumerated component-size facet spectra. The checker builds concepts by independent enumeration of restricted-growth partition strings and tests shattering through distinct trace masks. A separate union-find check tests the forest criterion, a Cayley recurrence checks polynomial coefficients, and a recursive minimax checks finite Littlestone dimensions. Verification is exhaustive over the stated finite ranges only and is not a proof of generality. The general mathematical arguments are recorded in RESULT.md. Independent external audit: not performed.
