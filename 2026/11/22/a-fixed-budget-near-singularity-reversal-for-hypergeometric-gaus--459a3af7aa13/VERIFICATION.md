---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The tangent and algebraic maps are precisely the inverse normalized cumulative integrals of the p=2 and p=3 kernels. Hence their transformed constants are A_d/d and H_d, respectively, and the quadrature integrates the constant numerator a exactly. Each fixed interior node of either matched map lands at x=O_m(d), and its numerator correction is O_m(d²). For p=2 dominated convergence with bound (f−a)/x² gives C_f>0, since f≥a and the positive quadratic jet is nonzero. The sampled correction is O_m(d). For p=3 the quadratic contribution integrates to c[asinh(1/d)−1/√(1+d²)], while the cubic remainder is bounded by integration of x³/(d²+x²)^(3/2)≤1. The sampled correction is only O_m(1). For sinh, scale each sample by d^(p−1); its weight is U_d sech^(p−1)(U_d s), which is O_s(log(1/d)d^((p−1)s)) and vanishes at every fixed positive s. The corresponding scaled integrals tend to πa/2 and a. This gives the signs, the constants in both absolute ratios, and both relative rates. Uniformity in m cannot hold for the sinh relative error tending to one: at each fixed d the transformed integrand is continuous and the positive Gauss rules converge by polynomial approximation. The frozen diagnostic was inspected, not executed. Independent bounded check: at 90 decimal digits integrate the original integrand with mpmath on [0,d,√d,1], evaluate changed rules using derivatives of the maps, and use nodes 1/2 or (1±1/√3)/2 with equal weights. In all 16 combinations of m=1,2, f=1+x² or 1+x²+x⁴, d=10^(−6),10^(−24), p=2,3, the trends agree. For m=2,d=10^(−24), the p=2 residuals are 1.00000000,1.33333333, the p=3 residuals/log(1/d) are 0.979135649,0.988183450, and the sinh estimate/integral is about 2.60801e−4 for p=2 and 5.99855e−9 for p=3. This finite check is not used to prove the limits. The geometric phrasing should be read as the exact displayed kernel (e.g. a transverse distance d to the endpoint), not a source at −d on the integration line.

## originality

PASS

Best of knowledge for the sharp fixed-order signed residuals and relative-error separation for nonconstant numerators at both exponents. The three changes of variables, Gaussian exactness on constants, and fixed-distance ellipse comparison are prior; the theorem does not contradict increasing-order convergence.

## value

PASS

A fixed sampling budget is a genuine constraint in near-singular quadrature. Demonstrating that one rule loses essentially all singular mass while two established matched choices recover it, with exact rates valid for nonconstant numerators, gives a useful warning about choosing transforms from ellipse size alone. The distinction between an integrated residual constant and a local logarithmic coefficient adds information beyond constant-numerator exactness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
