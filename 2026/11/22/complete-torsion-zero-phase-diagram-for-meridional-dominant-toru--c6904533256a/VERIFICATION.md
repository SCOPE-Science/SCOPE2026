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
# Verification and limits

Execute `python verify_torus_torsion.py` using Python 3, SymPy and NumPy. The actual run returned `TORUS_KNOT_TORSION_PHASE_CHECKS_OK 5 families, 30 parameter checks` and `DIRECT_CARTESIAN_DETERMINANT_OK 20`. The script checks exact symbolic determinant and endpoint identities, a direct Cartesian derivative calculation, and numerical root counts for multiple coprime winding pairs and radii. The full proof of all-parameter root counts is in `RESULT.md`; finite tests are not a substitute for its analytic convexity argument. The special zero-curvature condition was proved directly from the cross product and checked against Fuller's theorem. No independent audit was conducted.
