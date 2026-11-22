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

# Mathematical verification

The standalone `check.py` rebuilds the two finite-state Markov-chain absorption probability systems independently of the closed forms at unit switching, recovery and transmission rates, for each degree from 2 through 5, plus three distinct non-symmetric positive-rate vectors at degree three. It checks both no-infection and all-infected probabilities as exact rational numbers and uses numerical quadrature only for corroborating large-degree constants at degrees 20, 100, 500 and 2000. The analytic proof establishes the all-degree statements. Run `python check.py` with Python 3, SymPy, NumPy and SciPy. The script must finish with `PASS`. These are same-model computations, not independent certification.
