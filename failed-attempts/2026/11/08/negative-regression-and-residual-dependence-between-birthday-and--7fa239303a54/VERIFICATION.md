---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For iid uniform draws on n labels, conditioning on birthday time B=t leaves exactly n-t+1 unseen coupons, so C|B=t=t+sum_{r=1}^{n-t+1}Geom(r/n), with exceptional B=n+1 giving deterministic C=n. Coupling consecutive t using the same geometric increments gives strictly decreasing first-order stochastic order and negative covariance for nondecreasing transforms. Expressing B as indicators of initial unit discovery waits and summing independent geometric covariances gives the displayed exact negative double sum. Birthday survival product yields Rayleigh scaling, dominated Riemann sums give Cov(B,C)/sqrt(n)→-sqrt(pi/8), coupon variance n²π²/6 and birthday variance n(4-pi)/2 give the Pearson constant. The independent Rayleigh/Gumbel joint weak limit follows by coupling C to an independent complete geometric sum, with difference o_P(n). Verified exact covariance n=2,3,4,8 from separate rational formula. These finite checks are not the all-n proof.

## originality

FAIL

Complete primary earlier publication dated October 12, 2026 already proves exact joint law via conditional PGF, identical strict negative regression, identical finite covariance double sum, and both identical asymptotic constants; it also proves stronger L² conditional regression. Another earlier November 2 result independently states the same stochastic ordering and limits. The remaining jointly independent Rayleigh/Gumbel normalization is a standard consequence of this conditional joint law and established marginal occupancy limit, not an independent original claim rescuing the submitted aggregate.

## value

FAIL

Conditional negative regression and sharp residual covariance are compelling natural invariants, but these exact statements are already published with more detail. The only marginally additional two-scale weak independence follows from the preexisting joint PGF and classical coupon collector Gumbel and birthday Rayleigh limits by a routine coupling; no distinct nontrivial unknown parameter/classification remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
