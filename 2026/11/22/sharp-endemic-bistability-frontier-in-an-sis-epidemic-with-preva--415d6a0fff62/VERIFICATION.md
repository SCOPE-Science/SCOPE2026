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

# Verification evidence and limits

The equations are reconstructed from the exact SIS–logit model, with payoff matrices explicitly specified in `RESULT.md`. Every positive equilibrium is determined by the scalar identity \(g(I)=k\). The proof establishes strict unimodality, all positive-root counts, the principal Lambert-W formula, and local stability by Jacobian trace and determinant. The disease-free equality case is not assigned an unproved stability type.

Execute `python3 verify.py` from the directory containing the extracted files; it needs only Python 3 standard-library modules. The completed check examined 175 parameter triples strictly inside the bistability wedge, verifying maximum identities, bisection root locations, Jacobian signs, and exact field residuals. It also reproduced the rational-witness prevalences near 0.026390022712 and 0.193911638779. These are independent numerical checks of formulas, **not** proofs of infinite-domain assertions: the analytic proof is in `RESULT.md`.

The exact witness needs no floating-point certification: \(g(0)<4/5<g(1/10)\) follows from \(2<e<4\), and \(g(1)=0\). The unimodality argument then proves exactly two endemic roots. Source overlap and priority limitations are recorded in `REVIEW.md` and `AUDIT.json`. Independent scientific audit has not been performed.
