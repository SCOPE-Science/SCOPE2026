---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For two named fixed-size teams (s>=t>=1, a,b>=1, a+b=s+t), only opposite-type cross-team exchanges alter utility. Exact gains for decreasing occupancy x are (2x-a-d-1,2x-a-1), for increasing x (a-2x-1,a+d-2x-1), d=s-t. Endpoint availability is checked. Thus SSS iff a-1<=2x<=a+d+1; SS agrees when d=0, otherwise uses strict bounds. Welfare W=2[x(s-x)+(a-x)(t-a+x)] is a strictly concave quadratic centered at (2a+d)/4; total moving-agent gain is half of an adjacent welfare difference, so SSTU iff global welfare maximum over feasible integer x. Labeled counts C(a,x)C(b,s-x). Independently reimplemented direct gains/utility for 3439 labeled allocations through 9 agents, including first separation examples; no extrapolation from the finite checks.

## originality

PASS

The examined exact primary statements and indexed Resultary claims, including direct implication/subcase checks, do not cover the surviving complete theorem as scoped. Specific overlaps and uncertain inaccessible full texts are recorded; negative searches are not taken as novelty proof.

## value

PASS

Two-team fixed-capacity complete bipartite friendships is an elementary but natural canonical instance of fixed-size hedonic games. The complete equilibrium and labeled multiplicity classifications for all three standard exchange notions, exact efficiency criterion and sharp first sizes when notions diverge capture how capacity imbalance changes strategic stability, beyond mere existence or coarse PoA bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
