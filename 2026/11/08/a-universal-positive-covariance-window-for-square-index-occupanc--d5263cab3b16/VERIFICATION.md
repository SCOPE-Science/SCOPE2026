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

# Verification

The standalone `verify.py` is executable with Python 3 and only its standard library. Its exact finite-allocation branch independently enumerates all words of length \(0\le N\le8\) on \(m\in\{2,3,4\}\) possible boxes and computes each distinct mixed covariance using exact fractions; it compares those values to the closed mixed-moment formula. It tests the cancellation identities \(F(a)=0\), \(G(a)=1\), and zero discriminant for \(j=1,\dots,100\), again using exact rational arithmetic. Finally, high-precision decimal evaluations illustrate convergence in the critical window for \(j=1,2\).

Command: `python3 verify.py`

Observed output: `PASS: 720 exhaustive exact covariance assertions; 300 exact critical-polynomial assertions; 14 asymptotic diagnostic assertions; total 1034.`

Limits: The numerical checks sample finitely many parameters. They are neither an exhaustive classification of all sizes nor an independent proof of the asymptotic estimate. The result's infinite-size conclusion follows from the displayed exact moment relation and uniform second-order logarithmic expansion. The signs precisely at the two zero crossings of the limiting parabola are not determined.
