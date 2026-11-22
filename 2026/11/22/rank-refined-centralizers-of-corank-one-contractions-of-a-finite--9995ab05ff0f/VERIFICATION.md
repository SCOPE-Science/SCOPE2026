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

# Verification of the centralizer-rank formulas

Run `python3 verify.py` under Python 3, without dependencies. It generates every full nondecreasing contraction for each finite chain size from 2 to 10 using binary increments and independently checks composition pointwise. For each size and each one-flat-step position, it enumerates the commutant and compares every image-rank coefficient with the stated binomial expression; the entire reflected family is checked separately. The checker also tests the summed centralizer cardinalities and every predicted strict coefficientwise difference, including the explicit positive factorization.

Successful output terminates in `ALL_CORANK_COMMUTANT_TESTS_PASSED`. The proof in `RESULT.md` covers arbitrary chain size and the weak limit by analytic arguments; these bounded enumerations neither imply an infinite classification nor verify the weak-convergence limit. No formal proof-assistant certification or independent audit is claimed.
