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

The standalone script `artifacts/verify.py` performs exact integer and rational calculations. It directly constructs every small layered graph in the stated finite testing domain and counts shortest paths by breadth-first search independently of the layer-product formula. It checks the eight reduced-tail profile values and exact maximizing-tail recurrence through total tail size 90, and the three closed geodesic formulas for 35 choices of central-run length.

Run: `python3 artifacts/verify.py`.

The unrestricted theorem depends on the proofs of the layer-product count, the tail recurrence and its four local replacements, and the finite eight-profile comparison. The computational tests are not a substitute for these unrestricted arguments. Historical originality is provisional and not independently audited.
