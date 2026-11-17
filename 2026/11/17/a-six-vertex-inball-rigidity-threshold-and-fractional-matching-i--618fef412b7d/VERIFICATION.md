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

# Verification record

The proof in `RESULT.md` gives an all-dimensional analytical derivation. `check.py` independently implements the facet-distance comparison in exact rational arithmetic for 997 integer values \(4\le n\le1000\), enumerates the 22 candidate vertices of the five-vertex fractional matching polytope, verifies all vertex-degree equations, and tests all remaining facet-clearance inequalities at those candidates. Convexity then covers the entire five-vertex center locus, while the proof covers all dimensions. Optional numerical LP checks compare complete facet systems for dimensions four to seven; their availability is not a prerequisite.

This check is reproducibility assistance, not an external certificate of novelty or an independent audit. All quoted bounds and the distinct-center classification depend on the analytic arguments, not on finite tests.
