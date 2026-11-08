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

Exact arithmetic: run `python verify_dense.py`. This checks every complement with maximum deleted degree below half the vertex count on 3–6 vertices, additional sampled graphs through 10 vertices, deletion-of-biclique constructions, the initial total-edge envelope on all integer pairs up to 100 vertices, and strict threshold inequalities through 9999 vertices.

The conceptual proof is in `RESULT.md`: diameter two, integer tight-edge potentials, biclique coupling, and monotonicity/equality cases. These finite checks do **not** establish the infinite statements without that proof. Independent audit has not been performed.
