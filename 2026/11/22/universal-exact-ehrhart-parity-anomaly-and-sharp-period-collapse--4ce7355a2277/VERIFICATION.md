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

# Reproducibility

Run `python3 checker.py` with Python 3 and SymPy installed. The code enumerates all integer points by cyclic transfer recursion for each tested dilation, then performs exact rational polynomial interpolation. Sixteen cases, including one-half-vertex, integer-vertex, and infeasible-corner configurations, are checked. The script is evidence for those finite cases only; the proof of the all-dimensional theorem uses an exact parity decomposition of the tangent cone and Brion's identity.

Expected ending: `PASS cases=16`. The checker is included complete in the same package. There is no expert certification, formal proof assistant, or independent review.
