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

# Algebraic reproducibility

The standalone `artifacts/verify.py` reconstructs the coordinate maps symbolically with a unit-diagonal three-coordinate positive-definite equicorrelation matrix and an all-ones initial vector. It independently enumerates all 27 ordered updates, verifies the four objective formulas and their multiplicities, factors all differences against a permutation epoch, tests the mean identity, compares nine exact rational parameter choices and proves the two-coordinate base case symbolically. Execution requires Python 3 and SymPy. Its recorded standard output is included at `artifacts/verification.txt`.

# What this does and does not check

Exact symbolic equality of polynomials is checked across all 27 index sequences; the analytic proof separately derives the sign comparisons on the full open positive-definiteness interval. A finite grid would not by itself prove the continuous parameter claims. The verifier does not establish that the result is absent from every previously published document or independently validate the result.
