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

The exact statement and proof are in `RESULT.md`. Run `python3 check_partition.py` from this directory with Python 3 (standard library only). It exhaustively evaluates the 75 stated parameter triples and their 209445 feasible integer occupancy profiles, checks exact rational optima and profiles, and independently implements Euclidean capped-simplex projection by bisection for selected small cases. It checks one strictly nonvertex deepest point in the arithmetic resonance case.

The count of 660714883218 vertex configurations is a sum of exact binomial multiplicities, not an iteration over that many vertices. A finite range does not establish the theorem for all parameters; the argument uses strict convexity and the equality case of the Euclidean variance identity. Source novelty comparisons were based on identified scientific contents and cannot certify priority across inaccessible literature.
