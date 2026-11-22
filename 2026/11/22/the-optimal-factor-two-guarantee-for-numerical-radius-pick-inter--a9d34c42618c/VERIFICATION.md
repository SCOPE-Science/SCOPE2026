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

# Verification
The proof in `RESULT.md` first establishes the universal guarantee \(P\le\Gamma\le2P\) from the source's necessary circle-test theorem, classical matrix-valued Nevanlinna--Pick sufficiency at operator-norm budget, and the standard numerical-radius/operator-norm inequalities. It then proves factor-two optimality through exact finite-matrix singular values and scalar Schwarz--Pick along two approaching nodes. The explicit sufficient false-positive wedge follows from strict inequality in the lower bound. No numerical experiment is used to infer an infinite-dimensional or continuous assertion.

Run `python3 check_exact.py` to reproduce the representative exact-rational inverse-gram and singular-value checks; the script is supplementary. Source Example 2.5 at fixed radius is prior work, not independently new. The true interpolation cost at a fixed positive separation is bounded but not claimed exactly determined. Independent audit has not been performed.
