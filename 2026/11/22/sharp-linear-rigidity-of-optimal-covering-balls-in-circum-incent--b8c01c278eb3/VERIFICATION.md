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

# Verification evidence and limits

The theorem is proved analytically in `RESULT.md`. Its critical geometric inputs are the insphere-contact property of a nondegenerate simplex, the positive support radius in every tangent facet direction, the boundary contact points and feasible diameter balls in Nour [1], and the two exact radius-deficit inequalities. The proof explicitly treats all feasible centers, including the origin, and a fixed near-optimal radius threshold.

Run `python3 check_geometry.py` using Python's standard library. This checks the nonregular tetrahedron from the motivating paper, its facet normals, strict inradius, the value of the optimal radius, and homothetic sharpness witnesses. It also tests a random sample of 20,000 support inequalities. Numerical checks are finite and do not certify the uniform spherical support gap, the global containment theorem, or research priority; these are addressed in the written argument and literature comparison, respectively.

No independent mathematical audit or formal certification has been performed.
