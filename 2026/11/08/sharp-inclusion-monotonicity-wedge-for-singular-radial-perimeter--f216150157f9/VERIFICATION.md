---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The proof in `RESULT.md` is an analytic proof for all indicated positive side lengths and all real exponents, with the sharp singular transition for \(-1<p<0\). It does not rely on finite numerical tests. The differential identities, the sign of the normalized first variation, the convexity of the aspect-bounded shape region, and the two endpoint limits are the critical steps. The sign reversal outside the wedge is established by continuity of a strictly negative partial derivative and therefore gives genuine strictly nested counterexamples.

The standalone verifier `verification/check_rectangles.py` uses only the Python 3 standard library. Run `python verification/check_rectangles.py`. It prints `RECTANGLE_WEIGHTED_PERIMETER_OK 902` followed by six approximate aspect thresholds. It uses adaptive Simpson quadrature and centered differences to compare independent numerical expressions, checks monotonicity on sampled nested paths, confirms the predicted sign reversal when a short side grows outside the allowed region, and checks positive homogeneity. The quadrature is numerical: its passing output cannot prove root uniqueness, global inequality, exact phase endpoints or originality. Those statements are addressed by the explicit analytic argument.

Scientific limitations: only commonly oriented, origin-centered rectangles are classified. The result does not give a multidimensional box theorem or a general radial-weight monotonicity criterion. Historical priority remains provisional and no independent audit has been performed.
