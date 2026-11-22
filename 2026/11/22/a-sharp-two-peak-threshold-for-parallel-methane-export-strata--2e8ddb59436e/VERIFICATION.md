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

# Reproducibility and scope

The proof is self-contained in `RESULT.md`. Run `python3 verify.py` from the extracted directory with Python 3 and the standard library only. It checks the exact bivariate rational derivative numerator by polynomial algebra, rational stationary threshold inequalities, sign changes enclosing all three witness stationary points, stationary material balances, and selected exact identities. The checks do not sample an infinite parameter space as a substitute for a proof. The sharp positive-domain classification comes from the discriminant and strict monotonicity analysis in `RESULT.md`.

The verification does not include site observations, parameter fitting, microbial kinetics, or environmental model validation. External independent audit has not been performed.
