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

# Verification record

The exact Gaussian moment derivation is provided in `RESULT.md`. The standalone `check_correlated_cv.py` reconstructs the estimator coordinate polynomial, evaluates Gaussian expectations by recursive Isserlis pairings over all matching labels, and compares the result to the stated formulas using rational arithmetic, not Monte Carlo floating-point approximation.

Reproduction command:

```sh
python check_correlated_cv.py
```

Observed outcome on the complete checker: `PASS: 105 exact-rational dimension/rank/correlation cases, both mean and squared norm.` The tested cases are every dimension \(1\le d\le6\), every rank \(1\le k\le d\), and probe correlations \(0,1/3,1/2,4/5,1\). The proof, rather than the finite checker, establishes the theorem for all dimensions and correlations.

External independent mathematical validation has not been performed. The conclusions apply only to the fully specified coupled-reference quadratic model; the published independent-probe method is not tested or contradicted.
