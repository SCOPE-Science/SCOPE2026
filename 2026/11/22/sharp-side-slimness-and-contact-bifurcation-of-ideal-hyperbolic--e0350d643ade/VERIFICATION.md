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

# Verification notes

The exact mathematical proof consists of a point-to-geodesic distance identity, a reciprocal one-variable minimax analysis, an isometric comparison of the four sides, and elementary monotonicity. See `RESULT.md` for hypotheses, full quantifiers, equality case and endpoint limits.

`verify.py` computes actual hyperbolic distances between points on semicircle geodesics using \(\operatorname{arcosh}(1+|z-w|^2/(2\operatorname{Im}z\operatorname{Im}w))\), with golden-section minimization along each geodesic. It checks thirteen cross-ratio parameters and their peak formulas, samples both side-type envelopes, and verifies the relabeling symmetry. Reproduce with:

```text
python3 verify.py
```

Observed result: `PASS: 5335 direct/analytic checks, 5 symmetry comparisons, phase endpoints`.

The numerical checks are finite and are not an infinite proof. The results are only for nondegenerate ideal geodesic quadrilaterals in hyperbolic curvature \(-1\). Historical-priority completeness and independent external mathematical validation remain unestablished.
