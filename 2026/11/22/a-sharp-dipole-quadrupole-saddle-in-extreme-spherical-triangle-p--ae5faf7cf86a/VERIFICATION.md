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

# Verification details and limits

Run `python verify.py` from the same directory as the result. The checker uses only the Python standard library. It integrates the two-dimensional circular-ensemble gap simplex by midpoint quadrature, independently checks the normalization against the gamma expression, recovers the cosine moment and second and third symmetric moments, and checks the Haar-rotation-weighted dipole and quadrupole factors with a fixed-seed experiment.

A successful execution prints `VERIFY_OK`. The angular integrals are finite numerical diagnostics and do not replace the exact circular integration-by-parts argument. The proof separately establishes the nonuniform limit by bounded likelihood weighting of a geometrically localized uniform boundary layer. The integral norm comparisons, spherical rotation moment formulas, and trace inequalities are mathematical arguments independent of sampling runs.

No computer run establishes historical novelty or independent mathematical certification. The full article by Le (1989) and the unpublished Jones–Benyon-Tinker (1994) manuscript were not accessible; their potential bearing on priority is acknowledged.
