---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Solving the positive equilibrium conditions and differentiating at it gives trace -(A+B xi), determinant K xi and nonzero off-diagonals. With AB/K=1-eta^2 in (0,1), the discriminant has the two reported positive zeros; the trace/determinant give stability everywhere, and the off-diagonals make the endpoints defective. In the real-root regions set g=B gamma/K and u=B^2 xi/K. The slower root satisfies g^2-(AB/K+u)g+u=0 and cannot equal 1 because substitution gives eta^2>0. It lies below 1 on the lower-speed branch and above 1 on the upper-speed branch, by continuity from zero and from the upper endpoint respectively. Implicit differentiation gives the sign of 1-g for its slope; in the focus region the rate is half the negative trace and increases. Rationalizing the slow root gives its fast-speed limit K/B. Near a focus, a real change of coordinates gives inward radial velocity proportional to radius and a nonzero limiting angular velocity, which forces infinitely many crossings of the line y=y_*. For the no-cycle clause, omitted from the frozen local proof, the field multiplied by 1/y has divergence -tau z-xi(1+omega y)/y<0 on the interior. No nonconstant periodic orbit can lie on or touch the boundary: y=0 is invariant with scalar linear z dynamics and the other boundary edges point strictly inward for y>0. The stated optimum is only a spectral exponent; the Jordan factor matters for norm estimates.

## originality

PASS

The exact model, endemic equilibrium and stability, examples of spirals, and the general single-community no-cycle theorem precede this record. The supported distinct contribution is the complete common-speed sweep and its exact spectral optimum and speed-up at fixed breaking/creation ratio, not existence of spirals or the definition of the model.

## value

PASS

Scaling both response rates at fixed ratio isolates a natural tuning variable without moving the endemic equilibrium. The finite optimum is not what the slow/fast limits or an isolated spiral example show: the rate eventually decreases, and the exact optimum improves on the fast limit by a parameter-dependent factor that can approach two. This quantifies when a finite response speed is preferable for the stated local objective and separates damped crossings from recurrent outbreaks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
