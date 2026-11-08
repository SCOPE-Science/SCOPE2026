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
Run `python3 verify.py` in a directory containing the extracted research files. It checks the binomial-coefficient definitions and every required Eisenstein valuation for the finite set of indices 2, 4, 8, 16, 32, 64, 128, 256. The infinite quantifier follows from the proof using binary Frobenius congruences and Legendre’s factorial valuation identity; the finite verifier alone does not establish it. No independent audit has been performed.
