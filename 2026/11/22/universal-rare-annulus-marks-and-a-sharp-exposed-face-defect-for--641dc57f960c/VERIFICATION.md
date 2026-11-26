---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In a nonvertical slicing plane, projection sends each azimuthal meridian fiber to an interval along the corresponding radial ray. Its upper and lower plane-support levels increase with cos(azimuth) since R>a; away from the null transition set, annularity is exactly feasibility with nonempty interior at every azimuth, i.e. m<H−R sin θ. Haar cos θ and folded Lebesgue offset give the Jacobian b³xW_R/R², and the common hit conditioning cancels in the conditional density. The supports stay in a fixed bounded x-range. The vertical exposed face gives H′(0+)=q by taking limits of supporting maximizers, so uniformly G_R=1+qx/R+o(R⁻¹), W_R=1+O(R⁻²), and J_R=1/6+q/(3R)+o(R⁻¹); the sliver near x=1 has width and height O(R⁻¹). For q>0 the old triangle is contained in the enlarged support and the normalized density is strictly smaller throughout it, so TV equals the new mass outside, with leading term 6q∫₀¹x²dx/R=2q/R. For q=0 the support symmetric difference and density error are both o(R⁻¹); a C² support gives O(R⁻²). The hit mass is πR/4+O(1) and the annulus mass b³J_R/R². For the unit circle, independent expansion of the fixed-support normalizer gives 1/6+1/(40R²), and integrating the absolute centered second-order density at the sign change x=√(3/10) gives 27/400−9√30/2500. Inspected RESULT.md lines 41–126, VERIFICATION.md and check_marks.py. The 109 recorded checks, including numerical rectangle and ellipse cases, were not rerun; they do not certify arbitrary meridians. The bounds are for each fixed meridian.

## originality

PASS

Credit the earlier exact offset criterion, invariant measure and unmarked probabilities, and treat the finite marked density as their direct change-of-variables consequence. The distinct claim assessed here is the sharp conditional marked-TV law with nonsmooth exposed-face coefficient and the explicit circular second-order constant. These are not stated or supplied as probability bounds by the strongest reviewed sources.

## value

PASS

Conditioning on a rare topology gives a natural geometric observable with a universal mark law. The TV coefficient is a quantitative diagnostic of a face of the meridian even when no smooth boundary expansion is available. The zero-face and circular regimes both show why scalar rarity alone is an inadequate description of the convergence of conditional marks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
