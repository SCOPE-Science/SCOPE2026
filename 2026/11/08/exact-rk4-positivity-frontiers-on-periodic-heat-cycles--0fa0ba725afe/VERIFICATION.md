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

# Verification and scope

The complete analytic proof is in `RESULT.md`. Exact rational checks and an independent classical RK4 four-stage evaluation are in `verify.py` (standard Python library, using `fractions.Fraction`). Invoke `python3 verify.py`; the recorded output in `verification_output.txt` ends with `VERIFICATION_OK 13403 exact-rational assertions`.

The checker tests kernel symmetry and unit row sums for all 28 cycle sizes 3 through 30 at twelve timestep values, and verifies analytic kernel reductions at exact rational values. It also checks exact algebraic polynomials, root brackets and explicit sharp outside-window witnesses. The original analytic argument handles every real step and every integer cycle length, not merely enumerated ones; the checker is reproducibility support, not an infinite certificate.

The claim assumes exact classical RK4, constant-coefficient uniform one-dimensional periodic nearest-neighbor heat discretization, and one-step *endpoint* positivity for all nonnegative states. It does not establish stage positivity, extensions to variable-coefficient diffusion, other boundaries or arbitrary Markov generators. A separate independent mathematical review and publication-priority review have not been performed.
