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

# Reproducibility of the theorem

Run `python palindrome_cover_check.py` for explicit Euler-circuit constructions, verification of all required cyclic factors at alphabet sizes 2 through 8, and exhaustive binary testing of all cyclic strings with lengths 1 through 8. The expected minimum-length sequence is 8, 15, 28, 40, 60, 77, 104. Binary brute force finds the first cover at length 8, with 16 rooted strings.

Run `python palindrome_cover_ilp_check.py` with NumPy and SciPy to independently solve a necessary integer-flow relaxation for alphabet sizes 2, 3 and 4. Its optima are 8, 15 and 28; these lower bounds match the constructive covers. The optimization counts only necessary conditions, and is not used as an all-alphabet proof.

The unrestricted mathematical conclusion follows from the edge multiplicity, parity, and Euler expansion proof in RESULT.md. Both checkers were executed successfully against the source contained in this package. No claim of independent external audit, proof-assistant certification, exhaustive searches at larger alphabets, or optimality classification is made.
