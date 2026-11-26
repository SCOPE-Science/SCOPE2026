---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For C=(I+BGB)^(-1) and centered observations the shift penalty is xi^T GBCBG xi/2, so zero is sufficient and unique for G positive definite (not necessarily unique on the boundary). Writing Z=BGB, the quadratic coefficient of y in the integrated likelihood is B^(-1)Z(I+Z)^(-1)B^(-1), bounded between 0 and B^(-2); the residual covariance is at least sigma^2 I. The linear trace term therefore dominates the log determinant bounded above by d log(1+||B||^2 tr G), proving coercivity. The log-partition Hessian is a conditional variance strictly positive in every nonzero symmetric direction because the tilted Gaussian has full support and B is invertible. This also holds along boundary segments. Joint sign symmetry in a common eigenbasis then gives strictly improving diagonal pinching whenever G is nondiagonal. In a scalar mode differentiate the reduced objective: 2(1+z)^2 j'(z)=L z^2+(2L-1)z-2 rho. For rho<=0, L>1, and its derivative sign enforces the unique endpoint minimizer; for rho>0 the unique positive root is the given formula. At 1/L the numerator is 2(1-rho), giving the EEA ordering, including equality and opposite-mode signs. Continuity of the closed problem and the sequence G_*+epsilon I give exactly the stated attainability criterion; an ignored mode contributes its true mutual information, log(1+a_i^2/sigma^2)/2. Independent replay python3 /workspace/review_replay.py (section 4) evaluates the direct posterior KL for 108 two-mode PSD grid cases, including boundary and nondiagonal competitors. This is bounded corroboration, not global evidence; the reported separate random experiment was not rerun.

## originality

PASS

The explicit spectral optimizer with the all-mode attainment frontier and precision comparison is distinct on current evidence. The OAE objective, convexity in precision at fixed shift, Gaussian objective, optimal shift and existence of a scalar nonattainment example receive prior credit.

## value

PASS

Commuting symmetric forward models are a natural benchmark for a generally coupled surrogate calibration problem. Optimizing over the entire precision cone, not only diagonal competitors, makes the boundary phenomenon interpretable: the unregularized algorithm can fail to attain its optimum because it should discard precisely the data in nonpositive modes. The sign law predicts where residual-based EEA over- or underweights information, and mixed eigenmode differences show why a uniform precision inflation or deflation cannot always implement the correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
