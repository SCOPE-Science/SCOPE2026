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
# Verification details

Run `python3 verify_rounding.py` with Python 3.9 or later; no third-party packages are required. The program uses exact `fractions.Fraction` values and checks 13,234 rational assertions, including the one-shot-versus-iterated transition law, explicit geometric survival-tail sums, and 144 constructive three-point witnesses. It verifies the special irrational example with integer-square bounds around \(\sqrt2\), not floating-point comparisons.

The exact rational cases exercise the algebra and boundary conventions, but no finite enumeration is a proof that every integer or every real contraction satisfies the theorem. The full classification follows from the two short support/conditional-mean and counterexample arguments in `RESULT.md`. Scientific limits: scalar unit-grid rounding, ideal independent conditional randomness, and absence of forcing or saturation. Independent audit has not been performed.
