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

Run `python3 verify.py` with Python 3.9 or later; no third-party modules are needed. The committed `verify_output.txt` is the direct stdout from executing that script. The verifier independently enumerates directed edge subsets and tests every face's in/out degrees and directed acyclicity. It checks the mod-two reduced homology, exact decomposition into incident reverse-arc cones, and the dominated-vertex adjacency conditions in the disjoint case, for all three patterns with \(2\le n\le10\).

The global result for all \(n\ge2\) rests on the mathematical reduction in `RESULT.md`: cone-union suspension for incident arcs, uniform link domination for disjoint arcs, and tetrahedron-boundary identification at the small base. A finite test, even when exhaustive at its tested sizes, does not certify all sizes. No independent audit or external certification has been performed.
