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

# Reproduction and boundaries

`antiprism.py` is a standalone Python-standard-library exact-chamber checker. It works with degree-three coefficient vectors for the algebraic number \(t>0\) satisfying \(t^4=2\), performs arithmetic modulo that polynomial, and determines signs using nested integer square roots and rational bounds. Its assertions verify the 16-edge antiprism graph, no triple concurrency among eight normal great circles, all 58 feasible sign chambers, and exact cut-edge counts 24 hexagon chambers and 34 octagon chambers. Numeric spherical areas are secondary consistency checks only.

`CHAMBERS.txt` supplies the compact complete eight-bit sign-chamber certificate. A bit is one for a positive dot product with that indexed vertex. Every possible generic orientation belongs to one of the 58 masks because the great-circle arrangement has 56 intersection vertices and 112 arcs.

`independent_check.py` uses SciPy and NumPy to sample 300,000 independent uniform normal directions and directly construct 300 section convex hulls. The observed octagon frequency lies within five binomial standard errors of the exact closed-form value. `family_check.py` repeats the angular-law test at five distinct positive heights with 100,000 normals each.

The general parameter-law formula and monotonicity are established analytically in `RESULT.md`. The code does not purport to prove publication priority, provide an independent proof review, or certify floating-point probability digits. All arguments apply only to nondegenerate positive-height right square antiprisms with equal square bases and 45-degree twist; planes through a vertex form a Haar-null set.
