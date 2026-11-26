---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In equilibrium the length-biased interval and its uniform age give (2D/m) E integral_0^(L-h)_+ a da. If a reset intervenes the product has zero conditional expectation by independence. Dominated right differentiation gives C'_+(0)=-2D and C''_+(h)=(2D/m)Pr(L>h), including atoms. Integrating over the stationary square window yields the stated triangular kernel and both branches of Phi_T. Its second derivative at positive l is l(2T-l) for l<T and T^2 for l>=T, proving strict Jensen; evaluation at m and at the exponential law verifies the two variances and limiting ratio. Integration by parts is valid because C,C' decay and C' is absolutely continuous with integrable derivative; this gives the stated spectral expression. It is strictly positive for every real nonzero frequency under L>0, since sin z/z<1 for z!=0; the proof's aside about possible zeros is not an existence claim of the Finding. One may also obtain the absolutely continuous spectral measure directly by mixing, over L, the nonnegative transforms of the triangular kernels (L-|h|)_+^2, whose masses integrate to C(0). Monotone convergence yields the extended third-moment limit, and direct integration of the power-law tail against (z-h) and then the triangular averaging weight gives the stated constants, including the logarithmic critical case.

## originality

FAIL

A distinct prior catalog record gives the same equilibrium covariance, atom-sensitive recovery and third-moment spectral threshold. Unknown diffusivity follows by evaluation at lag zero. The distinct-window wording and explicit constants are not found as stated in the examined prior work, but the all-window optimizer is a routine consequence of the exact prior kernel: Jensen gives C_L(h)>=C_m(h) at every h; for nonconstant L the inequality is strict at h=0 by strict second-moment Jensen and hence on a nontrivial interval by continuity. The positive triangular window weight gives strictness for every T. The additional extended limits and power-law constants are direct integrals of the same kernel, not a substantially new claim in this package.

## value

FAIL

Exact covariance recovery and the third-moment boundary would be useful for this model, but those facts are already present in an equivalent setting. The remaining assertion is an informative interpretation of that kernel, not an independent advance here: pointwise convexity already gives the simultaneous clock ordering, and triangular integration gives the displayed finite-window and asymptotic constants. No new result on estimation, another observable, or a less restrictive reset model is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
