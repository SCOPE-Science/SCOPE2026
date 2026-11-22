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

# Reproducibility and limits

Run `python3 verify.py` using the Python 3 standard library. The checker directly uses exact rational arithmetic for 6,561 contraction comparisons on rational gain grids, 21 affine boundary two-cycle cases and separately checks nonlinear forced trajectories and an admissible sharpness sequence. It explicitly computes nonzero symmetric two-cycles for four gains above the unit boundary. All checks succeeded during preparation.

These are finite stress tests, not exhaustive verification of every parameter, every perturbation history or the infinite-time conclusions. The proof in `RESULT.md` establishes the universal quantifiers using one-step signed inequalities, compact invariant domains and contraction pullback arguments. The source comparison and residual priority uncertainty appear in `REVIEW.md` and `AUDIT.json`. Independent mathematical validation has not been performed.
