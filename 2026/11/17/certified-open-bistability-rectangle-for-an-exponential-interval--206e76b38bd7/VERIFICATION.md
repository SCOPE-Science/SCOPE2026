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

Execute `python3 verify_bistability.py` using the Python 3 standard library. The program uses exact integers on a rational grid of spacing \(10^{-30}\), outward integer floor/ceiling operations, a 23-term positive Taylor expansion for \(e^{t/16}\), and a rigorously bounded tail, rather than floating-point intervals.

For every parameter pair in the claimed rectangle and for every point of both certified base intervals, the fourth-return derivative is bounded in modulus by strictly less than \(0.51\) or \(0.72\), respectively. The respective fourth-return center errors are bounded by \(0.00095\) and \(0.00053\), below their mean-value contraction margins. The program additionally tests interval separation of second iterates and separation across all four phases of the first cycle from the second cycle's base interval.

The displayed diagnostic decimal figures are approximations of the grid-rational endpoints; all assertions are exact comparisons. This is a same-model reproducibility check, not an independent audit. The contraction argument itself is given in `RESULT.md`; neither a finite grid of parameter samples nor a floating-point orbit plot is used to establish the uniform theorem.
