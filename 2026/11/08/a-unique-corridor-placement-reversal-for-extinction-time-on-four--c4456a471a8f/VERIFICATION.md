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

Use Python 3 and SymPy; execute `python checker.py` from the extracted package. The script constructs the transient generator of the occupied/empty patch process for both graph completions, computes the exact symmetry-orbit solutions, and checks all 15 backward equations symbolically. It verifies the complete rational expressions and their difference, the coefficient-sign certificate for a unique positive threshold, an exact rational root interval, two asymptotic limits, and both adjacency characteristic polynomials. Separately computed full 15-state exact-rational solutions at six positive rates reproduce the closed expressions.

These calculations establish the stated algebraic identities for a finite Markov chain. The uniqueness and global sign of the threshold follow analytically from Descartes' rule of signs, continuity, and positive denominator coefficients. The checker does not address empirical realism, unstated graph families, or historical priority. No independent external audit or validation is claimed.
