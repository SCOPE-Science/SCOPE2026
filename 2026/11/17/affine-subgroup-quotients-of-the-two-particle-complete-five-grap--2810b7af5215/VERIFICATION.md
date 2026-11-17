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

Execute `python3 verify.py` with Python 3 and no third-party libraries. The program generates all unordered pairs of disjoint graph cell supports, face flags, affine group actions and subgroups, and quotient flag orbits. It checks the 14 subgroups in six conjugacy classes, uses Burnside's fixed-flag count for a second orbit-count calculation, checks every edge's triangle incidence, every vertex link, the number of boundary circles, orientation-sign propagation, Euler characteristics, and the final six homeomorphism types. Output is recorded in `verification_output.txt` and ends in `VERIFY_OK`.

The computations are exact and exhaustive for the finite five-label group and 55/180/120 original barycentric flags. The proof that these data classify compact surfaces uses the surface classification theorem, not numerical extrapolation. The noncompact continuous orbit spaces are only claimed to be homotopy equivalent to the compact models; the explicit equivariant deformation is mathematically supplied in `RESULT.md`. Literature search cannot eliminate unindexed equivalents. No independent audit has been performed.
