---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The exact polynomial vector field and oval R=x^2+(y+w(x^2-h)x/(2h))^2 give dR/dt=-wR(R-h)/h by differentiation. Along R=h, x=sqrt(h)cos(theta), the original physical-time xdot=y yields dot(theta)=-(1+(w/4)sin2theta), everywhere negative when 0<w<4. Thus minimal physical period T=integral dtheta/(1+alpha sin2theta)=2pi/sqrt(1-alpha^2) with alpha=w/4, and transverse multiplier exp(-wT). The normalized physical-time angle density is delta/[2pi(1+alpha sin2theta)]; two gate-centered tangent substitutions yield conditional standard Cauchy laws. Pushing the angle distribution through x=sqrt(h)cos(theta) gives the displayed non-arcsine coordinate density. Fourier/Poisson kernel of the gate law yields E(X^2)=h/2 and E[(X^2-h/2)^2]=h^2 delta/[4(1+delta)]; Cauchy gate scaling yields the two-atom weak limit and sharp (4-w)^1/2 moment concentration. The boundary w=4 is nonperiodic. Independently re-integrated period and squared-position moment for four alpha values, with finite verification only as corroboration.

## originality

PASS

PASS to best knowledge. Belattar et al (2023) prove existence, invariant oval, hyperbolicity and phase portrait for the exact polynomial oscillator; those are explicitly NOT claimed new. Its inspected main theorem/proof does not state the original-physical-time phase distribution, full Euclidean position density, exact period and transverse multiplier, or the sharp w→4 coordinate concentration. The classical Adler phase drift integral/Cauchy substitution is generic prior knowledge, but applying the original unmodified polynomial dynamics to identify a complete measurable coordinate distribution and limit is a distinct natural system-specific quantitative result. No inspected stronger published theorem implies the full package, with risk of unindexed equivalent integration.

## value

PASS

For a concrete experimentally interpretable algebraic limit cycle undergoing arrest at w=4, exact physical-time occupation, period, transverse stability and concentration of the measured x coordinate are natural dynamical invariants not determined by knowing just the geometric oval. The boundary two-atom trapping law with rate quantitatively distinguishes time occupancy from uniform angle or arclength and resolves a motivated gap in the source phase portrait. It is a nontrivial complete metric-temporal classification of this family, albeit reducible by elementary integration once the physical angular drift is found.

The dated certificate retains the supplied scientific assessment, sources and limitations.
