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

With Python 3 and the bundled `verify.py`, execute `python3 verify.py`. The verifier uses only `fractions.Fraction`, reconstructs the combinatorial Laplacian, computes \(F(hL)\) by exact rational matrix inversion, and compares all off-diagonal entries with the analytic formulas. It checks 54 full rational matrices and 5,532 individual off-diagonal identities across nine parameter pairs and six positive rational steps. It also checks the quartic numerator identity, diagonal positivity and stochastic row sums. The script must print `VERIFY_OK` and counts.

The infinite-parameter statements follow from the algebraic projector decomposition and strict one-root sign argument in `RESULT.md`. Finite tests cannot prove a statement over all integers and timesteps. Published mathematical priority and independent verification remain open.
