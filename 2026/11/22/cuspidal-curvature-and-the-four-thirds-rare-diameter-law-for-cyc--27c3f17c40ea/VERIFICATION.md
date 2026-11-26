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

Compactness and the unique unordered diametral pair reduce the event to two disjoint ordered endpoint neighborhoods. In either one, horizontal displacement loses a_L t³+a_R s³+O(t⁴+s⁴); squaring the transverse difference adds only O(t⁴+s⁴), and the chord length is bounded away from zero there. Thus the leading deficit is uniformly comparable to t³+s³, even on the axes. Under cubic scaling, the exact domains lie in a fixed bounded set and converge off the simplex boundary, while the normalized arclength density is dominated by a multiple of u^(−1/3)v^(−1/3). Integration gives the stated beta integral and constant, including the factor two from the two orders. The actual slack differs uniformly from 1−u−v by o(1); hence the stated joint Dirichlet limit, Beta law for the sum and independent Beta law for the left fraction follow. The order variable is uniform and independent of the canonically left/right-labeled marks by exchangeability (the two complementary order events are not themselves independent). The determinant has magnitude 12 a_i |b_i| and the denominator is (2|b_i|)^(5/2), giving the intrinsic coefficient. For the cycloid, the exact chord identity bounds the norm by 2r(d+sin d), with equality at the global maximum possible only for d=π; the length is 8r and a_i=r/6, b_i=r/2. Reviewer-authored `python3 /workspace/independent_reproduction.py cusp` (SciPy 1.18.1) used direct integration in probability-mass coordinates, obtaining the coefficient 0.05830090078339615 and tail ratios 1.0262350114, 1.0112603267 and 1.0050207385 at the three listed thresholds. The last conditional first mark was 0.2868319033 versus 2/7. These are diagnostics, not certified bounds or an infinite-claim proof.

## originality

PASS

The cycloid's cusp invariant is known, and the same-day phase-uniform trochoid result supplies enough local information for the ordinary cycloid specialization by reweighting. The 4/3 exponent and Dirichlet parameters are also shared by other geometric models. The distinct supported claim is a uniform intrinsic law for arbitrary compact endpoint-cusped plane arcs satisfying the precise local and global conditions, not priority of the cycloid diameter, the bare exponent, or the Dirichlet family.

## value

PASS

The general theorem identifies a sampling-sensitive exponent and an intrinsic, quantitative relation between arclength tail probability and the product of the two absolute cusp curvatures. Its conditional law resolves both the distance deficit and the division of contributions between endpoints. Separating the global uniqueness condition from the local geometry distinguishes this class from smooth or multiply diametral settings. This reach, rather than the cycloid specialization on its own, supports value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
