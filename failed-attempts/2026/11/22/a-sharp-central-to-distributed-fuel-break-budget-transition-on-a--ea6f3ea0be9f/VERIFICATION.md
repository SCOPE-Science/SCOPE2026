---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Under uniform single ignition, each unordered connected pair contributes twice in the average, giving exactly the six path monomials with prefactor 1/2. The singleton monomials alone make the Hessian positive definite, while each remaining monomial has a positive semidefinite Hessian. Reflection gives equal outer effort, and the constrained derivative at zero outer effort is p[(1+p)exp(-B)-1]. Its sign and strict convexity prove uniqueness even at the threshold; the right endpoint has positive derivative, and B=0 is a singleton. Interior marginal equality gives q_2=q_1/(1+q_1) and hence the stated cubic and center-to-outer gap; the cubic gives the asymptotic fractions. On three sites the product is fixed and strict convexity equalizes the two efforts; on two sites there is no choice. Independently evaluated the rational risk witness (57/32 and 8177/4608). Reviewed VERIFICATION.md and check.py as evidence without execution; neither constitutes field validation.

## originality

FAIL

A distinct indexed path result gives the exact p=1 case and its strictly convex one-variable objective. The entire frozen generalization in p is obtained by a common effort translation and restriction to a subinterval of that very objective; see the explicit transfer below. This is a statement-level comparison, not a historical-priority inference from catalogue dates.

## value

FAIL

A support transition can be a useful exact design benchmark, but this record adds only a uniform coordinate translation and routine clipping of the already-known strictly convex optimizer. It adds no new active-set patterns, geometry, or scientifically justified treatment heterogeneity. The exact reparametrized cutoff alone is not a separate surviving valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
