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

- Standard-library `verify_singer.py` reconstructs the extension field with a primitive polynomial for each checked order, checks that the nonzero powers exhaust all residues, builds the \(q+1\)-element trace-zero difference set and verifies its planar-difference property.
- It enumerates the full point and line orbits and edge orbits for every divisor \(d\mid(q^2+q+1)\), for cyclic subgroup quotients and order-three semilinear extensions with representatives \(a=0,1,2\). Fixed-graph vertices, edges, connected components, and six-cycle degrees are separately checked.
- Ten prime powers \(q=2,3,4,5,7,8,9,11,13,16\) pass; the exact stdout is `checks.txt`.
- The all-prime-power quantifier follows from the proof, not these examples. A quotient is computed with parallel edges counted separately; fixed-point computations use the actual geometric realization and the preservation of point/line shores.
- Literature priority is based on inspected full-text or identified source materials, not on a formal global novelty certificate.
