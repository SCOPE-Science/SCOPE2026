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

The theorem is justified by the exact normal-fan and support-width arguments in `RESULT.md`, using a stated prior local-defect theorem. The accompanying `verify_antiprism.py` reconstructs the vertices, edges, facets, incidence lists and outward normals, and checks 39 numerical-combinatorial count identities for the thirteen base sizes \(n=3,4,\ldots,15\). The vertex-pair test solves support-direction feasibility by linear programming, while the edge-midpoint-pair test uses orthogonality to both edge directions and explicit normal-cone generators for parallel edges. All 39 checks passed when run using Python with NumPy and SciPy. Finite floating-point checks, even at very small tolerance, are corroboration rather than an infinite proof. No independent mathematical audit or external formal validation was performed.
