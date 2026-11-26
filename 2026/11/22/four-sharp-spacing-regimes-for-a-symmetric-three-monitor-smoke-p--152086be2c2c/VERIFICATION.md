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

For k covering monitors the conditional alarm probability is 1−q^k, with q=1−p. Integrating the layers uses weights p,pq,pq². For d<r the union and triple intersection have half-widths r+d and r−d, and the doubly-or-more covered region is the middle footprint. For r<d<2r the union still has half-width r+d and two disjoint pair overlaps each have Gaussian mass Φσ(r)−Φσ(d−r); beyond 2r only the three single layers remain. Touching endpoints have zero measure, giving continuity at both contacts. Independently recovering the moving-endpoint flux gives, up to the positive factor 2pφσ(r−d), the sign of exp(−2rd/σ²)−q² before r, exp(−2rd/σ²)−q between r and 2r, and a strictly negative sign past 2r. Thus the derivative changes sign at d=ell in the first smooth segment or d=ell/2 in the second; the downward jumps select r when r≤ell≤2r and 2r when ell≥4r. This proves a global unique maximizer including transition equalities (isolated zero slopes do not create a flat set of maximizers), and excludes d=0 since its right slope is strictly positive. At r=σ the recomputed change points are 0.6321205588, 0.8646647168, and 0.9816843611. The analytic argument covers the full unbounded spacing domain and is not a numerical grid search.

## originality

PASS

Weighted overlap coverage for fallible sensors, Gaussian spacing optimization and monitor contact geometry all have inspected precedents. The supported distinct contribution is the exact four-regime spacing of three identical hard-footprint monitors in this particular symmetric Gaussian at-least-one-alarm problem, with both contact plateaus and uniqueness. No inspected statement supplies those two plateau intervals or implies the complete optimizer. This is not a priority certification.

## value

PASS

The constrained transect presents a concrete coverage-versus-redundancy tradeoff: higher reliability changes the value of losing triple and double coverage differently. The exact rule identifies a nonzero interval over which the unique spacing does not move despite reliability changes, followed by another moving regime and eventual just-adjacent spacing. The two thresholds for entering and leaving the intermediate plateau and the final threshold are usable as a benchmark for this stylized layout. The value is the sharp structural contact classification, not a claim of better real deployments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
