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

## Reproducibility

Run `python3 verify.py` from the extracted directory. The script requires Python 3, SymPy, NumPy and SciPy. It performs exact symbolic integrations for the trapezoid's base means, the mixed central second moment, and the taper-variable polynomial identities. For 96 rational-parameter three-dimensional convex polytopes it independently triangulates the boundary, cones facets to an interior point, integrates linear and quadratic functions on exact rational tetrahedra, and compares the exact covariance to the separate closed expression. The observed output was `ALL_CHECKS_PASSED 96 independent exact tetrahedral prismatoid moment comparisons`.

The exact all-parameter argument is contained in RESULT.md; the finite triangulations and symbolic computation are corroborative checks, not independent scientific audit or exhaustive proof. Historical priority is provisional. The geometric realization is the original standard-coordinate orientation and the interior measure is normalized Lebesgue volume.
