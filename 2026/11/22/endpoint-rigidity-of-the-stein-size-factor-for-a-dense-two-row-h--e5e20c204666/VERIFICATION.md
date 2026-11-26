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

Detailed balance and telescoping give the sharp factor at j=m+1 as F_m G_{m+1}/((m+1)²p_{m+1}); the lower tail and its complement attain the eventwise bound. At m=0 it is (1-p_0)/(4w)≥1/4. Summing the quadratic-geometric tail and using n=m+1 gives the factor bound 5/n in each regime (1-w)n≤1 or ≥1, which suffices for n≥25. For 2≤n≤24, bounding the three geometric-moment terms by their stated rational envelopes gives B_n with denominator 1140n(n+1). The numerator of 1/5−B_n is 23 at n=2 and is at least 135n²−236n−221>0 for 3≤n≤24. Thus every later site is ≤1/5 uniformly on the frozen interval, the maximizer is unique in its index, and the limit follows exactly. The events themselves need not have unique signs.

## originality

PASS

Pass for the explicit nonasymptotic parameter window and quantitative uniform separation of the noninitial sites. A distinct same-day general HNB result directly covers the qualitative eventual equality and the limit under the exact parameter substitution, and itself describes the two-row result as an earlier special case. Date paths do not establish priority. Its near-one compactness/finite-site argument does not give the certified window [9/10,1) or the uniform cap of 1/5. Those are proved here via a quantitative all-index estimate, not asserted as a new generic first-site principle.

## value

PASS

The HNB open problem motivates a natural Stein error constant. This result makes the eventual assertion usable at a stated finite parameter, including w=0.9, and certifies a gap of at least 1/20 against every competing site. Exact evaluation and robust localization across an entire explicit interval are more informative than computing the first site's value or observing its numerical dominance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
