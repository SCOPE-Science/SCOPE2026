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

Independent local derivation: maximizing radius on the first quadrant is equivalent to optimizing a^(2/p)+(1−a)^(2/p) for a=|x|^p. The maximizers are the axial tips below p=2 and diagonals above it. Triangle-inequality equality forces antipodality, so compactness localizes every near-diameter pair. For p≤1, the branch coordinate u=1−|x| has transverse size (pu)^(1/p)(1+O(u)); distance defect is asymptotic to u+v and the arclength Jacobian tends to 1 for p<1 and √2 for p=1. Four ordered tip pairs times four branch choices and triangle area 1/2 give 8/L_p² and 16/L_1². For 1<p<2 the arclength density in the signed transverse coordinate is 1+o(1); the leading deficit is (|y_1|^p+|y_2|^p)/p, as the transverse quadratic correction is lower order. A beta integral of the unit sublevel disk gives the stated gamma ratio and coefficient after summing the four pairs. At p=2 the exact angular half-width is 2 arccos(1−ε/2). For p>2 the diagonal radius has radial loss r_p(p−2)u²/2 to second order; summing both radial losses and the angular loss r_p(u−v)²/4 gives the asserted positive definite form. Its determinant is r_p²(p−1)(p−2)/4, and the arclength-product density is r_p² at the center, giving the last coefficient. The local relative errors tend uniformly to zero, confining the rescaled events to bounded sets; the respective ellipse, disk and triangle boundaries are null, so the rescaled densities converge after normalization in L¹, including the finite labels. The circle uses the exact angular band. The quarter-arc parameterization (cos(t)^(2/p),sin(t)^(2/p)) yields the perimeter; monotone coordinates ensure rectifiability and domination near p=1 yields continuity there. The one-sided coefficient limits are 8/L_1², precisely half the diamond coefficient.

## originality

PASS

The supported distinct contribution is the complete fixed-parameter arclength-endpoint classification, the comparison across its singular transitions, and the corresponding marked limits as a family. The circle and astroid cases overlap materially with inspected statements; neither supports standalone novelty. The diamond computation is elementary tip geometry, not credited as an independent novelty. No inspected comparison gives the full fixed-p boundary-sampled classification.

## value

PASS

This is a complete fixed-shape family law for natural boundary sampling, not a table of special cases. The sharp coefficients and explicit conditional shapes distinguish cusp, corner, singular curvature, circular degeneracy and isolated smooth maxima. The diamond's doubled coefficient and the change in the nature of localization at the circle are substantive features that simpler diameter comparisons miss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
