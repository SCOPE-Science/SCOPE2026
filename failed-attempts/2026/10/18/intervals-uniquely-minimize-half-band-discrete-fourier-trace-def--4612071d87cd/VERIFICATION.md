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

Integrating over [−1/4,1/4] gives K(0)=1/2 and sin(πk/2)/(πk) for k≠0. Squaring and counting both orders of each unordered pair gives D=N/4−(2/π²)E, where E sums inverse squared odd distances. For a cutoff at 2r+1 the leftmost point has degree at most r+1, and any point of the larger parity class has degree at most floor(N/2). Removing a point of degree at most the minimum of those bounds proves the count comparison by induction, since the new interval endpoint realizes that minimum. The positive telescoping weights (2r+1)^−2−(2r+3)^−2 transfer all counts to E; the first count has gap c(Ω)−1 with weight 8/9. This proves strictness off intervals and the exact penalty, with uniform equality at N=2 and {0,3}. Singletons have the stated constant defect.

## originality

FAIL

Mayeli supplies the trace identity. More decisively, Pollard's classical truncated representation-sum theorem already gives the simultaneous all-cardinality edge inequalities by splitting the integer sites into even and odd classes and applying its majorization bound to the rescaled difference counts. The same positive layer-cake and the elementary first-cutoff count give both strictness and the uniformly sharp penalty. The reviewed proof is valid and elementary, but the stated results are a corollary of the stronger known rearrangement bound, not a gap left by the more closely named asymptotic isoperimetry papers.

## value

FAIL

The optimizer and component count are naturally motivated, and the short induction is a useful exposition. As a research claim, however, the exact result follows from the older representation majorization under the parity reduction, with the first layer and a two-site check accounting for the sharp coefficient. No additional nonmechanical extremal invariant or new band is established by the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
