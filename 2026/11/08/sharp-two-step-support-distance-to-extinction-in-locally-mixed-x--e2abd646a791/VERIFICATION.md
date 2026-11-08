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

# Reproducible checks

Run `python3 verify.py` with Python 3.10 or newer; it uses only the standard library. It enumerates all states for cyclic rings of lengths \(2\) through \(15\) and validates the constructive support path, the non-isolated intermediate state, and the second step to zero. A separate direct support enumeration handles all states for lengths \(2\) through \(9\), independently of the constructive function. It also verifies the one-step count formula and exact rational two-step probabilities at mixing probability \(1/3\) for lengths \(2\) through \(7\).

The expected successful output is:

`VERIFY_OK constructed_support_paths=65532 one_step_distance_counts=14 independently_exhausted_states=1020 exact_probability_cases=252 n_range=2..15`

These calculations are finite sanity checks. The proof for every ring length and every interior mixing probability is in RESULT.md. The asymptotic counting statement follows analytically from the characteristic polynomial. Independent audit has not been performed.
