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

Run `python verify.py` with an ordinary Python 3 interpreter. This reproduces 7,057 exact arithmetic assertions using only `fractions.Fraction`, the standard library, and direct pre-update state transitions: 162 directed edge updates, 180 high-confidence conditional-energy identities, 10 finite dyadic probability-law checks, 360 finite moment recurrences, 4,320 general star-confidence updates, and 2,025 biased-star moment recurrences.

The checks are finite and are not substituted for the theorem's real-parameter proof, its iid run argument, or its Bernoulli measure-dimension proof. The fixed graph is the pure neighborhood model of Krishnagopal–Porter Eq. (3) with one interaction per discrete step. The code neither measures publication originality nor establishes independent validation.
