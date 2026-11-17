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

Run `python verify.py` with Python 3, SymPy and mpmath. The checker was executed against this exact standalone artifact and reported `PASS: cubic composition, Jacobian factorization, 3D positive samples, diagonal critical rate`.

The exact identity in proof step 2 follows by subtracting the logarithms of two coordinates; this avoids loss of sign or square-root assumptions. The upper bound \(e\) holds only after the first iteration, and all subsequent contraction estimates are explicitly indexed from \(n\ge1\). The lower total-population bound combines monotone growth below one with a minimum on \([1,3e]\). With bounded log ratios it yields a positive coordinate-wise floor, hence a uniform multiplier \(q<1\) without an unspecified persistence lemma.

The mean perturbation in proof step 3 is second order because the centered deviations sum to zero and the weighted first-order term equals a sum of squares; its error is bounded using the positive total-population floor. Compact uniform attraction of the scalar Ricker map, and finite-block approximation for vanishing forcing, furnish the infinite-time convergence. The scalar no-two-cycle theorem and local attraction at the flip are the standard one-dimensional inputs identified in the proof. The exact transverse limit follows from continuity of the logarithmic mean and Cesàro summation. The diagonal limit is a parabolic two-step asymptotic, not a generic three-dimensional center-manifold claim.

Symbolic and high-precision numerical diagnostics test selected cases only. They do not prove global quantifiers, rule out all previously published equivalents, or independently validate the result. No external independent audit was performed.
