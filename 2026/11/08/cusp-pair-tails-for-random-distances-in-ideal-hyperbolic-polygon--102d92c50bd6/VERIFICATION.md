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

The proof uses exact cusp-strip area Jacobians, the curvature-\(-1\) upper-half-plane distance identity, exponential-depth convolution, and an explicit integrable error-band estimate. It is an analytic argument, not a numerical extrapolation. The coefficient is positive for every valid polygon and invariant under changes of horoball cutoff because those cutoff heights cancel exactly.

Run `python -m pip install -r requirements.txt` followed by `python verify_ideal_polygon_distance_tail.py`. The program checks the cusp chart distance normalization for triangle, quadrilateral and pentagon examples; tests the exact triangle and quadrilateral coefficient formulas; and performs fixed-seed area-uniform simulations for an ideal triangle and two distinct ideal quadrilaterals, with \(1{,}500{,}000\) pairs per shape. It ends with `IDEAL_HYPERBOLIC_POLYGON_CUSP_PAIR_TAIL_CHECKS_OK` if all internal finite checks pass.

The simulations report finite-threshold values of \(e^R\Pr(D>R)-C(P)R\), which are expected to remain bounded rather than vanish. The proof's asymptotic remainder, and especially historical novelty, are not certified by a finite simulation. No independent audit or independent validation has been performed.
