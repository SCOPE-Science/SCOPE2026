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

# Mathematical verification

The proof gives an exact formula for every finite connected positive-length metric graph, independent of numerical sampling. Run `python3 verify.py` using Python 3 standard library. The program uses `fractions.Fraction` for every length, resistance, linear solve, and comparison. Its checking route inserts the evaluation point as a graph vertex and independently solves the ground-fixed Kirchhoff Poisson equation for a delta source minus uniform arclength; the exact quadratic interior correction then recovers the centered pointwise Green diagonal. For ten explicitly specified networks and six rational sample positions per edge it performs 294 exact comparisons against the stated resistance envelope and verifies ten Foster/curvature sums and the envelope's dominance. The program printed `ALL_UNIVERSAL_GRAPH_ENVELOPE_CHECKS_PASSED` in the actual replay. Random values, finite grid checks and timeouts are not asserted to establish a theorem. All-dimensional conclusions rely on the proof in `RESULT.md`. Independent mathematical audit: not performed.
