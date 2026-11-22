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

# Reproducibility

Use `python checker.py` from the folder containing the embedded source. It uses only exact `fractions.Fraction` arithmetic and the Python standard library. It enumerates all \(3^3=27\) site assignments and verifies the complete encounter-generated replacement matrices, two different pairwise collision probabilities, coefficient formulas and strict sign inequalities. It also recomputes birth–death fixation probabilities directly from transition ratios at representative selection intensities; the continuum sign follows from the analytical coefficient inequalities, not the sampled intensities.

Proof assumptions: identically and independently sampled common site law, fixed anonymous group-composition payoffs, positive fitnesses, and pre-averaged fitness-proportional BDB updating. No finite enumeration is used to claim an infinite-parameter exhaustive search. A separate independent scientific audit has not been performed.
