---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The centered Euler second moment multiplies by E[(1-h+(sigma/sqrt(lambda))*sqrt(h)*Z)^2]=f_d(h), so independent increments give the stated product. Expanding in z=h1*h2 at fixed sum T gives f_d(T)+z^2-2z0*z with z0=(2-d^2+dT)/2. The interval of attainable products is exactly [0,T^2/4]; clipping z0 is the unique minimizer in z. The zero and equal-step thresholds follow from z0=0 and (T-d)^2<=4-d^2 respectively; for d>sqrt(2), T_- - T_c=2/d-sqrt(4-d^2)>0 by squaring. The boundary equalities yield one unordered split, including the collapsed endpoints, which are only approached in the open mesh. For large T, the smaller step is 2z*/(T+sqrt(T^2-4z*))=d/2+O(1/T), so the optimal product is (1-d^2/4)T^2+O(T), while the equal product is T^4/16+O(T^3). Taylor expansion gives the stated bias; at d=sqrt(2) the quadratic term vanishes and the cubic term is positive. For independent bounded corroboration, `python /workspace/independent_checks.py 3` checked the reduction and optimum inequality on 32,300 rational grid points; the continuous classification is algebraic.

## originality

PASS

Bounded prior comparison supports the exact finite-horizon covariance phase diagram for standard two-step Euler–Maruyama. Neither a uniform-mesh result for strong solution error, free-final-time covariance steering, nor a fixed-budget observation-mesh theorem covers this objective and these thresholds.

## value

PASS

Although the key minimization is elementary, the full phase diagram fixes a meaningful failure mode of numerical covariance as an objective: with low noise, the closed optimum starts collapsed, moves to unequal interior steps, becomes uniform, then leaves the uniform grid. The open-mesh nonattainment and unbounded long-time penalty for equal steps are exact test cases for mesh optimization, not claims about the best mesh for solution accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
