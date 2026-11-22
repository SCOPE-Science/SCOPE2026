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

# Reproduction and boundaries

Run `python verification.py` with Python 3, SymPy and SciPy. The deterministic rational checks construct \(C=T^{\mathsf T}T+I\) from integer matrices and test both claimed inverse formulas by exact left and right multiplication. They cover dimensions one through five, 75 trial matrices at each dimension, and both symmetric and independent updates. Each case checks the two products and nonzero determinant, yielding 2,250 exact matrix assertions. The script also evaluates five scalar product-normal small-ball tests and three square-normal small-ball tests, for a total of 2,258 assertions.

The scalar tests compare finite small-ball probabilities with the leading asymptotics. Neither tests nor numerical samples prove an infinite-dimensional statement or the high-threshold asymptotic for all positive-definite range blocks. The analytic proof in RESULT.md establishes those assertions. The code checks the full inverse identities; it does not independently establish the bibliographic originality of the finding. Neither the proof nor checker asserts a finite-threshold ordering of condition numbers.
