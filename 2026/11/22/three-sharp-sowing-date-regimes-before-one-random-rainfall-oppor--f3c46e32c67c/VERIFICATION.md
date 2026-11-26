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

Shifting a delayed first date to zero multiplies its positive success probability by exp(t₁), so every optimizer starts at zero. For u=exp(−t₂), v=exp(−t₃), direct integration over the three intervals of the uniform variable exp(−R) gives the same objective F as inclusion–exclusion. The compactified domain is continuous at its zero corner; that corner is strictly worse than (1,1), and moving off v=0 at u>0 increases F. On v=u<1 the only possible diagonal maximizer has negative F_v and is improved by decreasing v. The u=1 edge has unique optimizer v=min(1,p₁/p). Interior stationarity forces u=Z(y) and p₁<y<3/4 for y=pv/u. The singular value y=8/9 cannot satisfy F_v=0. On the admissible interval the remaining stationarity function is strictly increasing by the stated positive quadratics, and its endpoint signs yield the unique admissible root only for p>p₂. For those p the boundary candidate has F_u<0 (so an inward move decreasing u increases F); at p=p₂ the limiting root is the existing boundary point, not a tie. This exhausts all closure boundaries and interior stationary points and gives the three unique ordered calendars. Independent integration and polynomial root isolation reproduce both constants and, at p=1, dates 0, 0.156819423113, 0.706895851121 and success 0.7895887539535.

## originality

PASS

Rain-dependent sowing and diversified timing are established ideas. The supported distinct finding is the full three-release optimum under one exponential trigger, with three independently decaying establishment opportunities conditional on that trigger and a union-of-successes objective. In that model the two exact thresholds control changes in the active equality constraints. The strongest indexed exponential calendars and the biological timing literature inspected use different feasible timing choices or objectives, and do not give these thresholds or the unique quartic regime.

## value

PASS

The tradeoff between early availability and lifetime decay is inherent in timing several opportunities before one uncertain trigger. Three cohorts are the smallest instance in which simultaneous, partly staggered, and fully staggered schedules can all be distinct. Exact thresholds show when to expect each pattern and include both boundary cases; this gives a structural baseline for timing diversification without inferring distinct rain sources or adaptive decisions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
