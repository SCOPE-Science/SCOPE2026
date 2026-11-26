---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The two above-threshold lengths add on disjoint time intervals; their exponentiated sum is W(a)=min(max(a,1),1/q)max(1,d−ra), r=1−q, with the post-dose tail included and equality instants of zero measure. For d≤1 all allocations give W=1. For d>1 the two unsplit endpoints give W=d. If a≤1 then W≤d with equality only at a=0; if the second level d−ra≤1, W≤d with equality only possibly at a=d. Where both peaks exceed threshold before the first factor caps, W=a(d−ra), strictly concave. Past the cap 1/q the improving portion of W declines strictly. For q<1/2, the interior vertex is feasible at d=4r, has a=2 there and is the unique third tie; its value d²/(4r) exceeds d strictly thereafter until it reaches the cap at d=2r/q. At and above this second threshold the cap wins: its excess over d is r(qd−1)/q²>0. For q≥1/2 the quadratic increases up to the right feasible edge since d−2ra≥d(1−2r)≥0, strictly except possibly at an endpoint; no split wins before d>1/q, and beyond that the cap uniquely wins. At q=1/2 and d=2 there is no third optimizer. The two formulas agree at the transitions. In the stated reversal interval the equal first increment is inside the quadratic branch and W(d/2)=d²(1+q)/4<d, whereas the best split has W>d. The example gives 961/300>31/10>961/320. The strict reversal is claimed within q<1/2, not claimed to occur only there. Inspected the rational frozen checker without execution; the continuum claim rests on branch comparisons, not rational sampling.

## originality

PASS

Linear clearance, superposition and time over an exposure threshold are prior ingredients. The supported difference is the exact global dose-share diagram with all ties for two fixed administrations under a single budget and unbounded observation, together with distinct onset types and the strict equal-split reversal. The prior comparison is provisional, particularly for unavailable older PK sources.

## value

PASS

Fixed-interval fractionation and level-set duration give a natural minimal exposure benchmark. The exact switch between discontinuous interior-split onset and continuous emergence at the cap explains when a gap in coverage is optimal; the open reversal region disproves a natural equal-split heuristic. Its value is the exact structure and counterexample under the model, not practical prescribing or a biological efficacy result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
