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

# Reproducibility and limits

The standalone Python checker `proof/q4_cut_verifier.py` was executed in its extracted directory. It regenerated the graph, facets and faces, checked the full directed discrete-Morse Hasse graph for acyclicity, checked every possible five-vertex Alexander-dual extension, and performed exact unit-pivot integral elimination on the Alexander-dual boundary. Output was byte-compared with `proof/q4_cut_verification.json`.

The mathematical deductions from the finite certificate are given in `RESULT.md`, especially the integral duality and attaching-map argument. The run proves a single finite four-cube case, not an infinite-dimensional statement. This record is a self-review, not independent external validation.
