---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The infimum, optimizer, and strict comparison are correct, but the explicit claim that the optimizer is interior exactly when (1-alpha)|ab|<=s is false. The Gaussian residual vector (X2-aX1,X3-bX1) is independent of X1, with covariance d=c-ab and variances 1-a²,1-b². Positive semidefiniteness is |d|<=s. Expanding the conditional product and using the tilted normal second and fourth moments 1-alpha and (1-alpha)(3-alpha) gives B+4ab(1-alpha)d+2d². The optimizer is the projection of -(1-alpha)ab onto [-s,s]. Strict interior requires (1-alpha)|ab|<s. For example, alpha=1/2 and a=b=sqrt(2/3) give s=(1-alpha)|ab|=1/3 and c*=1/3, the lower endpoint. At s=0 the feasible set is already a singular singleton. Subtracting s² from the unconstrained minimum gives (1-alpha)[a²+b²-(1-alpha)a²b²], strictly positive off the origin; the correction for projection is nonnegative. The stated 51/64 example is correct.

## originality

FAIL

A different indexed result already gives both the exact unoptimized moment polynomial and the entire admissible interval for the very same Gaussian model, including singular cases. The claimed envelope and phase regimes, once the boundary wording is corrected, are mechanically implied by completing the square and clipping its center to that published interval. The indexed result's headline deficit extremum is different; the decisive overlap is in its exact formulas, not its headline or date.

## value

FAIL

A fixed-correlation envelope is a natural sharpness question, but here the entire corrected answer is a one-variable square completion on the already stated interval for the already stated exact objective. The example and the phase description add no independently useful unknown result. Changing the weak boundary inequality to a strict one would not leave a qualifying repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
