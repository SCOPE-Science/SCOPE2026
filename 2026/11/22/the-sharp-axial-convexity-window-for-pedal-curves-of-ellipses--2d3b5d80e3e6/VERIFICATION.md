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

# Reproducibility and limitations

Execute `python check.py` with Python 3, SymPy, and NumPy installed. It verifies the explicit polar curvature identity, exact factorization at the stationary minimizer, a symbolic thin-ellipse expansion, and numerical comparisons for 300 parameter combinations. The numerical grid is not exhaustive and is never used to prove nonexistence of extra convexity windows. The all-parameter sign proof rests on monotonicity of \(2ex/(1+ex^2)\) for \(0<e<1\) and the factorization displayed in RESULT.md.

The point must remain in the ellipse's interior; no claim is made about off-axis foot loci. Boundary examples with zero curvature are still strictly convex as point sets. Originality has residual risk from historically inaccessible conic-pedal material; no independent mathematical validation has been carried out.
