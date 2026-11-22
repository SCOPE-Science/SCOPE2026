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

# Reproduction and scope

Run `python verify.py` with the standard Python library. It uses exact rational arithmetic, not floating-point tolerances, to classify the ten acyclic block partitions of the diamond, all 118 nonzero projected Boolean-cut ratios and the nine displayed rational expressions in the positive weight parameter. The cross-multiplied coefficient identities are exact. The derivation in `RESULT.md` proves that these finite cut cases control the full real-input variation operator norm by a layer-cake decomposition and that piecewise-linear segment integration controls the nonlinear isotonic projection.

The checker also reconstructs exact Euclidean isotonic projections by testing all feasible faces and minimizing squared residuals, confirming the explicit strict-face sharpness witnesses for parameters on either side of one and 2200 deterministic rational sample pairs. Those finite sample comparisons are supplementary and are not offered as a proof of the continuum or of unrestricted inputs.

The certificate assumes precisely four vertices, the diamond order, equal observation masses and weights \((r,1,1,r)\) in the stated edge order. It makes no claim about arbitrary weighted masses or larger partial orders. Historical priority remains subject to further literature review; independent audit has not been performed.
