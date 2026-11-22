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

# Reproducible checks and limits

Run `python3 verify_projection.py` from the directory containing the file. Python standard library suffices for 32 design-moment and 20-minor checks; optional NumPy and SciPy add five convex-hull calculations on the 64 signed segment sums. The saved run printed `PASS including five independent convex-hull volume calculations`, with endpoint dimensionless values approximately 3.5555555555555554 and 2.3703703703703702 for \(\operatorname{Vol}(\Pi P)/\pi^3\).

Exact rational endpoint tests confirm the projection volume ratio \(3/2\) and affine quotient values \(27/2\) and \(8\); a 1001-angle grid checks that projection volume and the affine quotient decrease while the original polytope volume increases. A separate symbolic evaluation of the 20 minors at \(\phi=0,\pi/6,\pi/3\) gave respectively \(12,\ 4+4\sqrt3,\ 8\), matching the all-angle formula.

Finite sampling or convex-hull numerical agreement is not a certificate for the continuum or uniqueness. Those rely on the exact two-triple classification, fixed determinant-sign chamber, and strict monotonicity proved in RESULT.md. No independent external audit has been performed.
