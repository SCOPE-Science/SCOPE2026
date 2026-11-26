---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In a cubic triangle-free graph of this order, the first force from three black vertices leaves a closed neighborhood whose leaves each have two white neighbors, so at least four seeds are required. For four seeds, a one-row set needs a consecutive triple for a first force and cannot advance unless the fourth extends it. With three seeds on one row and v_0 on the other, omission of u_0 makes the only possible first force stall; with u_0 present, exactly one horizontal neighbor of u_0 must be initially selected. After reflection, choose the force u_0→u_{−1}; the third upper seed must then be at ±2 to enable another force. Other initially legal choices do not invalidate this necessity: a stalled closure after any legal sequence contains every reachable forced vertex, by monotonicity. With two seeds on each row, a first force requires an adjacent row pair with a shared column and stalls if the opposite pair is nonadjacent. With adjacent pairs the relative shifts are exactly −1,0,1. Each surviving template makes two adjacent full rungs, which propagate both ways. The types are disjoint and have the claimed multiplicities. Independently verified all five rows of the exact intersection-three table by triple incidence, using integer anchors −5,…,5 and separately cyclic n=6,…,15; replay: python3 /workspace/review_ladder_overlap.py. Any candidate sharing a vertex has an anchor in that integer interval up to reduction, and all its columns and the representative's lie in [−7,8], where reduction is injective for n≥16. This certifies the table on the entire stated range, not by extrapolation. The degree polynomial and 48n follow by summing degrees. Aligned states for consecutive anchors are joined through a shifted state, and the table attaches all other types. The supplied scripts and saved outputs were inspected, not executed; the n=5 profile is only supporting boundary evidence.

## originality

FAIL

The distinct 2026/10/13 Resultary record covers the full labeled minimum-set family and 13n count on n≥5. More decisively, the distinct 2026/10/18 token-jumping geometry record has the identical exchange graph definition and n≥6 hypothesis and already states connectedness, 48n edges, all three degree multiplicities and the same full type-neighbor quotient after reordering types. The date does not decide which came first; the original claim has no demonstrated distinct content in this comparison. The finite n=5 boundary note is corroboration, not a surviving standalone scientific claim.

## value

PASS

Optimal seed geometry and one-token mobility are natural questions left open by knowing only Z=4. The uniform local exchange table, global degree counts and explicit connectivity are useful exact data on an infinite family, while n=5 delimits the stable range. Those substantive results are already covered; the frozen record does not specify a distinct result deserving a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
