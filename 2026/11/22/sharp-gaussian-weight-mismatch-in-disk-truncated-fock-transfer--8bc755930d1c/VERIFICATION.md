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

# Reproducibility and limits

`verify.py` is a standalone standard-library Python 3 program. Run `python3 verify.py` from the directory containing the extracted file. It evaluates positive Poisson upper-tail sums, compares them to incomplete-gamma finite expansions, verifies numerically resolvable strict tail-ratio inequalities, tests adjacent-mode ties at analytical thresholds, checks the exact degree-zero norm, and compares computed largest coefficients with the predicted sharp large-radius equivalent. At packaging, the program passed 674 finite assertions. The program requires no external data, symbolic algebra package, or network.

The mathematical proof of the all-radius statements is in `RESULT.md`, not in the checker. Numerical truncation cannot establish infinite-dimensional completeness, strict inequalities for all indices or the asymptotic limit. The exact special-function identity is justified by Gaussian monomial orthogonality; the sharp constant is justified by uniform Poisson-tail/Stirling estimates plus a global Chernoff exclusion of all competing degree scales. Historical priority cannot be certified computationally, and independent review has not occurred.
