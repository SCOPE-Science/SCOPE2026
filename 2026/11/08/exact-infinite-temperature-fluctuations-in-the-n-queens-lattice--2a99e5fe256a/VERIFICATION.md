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

# Verification of the finite-board fluctuation identity

Execute `python3 check.py` in the directory containing this file. Python 3 standard library only; the checker does not download inputs or require external software.

It tests the closed edge count, wedge count, and parity-sensitive mixed diagonal sum by direct site iteration at every integer board size from 2 through 80. It then computes the complete finite-population second moment with rational hypergeometric probabilities and compares it to the stated rational variance. Independently, for each of the four sizes 2, 3, 4 and 5, it constructs all attack edges and enumerates **all** subsets of precisely the specified cardinality, comparing directly obtained first and second moments. A final rational identity verifies the limiting cancellation. All 491 programmed exact checks passed.

The proof in `RESULT.md` proves the identities for all integer board sizes; the bounded computations are reproducibility tests only, not a substitute for its algebraic parity sum, falling-factorial covariance identity or limiting argument. The last result is an **iterated** limit with temperature first. No global result about arbitrary finite temperature, phase transitions, or independence of external review is claimed.
