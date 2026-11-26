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

For each c, log-curvature equality gives Z_T/Z_S = exp(AR+B); multiplication by exp(cR²) and continuation of the Gaussian-damped bilateral Laplace transforms give a shift by k=A/(2c). Fourier uniqueness of the finite measures yields the pointwise gauge by continuity. If the two shifts coincide, c1≠c2 forces zero shift. Otherwise taking logarithms produces a global affine first difference with quadratic coefficient α=(c1 k1−c2 k2)/(k1−k2). Subtracting the quadratic-affine solution gives a bounded periodic logarithm. Growth rules out α>0, and α=0 forces b=0 by growth of S and then k1=k2=0 by growth of T. With α=−a<0, the compatibility equation gives the stated shifts, and periodicity and the common envelope slope give sufficiency. The alias-to-spectrum ratio has nonzero exponential slope times a bounded, bounded-away-from-zero factor, so it cannot be constant. The Fourier window squared gives c=2π/σ²; the unit-window intensity formula transforms with area Jacobian one and frequency second-derivative factor σ², giving 1/(2c). CHECK.py was inspected, not executed: its finite quadrature corroborates selected examples only; neither direction of the result needs numerical integration.

## originality

PASS

The one-width shift/tilt orbit is established in the distinct same-day record, and the affine ambiguity of the smoothed PSD is explicitly established in the cited paper. Neither inspected statement solves the simultaneous fixed-width gauge constraints. The classification of their intersection, including the exact periodic exception with only upper growth, is the supported distinct claim, to the best of the checked evidence.

## value

PASS

It settles a natural identifiability question left by the known single-window ambiguity. It gives exact conditions for when a second instrument width resolves all non-scale ambiguity, and constructively characterizes the smooth non-Gaussian failure modes as well as Gaussians. It makes no finite-data or stability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
