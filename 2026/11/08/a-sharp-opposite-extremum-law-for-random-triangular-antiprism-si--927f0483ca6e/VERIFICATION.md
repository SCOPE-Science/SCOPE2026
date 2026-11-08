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

The theorem's proof is analytic: exact projected-vertex triangle inequalities, a finite partition into eight conical solid angles, explicit dot products and determinants of the generators, correct arctangent branches, and an exact derivative-sign argument for all \(h>0\). These steps verify the continuous parameter theorem and its equality case. The generic-view null sets and positive-height boundary are identified explicitly.

The standalone `check_antiprism.py` was executed with Python 3 using only its standard library. For each of five different positive heights (including the regular-octahedron height), 18,000 seeded uniformly random viewing normals were used to independently project all six three-dimensional vertices, build a two-dimensional monotone-chain convex hull, and count whether it had six vertices. The observed proportions agreed with the exact formula within conservative stated binomial tolerances. The code also directly evaluates spherical cone solid angles from generating vectors, tests numerical derivative consistency, and checks the limiting and critical values. Completion marker: `TRIANGULAR_ANTIPRISM_SIX_SHADOW_CHECKS_PASSED`.

The numerical checks are finite and do not prove an all-height theorem or establish originality. General solid-angle formulas and the regular-octahedral constant are credited to earlier literature. No independent mathematical audit or external certification has been performed.
