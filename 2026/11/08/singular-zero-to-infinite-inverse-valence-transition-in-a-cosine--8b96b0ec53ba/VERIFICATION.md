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

# Verification scope

Run `python verify.py` after installing Python 3, NumPy (via SciPy), SciPy, and SymPy. It checks the exact symbolic identity connecting the full Jacobian determinant with the one-dimensional inverse equation, including the target-dependent affine flux substitution. For three nonzero couplings (two positive and one negative), three positive flux parameter pairs, two choices of the remaining parameters and target, and 31 successive large flux cells, it constructs 558 inverse solutions by bracketing and verifies the complete original map, positivity of both inputs, noncriticality, and the stated first correction to their asymptotic lattice positions.

Expected completion banner: `VERIFY_OK symbolic_Jacobian_identity=1 asymptotic_regular_positive_preimages= 558`.

The all-target, all-parameter, infinite-branch and count-asymptotic conclusions are proved in RESULT.md. Finite tests are corroboration, not certification of infinite quantifiers. The original literature establishes the source map but does not independently verify these new claims. Independent review has not been performed.
