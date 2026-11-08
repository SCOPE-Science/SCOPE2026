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

# Verification of the stated coefficient signs

Run `python3 verify.py` with Python 3 (standard library only). This performs exact-rational arithmetic and ends with `ALL EXACT CHECKS PASSED`.

For each of BDF4 and BDF5, the checker constructs the polynomial from the BDF defining sum, derives and compares each Schur constant, verifies the zero-free radius \(R=7/5\) or \(R=4/3\), and establishes all coefficients through index \(999\), including the vanishing index two. It also checks the Cauchy-tail inequalities at \(1000\) and the exact monotonicity criterion that makes them valid for all subsequent indices. For BDF6 it verifies the strictly positive expression for the second normalized coefficient. A written proof of why the rational tests imply the infinite conclusion is in RESULT.md, especially its zero separation, convolution-tail and fractional-composition steps. Numerical sampling alone would not establish the infinite statement.

Scientific limits: the certificates concern uncorrected, uniform-grid scalar convolution weights, not a fully assembled solver. No independent mathematical audit has been performed. Primary literature comparisons establish only the inspected evidence, not exhaustive priority.
