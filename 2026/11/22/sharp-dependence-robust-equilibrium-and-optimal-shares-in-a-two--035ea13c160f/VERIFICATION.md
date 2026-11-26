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

For D=U−V the unique scalar root z=Q(b(2z−1)) exists by continuity, monotonicity and opposite endpoint signs. The private payoff difference gives b=a; sorting the largest D first and differentiating a[z²+(1−z)²] gives b=2a for the planner. The sorted intrinsic-value derivative is the strictly decreasing upper quantile of D on the interior, with limiting derivatives ±1, so the planner's root gives the unique maximizing share. For a root above one half, t=b(2z−1) is in (0,1) and Q(t)<1−t, since {D>t} is contained in {U>t} with positive mass in the omitted open part. Reflection gives Q(−s)>s for the lower half. For a target in the upper half of the open interval, t<1−z. Choose z−<z<z+ so close that t lies strictly between both rotations' two support values −z± and 1−z±; these laws have tail masses z± at t. Adding independent wrapped noise gives positive smooth densities uniform in both margins, with limiting tails at t by a.s. convergence off a zero-probability wrap boundary and no atom at t. Mixture now attains the exact tail z. Reflection and independence fill the remaining shares. For the same law, doubling b keeps the root on the same side of one half (the sign at one half is unchanged) and moves it strictly inward, including if the doubled threshold is outside (−1,1). The identified sets are separate, not a Cartesian product claim.

## originality

PASS

The supported distinct statement is exact smooth-positive attainment of every interior endogenous share, strict endpoint exclusion, and the resulting dependence-robust identification for both private and social shares. Neither the congestion threshold characterization nor fixed-marginal tail bounds are new. The same-copula balancing is an elementary but useful comparative-static consequence, not the sole basis for originality.

## value

PASS

With only two known valuation marginals, point predictions for congestion allocation need not be identified. Exact open ranges answer how large the ambiguity is, show that requiring everywhere-positive smooth density does not reduce the attainable interior, and distinguish what is robustly true of planner balance for a fixed law from the separately attainable shares. This is a complete, motivated identification calculation, not simulation or a general welfare claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
