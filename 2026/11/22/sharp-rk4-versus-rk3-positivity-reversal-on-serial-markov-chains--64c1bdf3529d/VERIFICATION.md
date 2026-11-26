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

With a terminal padded zero and strictly positive birth rates, paths of k forward jumps contribute the product of k rates times the divided difference of the end-step polynomial on the k+1 consecutive diagonal arguments (holding transitions give the extra powers). RK3: only the diagonal root rho and the two-jump factors 3-h times the triple sum in the form 3-h(a+b+c) can obstruct; its first derivative is a positive quadratic. RK4: its diagonals and second divided differences are positive; the one-jump multiplier is the average of R3(-hu) over the adjacent-rate interval (point value if equal), strictly decreasing in h; the three-jump sign is 4-h(a+b+c+d). These give nonreentrant closed horizons, with missing distances omitted. Normalize H3=1: each rate is at most rho and every three-rate sum is at most 3, so every four-rate sum is at most 3+rho and the pair roots are at least 1. At the displayed witness both a triple and a largest-rate constraint saturate and the four-rate sum is 3+rho; appending positive rates no larger than (3-rho)/2 also works at any larger n. For the strict upper bound, when H3=rho/M a pair containing M and a positive neighbor has a strictly smaller cubic root than the mean over [0,M], which vanishes at h=delta/M. When H3=3/T, every triple extends to a four-window so the ratio is at most 4/3. The family with one unit rate followed by epsilon rates tends to the endpoint ratio, since the isolated pair root tends to delta<4 and other pairs diverge. At n=4 the four-window sum equals T, so 4/S cannot limit before H3; at n<=3 no such obstruction exists. python3 /workspace/branches/independent_checks.py 2 verifies the two symbolic obstruction entries and checks signs near the five-state horizon. The exact cubic definitions govern the constants; the printed last digits of delta are slightly rounded (independently 2.78529356340528162...). Neither the original finite checks nor this replay substitutes for the inequalities.

## originality

PASS

Best-knowledge pass for the optimized heterogeneous RK4/RK3 comparison, the sharp witnesses and the minimum-state theorem, not for the RK4 local coefficient formula. Heterogeneous long directed cycles already give essentially that RK4 ingredient; homogeneous pure-birth thresholds and a same-day two-method result address different quantifiers or orders.

## value

PASS

This gives sharp limits on how much safe completed step length can change with method order on natural serial transport generators, including a concrete minimal-size loss and the obstruction that causes it. The joint optimization, not a reissue of local polynomial tests, is actionable when positivity rather than stability alone limits steps. No comparison of accuracy, cost, or internal-stage positivity follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
