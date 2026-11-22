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

The proof uses an exact affine induction-state recurrence, three direct exchange identities, and five transposition identities for a four-variable polynomial. These compare all possible permutations by strictly improving swaps and require no assumptions about numerical approximation.

The reproducible checker is `verify.py` in the same package. It uses Python 3 standard-library `fractions.Fraction`, samples reproducible distinct rational activation increments and rational shade-retention and initial-induction values, enumerates every permutation of each sampled three- and four-lightfleck instance, and evaluates the exact recurrence. The recorded execution output was `PASS: 124005 exact rational assertions`.

Finite tests do not establish the global assertions for real parameters; the exact algebraic proof supplies those. Numerical parameter-to-duration conversion is only illustrative. No direct plant experiment or physiological calibration is asserted. Independent validation has not been performed.
