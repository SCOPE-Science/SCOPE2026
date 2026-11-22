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

# Reproducible verification

Run `python check.py` with Python 3.10+ and no third-party packages. The program independently constructs all allowed absent/forward/reverse orientations of complete underlying graphs through five vertices and computes each event by inspecting directed paths of length one or two. It uses exact `fractions.Fraction` probabilities at five rational densities and compares with every available type formula; the same checker verifies endpoint-orientation coefficients and two polynomial positivity identities at one hundred rational density points.

Observed result in the extracted package: `PASS 488 independent exact rational comparisons and algebraic identities`.

This finite enumeration does not establish all-order claims; those rely on factorization of independent external edge blocks and the finite symbolic endpoint polynomials proved in `RESULT.md`. The published global unrestricted-path sign theorem was checked as literature evidence, not computationally reproved. No independent external audit has been performed.
