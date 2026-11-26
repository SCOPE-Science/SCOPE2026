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

For ordinary area measure the half-plane Berezin probability has density 4(Im u)^2/(π|u−conj(v)|^4). Straightening the genuine sector by w^p and reflecting gives an analytic chart with nonzero positive derivative in the straightened coordinate, so hσ(v)=c^(−s)|v|^s(1+O(|v|)) near zero, s=σ/p. For fixed interior u the small-radius integral has exponent s+1: divergence at s≤−2 is at every evaluation point. On an interior angular compactum, |u−conj(v)| is bounded below by a fixed multiple of |u|+|v|. Consequently the rescaled middle integrand is dominated by a constant times |v|^s/(1+|v|)^4, and the part away from the mapped corner is of order r^(2p). At s=2, on 2|u|<|v|<ε the relative errors O(|v|)+O(|u|/|v|) have bounded integrals against d|v|/|v|; the angular measure π and the radial logarithm p log(1/r) give 4p sin²(pφ), with the two complementary regions bounded after division by r^(2p). For s>2 the integrable majorant hσ(v)|v|^(−4) gives the asserted saturated coefficient, with no need for hσ to have bounded support in the half-plane. Under a change ψ(v)=λv/(1+bv) the Jacobian ratio |ψ′(v)|²/|ψ(v)|⁴=λ^(−2)|v|^(−4) cancels the change in c². Reflection gives angular symmetry; off any neighborhood of the relevant side point ±1 the weighted kernel mass tends to zero, using the same two integrability exponents. At the bisector the Cayley map gives uniform disk area, q↦−q negates the logarithm X, and its disk orthogonality variance is 2∑_{n odd}1/[n²(n+1)]=π²/4−2log 2. Strict Jensen and a Taylor expansion justified by exponential moments in |s|<2 give both bisector claims.

## originality

PASS

Credit standard conformal kernel transport and familiar polygonal Bergman and Toeplitz theory. The distinct claim supported by the inspected statements is the complete sharp localized corner-power response, including the coefficients and angular contrast, not the conformal formulas themselves or boundedness criteria.

## value

PASS

Corner distance is a canonical singular test symbol for coherent-state localization. Exact thresholds separate divergence at every interior point, a universal angular response, a universal logarithmic correction, and a saturated response whose coefficient depends on the cutoff/global chart. This is quantitative information not supplied by qualitative boundedness, including for acute corners and some powers that are not ordinary area-integrable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
