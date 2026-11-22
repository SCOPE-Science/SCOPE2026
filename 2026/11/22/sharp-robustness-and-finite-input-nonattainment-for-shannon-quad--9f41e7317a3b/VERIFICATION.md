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

# Reproduction and limits

Run `python3 checker.py` with a standard Python 3 interpreter. The program checks the explicit Jacobian by exact fractions, brute-force sign vectors, and deterministic rational simplex samples for dimensions 2 through 8 and four positive parameter pairs. These are finite tests, not a proof of a universal theorem. The proof is given in `RESULT.md`, including boundary behavior, parameter normalization and an infinitesimal sharpness witness.

The symbol `L` throughout the package denotes the global input-maximum/output-sum Lipschitz coefficient, not the derivative's Euclidean operator norm. No independent mathematical audit or external validation is claimed.
