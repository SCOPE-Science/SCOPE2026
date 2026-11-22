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

# Reproduction

Run `python verify.py` under Python 3.10 or later, with only the standard library. The program exhaustively sums probabilities over all paired-bit words in its stated finite ranges using exact `fractions.Fraction` arithmetic. Its output is `PASS 181 exact rational formula assertions`.

The finite checks verify the one-site run probability, the two-copy same-site probability, the exact finite covariance, and the shifted cross-copy probability. The limit uses the explicit collision probabilities together with the marked Poisson-process theorem of Arratia, Goldstein and Gordon (1990, Section 3, Theorem 2); no computational extrapolation is used for convergence. No formal proof assistant or independent mathematical audit has been run.
