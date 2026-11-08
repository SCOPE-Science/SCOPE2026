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

Run `python check.py` after installing the single dependency in `requirements.txt`. The program was executed successfully from the scientific package and checked: the stationary generator recurrence and exact quartic factorization symbolically, the strictly positive variance identity, eight independent exact-rational generator matrix systems, the quartic coefficient signs, and the explicit rational crossover example.

The proof of existence and uniqueness is the stationary convolution, triangular generator recurrence and strict coefficient-sign argument documented in `RESULT.md`; the finite numerical and rational instances do not by themselves establish the universal parameter claim. No independent audit, external certification or all-literature novelty guarantee is asserted.
