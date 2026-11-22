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

Execute `python3 checker.py` using Python 3. No external Python libraries, databases, or network connection are required.

The checker performs 2,917 exact finite tests of Pell/companion recurrences, the Dold congruences for several valid integer polynomial weights, the integer coefficients through degree 36 of seven power-series families, the corresponding first coefficients of OEIS A208034, and the logarithmic derivative of the explicit rational-power product. It also checks the first obstruction for odd and improperly scaled weights. The result is the printed `PASS` line.

These are finite consistency tests, not an exhaustive test of every polynomial, every prime, or all coefficient orders. The infinite claim relies on the explicit proof in RESULT.md; the degree conclusion relies on algebraic valuations rather than numerical root experiments.

No independent audit has been performed.
