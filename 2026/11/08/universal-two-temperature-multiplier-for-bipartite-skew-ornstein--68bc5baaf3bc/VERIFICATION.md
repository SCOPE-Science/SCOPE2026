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

The finite-dimensional theorem is proved analytically in `RESULT.md` by the block-sign involution and the stationary covariance trace identity. `verify.py` uses only the Python 3 standard library and exact `fractions.Fraction` arithmetic, with a separate Lyapunov linear-system solve and rational matrix inversion. The deterministic seed gives reproducible model coefficients. Executing `python verify.py` passed 99 exact-rational cases: 96 nontrivial combinations of dimensions, noncommuting within-group symmetric positive definite relaxation, nonzero intergroup skew coupling, and contrasting temperatures, plus two disconnected equilibrium examples, and one counterexample outside the sign-adjoint class. For each nontrivial combination it checks the full EPR, covariance and irreversible-current identities, not merely a scalar asymptotic.

These checks do not establish the universal quantifiers over arbitrary finite dimension and real parameters, nor do they establish publication novelty; those respectively rely on the written matrix proof and the separately limited literature comparisons. No independent audit has been performed.
