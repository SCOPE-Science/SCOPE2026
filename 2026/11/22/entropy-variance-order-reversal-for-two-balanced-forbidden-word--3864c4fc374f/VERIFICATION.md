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

# Verification and reproducibility

The self-contained `check.py` uses exact Python integer and rational arithmetic with no external packages. Execute `python3 check.py` beside this document; its final output is `ALL CHECKS PASSED` after the following independently implemented checks.

- For every \(2\le k\le7\), 44 exact dyadic bisection steps isolate the unique near-one positive roots of the two distinct pole equations. Rational interval evaluation of the closed variance formulas verifies a strictly positive lower bound on their difference. Root signs and derivative positivity are checked in exact arithmetic, not inferred from decimal approximations.
- For every \(8\le k\le100\), exact arithmetic checks the elementary gate \(160k^2 4^{-k}<k+1\) and the small-parameter bound \(4k4^{-k}<1/100\). The proof establishes the monotonic extension of the gate and the variance remainder inequalities for all \(k\ge8\); finite checking does not replace those arguments.
- Direct enumeration of all binary words through length 13 for each of three pattern sizes \(k=2,3,4\) and both forbidden-word families reproduces every coefficient of the independently derived bivariate rational generating function, including coefficients by number of 1s.

The uniform-\(n\) limit defining the variance uses primitivity of the prefix automaton and the analytic Perron pressure. The small-case signs use exact rational certificates; the unbounded family and the asymptotics use the written inequalities. No claim of independent external audit is made.
