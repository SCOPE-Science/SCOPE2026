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

Haar measure makes the absolute cosine Z uniform on [0,1]; Cauchy's projection formula gives the stated integral, with base term pi*z/2. Integration of the absolute cosine gives pi*z when z>=k/sqrt(1+k^2), and on the other branch substitution z=k*sin(alpha)/sqrt(1+k^2 sin^2(alpha)) gives G. The sign of G_alpha is the sign of H(alpha)^2-k^2, and H falls to its unique minimum before rising again. At the minimum of H, G is increasing up to a branch endpoint of area less than pi; the smaller stationary root for k above that threshold is a local maximum of increasing height since G_k>0, and its height tends to infinity (already G(k,0)=k). Hence exactly one tie with the polar maximum, at the stated alpha_c. Other directions are separated by a uniform gap near the tie. The chain rule gives kappa=-G_alphaalpha/z_alpha^2>0, and the smooth envelope gives m'=G_k and m''=G_kk-G_kalpha^2/G_alphaalpha. A signed analytic square-root coordinate about the nondegenerate oblique maximum gives superlevel interval length C(k)sqrt(t)+O(t^(3/2)), since the odd Jacobian term cancels. The polar length is exactly [pi+epsilon-M(k)]_+/pi near the maximum. These give the fixed-aspect claims. At k=k_c+lambda*epsilon the heights differ by d*lambda*epsilon+O(epsilon^2); when the oblique leading deficit is zero (lambda=-1/d), the next-order coefficient must be retained. On k=k_c-epsilon/d+mu*epsilon^2 the oblique deficit is (d*mu+beta)epsilon^2+O(epsilon^3). For d*mu+beta=0 its width is at most O(epsilon^(3/2)); for a negative coefficient there is no oblique interval for small epsilon. Thus on the inner scale each component is at most order epsilon and both have positive order-epsilon weight only on the positive branch, as the formulas specify. On that branch the centered rescaled endpoints converge and constant density gives conditional total variation, and the polar rescaling is exactly uniform near the tip. The independent 50-digit recomputation (record4_recompute.py) gives k_c=2.641402552064102, d=0.7767760421294519, kappa=3.667631057865201, q=0.2291445948054032 and beta=0.1898838274257648; at mu=0 direct oblique lengths divided by epsilon are 0.6436062938 and 0.6435741224 at epsilon=10^-4 and 10^-5, tending toward the predicted 0.6435705481. The proof is replayable from RESULT.md lines 74–137, not inferred from those examples. The frozen verifier and notes were inspected without running the uploaded script.

## originality

PASS

The brightness formula and deterministic maximizing-direction switch are antecedents, not independently original parts. The supported contribution is the local probability at the tie and the joint parameter/deficit analysis: the outer epsilon window, the inner epsilon-squared window with its second-order shift, and the conditional viewing-direction laws. The indexed deterministic theorem and the independently available Vickers–Brown abstract do not state such limits. The latter's cone section and appendix remain an explicit access risk.

## value

PASS

At a known deterministic switch the two maximizing types give different mass orders: square root for the interior maximum and linear for the polar endpoint. The result quantifies the first window in which the interior mass vanishes and the finer offset where both mechanisms can supply comparable mass. The conditional laws say which types of viewing directions survive and on what spatial scale. This joint asymptotic and the shifted boundary are useful information beyond the known maximizing latitudes or a fixed-aspect density evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
