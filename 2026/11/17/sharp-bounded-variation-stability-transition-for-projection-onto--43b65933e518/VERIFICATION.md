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

# Verification of the sharp path-total-variation-ball projection coefficient

The proof in `RESULT.md` covers arbitrary finite real path lengths and all shared positive constraint radii. Its key nonstandard algebraic step is the boundary-sign identity \(V_n(g)=\|g\|_2^2\), verified from the explicit formula for block-constant \(g\) in the proof. Block averaging contracts path total variation; the correction term then has gain at most one more. Direct classification of the only possible low-dimensional face types gives the smaller constant one.

Run `python check_tv_ball.py` to independently reproduce the exact rational checks. It exhaustively forms every signed nonempty active-edge face projector in dimensions \(2\) through \(8\), compares induced difference-coordinate column norms, and evaluates explicit finite pairs attaining coefficient two at lengths \(4\) through \(39\). The final success line is `ALL_PATH_TV_BALL_PROJECTION_CHECKS_PASS`. Exact finite checks do not certify untested dimensions, which rely on the analytical proof.

The primary scientific limits are unweighted one-dimensional nonperiodic paths, Euclidean fidelity, fixed positive shared variation radius, and one nearest-point projection. The literature inspection does not constitute exhaustive priority certification. Independent mathematical audit has not been performed.
