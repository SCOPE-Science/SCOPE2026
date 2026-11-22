---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The Fourier transform of 1_{[-a,a]x[-b,b]} is the exact product 4 sin(a xi_1)sin(b xi_2)/(xi_1 xi_2). On the circle the quadrant integral reduces to 64/R^4 times a singular but integrable trigonometric product. A fixed interior arc contributes O(R^-4). Near each axis, integrating sin^2(bR theta)/theta^2 gives the O(R^-3) term; subtracting the frozen sin^2(aR) term leaves a boundary layer theta=x/sqrt(R). Uniform-in-phase dominated convergence of the coefficient functions, together with nonstationary oscillatory averaging of sin^2(b sqrt(R)x), yields the Fresnel correction of order R^-7/2. Explicit integrals of (1-cos ax^2)/x^2 and sin(ax^2)/x^2 each equal sqrt(pi*a/2), giving the recorded 8sqrt(2pi) coefficients and little-o remainder for every fixed a,b>0 and arbitrary real R. Rescaled bounded subsequences force both axial sine phases to zero; rational exact matching or continued-fraction approximants for b/a give the upper liminf, so the sharp constant is 8sqrt(2pi)(sqrt a+sqrt b). Independent direct Simpson quadrature at radii 376.991 for a=b=1 and 530.929 for a=1,b=sqrt2 gave rescaled error about -0.184 and -0.125, respectively; this is bounded numerical corroboration, not proof.

## originality

PASS

PASS best of knowledge for the all-aspect-ratio two-term oscillatory expansion and liminf. Earlier polygon and convex-domain Fourier mean-decay papers establish base product formulas, R^-3 generic rates and certain square resonant upper bounds; the inspected specific statements do not identify this R^-7/2 exact constant uniformly over all real radii. Priority from older diffraction or polyhedral Fourier-asymptotics remains a risk.

## value

PASS

Classical rectangle/square Fourier decay identifies exceptional near-resonant angular averages, but rate bounds do not give the unavoidable positive second-order floor. A complete all-real-radius two-term expansion and exact lower envelope for every fixed aspect ratio quantify the sharp resonance obstruction rather than merely improving a generic O(R^-3) bound. Rational and irrational aspect ratios share a surprising exact constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
