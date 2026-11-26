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

The derivative of H_theta lies between theta^2/(theta+1) and theta, so h is strictly increasing and bounded above and below by positive linear multiples of y. Integrating out either exponential conditional gives the stated marginal and normalizer, Z_k ~ log(k)/k. For powers 1 and 2, h_i(y)^p exp(-a_i y)/y is an integrable majorant for the marginal numerator multiplied by k; thus E[X_i] ~ A_i/log(k) and Var(X_i) ~ B_i/log(k). The conditional mean also gives E[Y_1 Y_2]=E[Y_1/(a_2+kY_1)]<=1/k, bounding the mixed X moment by O(1/k). The covariance is therefore asymptotic to -A_1 A_2/(log(k))^2, proving the prefactor. For finite k>0 the conditional X_2 mean strictly decreases with Y_1 while X_1 increases, proving strict negativity; continuity at finite k and the two zero endpoints yield an attained negative minimum in the interior. On intervals inside (0,1), the logarithmic coordinate T_1 has limiting uniform mass by integration of 1/(ky); letting interval endpoints approach 0 and 1 gives tightness and the uniform limit. The conditional exponential representation gives T_2=max(0,1-T_1)+o_P(1) because the log-sum differs from the max by O(1/log(k)) and log(E)/log(k) tends to zero. Hence the log coordinates tend jointly to (U,1-U). Continuous limiting uniform marginal quantiles give copula convergence; the common Lipschitz bound makes it uniform. Decreasing both coordinates reflects the copula twice but fixes W, and both limiting rank statistics follow from bounded rank-score or independent-copy formulas with no ties in the limit. Independent quadrature using numeric inverse hazards and a logarithmic integration coordinate tested two fixed parameter sets through k=10^16. It also returned approximately -0.2561772788 at a parameter point where the source paper's Table 1 prints +0.9552; the analytic sign proves that the positive table value cannot describe the density of its Eq. (32). Replay: python3 /workspace/reproductions/frozen_checks.py 2.

## originality

PASS

The bivariate family, its hazard transformation, the exponential-conditional parent density and finite-coupling dependence are not new. The supported distinct claim is the simultaneous countermonotone copula limit and explicit sharp Lindley-scale Pearson asymptotic as the coupling alone diverges. The checked model and generation papers provide the density/conditional representation, not the joint logarithmic-rank degeneration or the inverse-hazard dependent coefficient. The conclusion is bounded by the inability to inspect the full 1988 article.

## value

PASS

This is a natural regime of a published lifetime model where two common dependence diagnostics give opposite practical impressions: the copula approaches the most negatively dependent possible rank law while Pearson correlation vanishes. The explicit nonzero logarithmic coefficient gives the scale of this mismatch for each fixed set of parameters, rather than merely showing numerical smallness or a qualitative contrast.

The dated certificate retains the supplied scientific assessment, sources and limitations.
