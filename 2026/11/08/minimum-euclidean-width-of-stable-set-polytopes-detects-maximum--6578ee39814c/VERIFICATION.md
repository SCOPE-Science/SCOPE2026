---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Re-audited the repaired theorem. On each stable color class, the sum L_j of absolute weights is bounded by width w, and the squared mass Q_j is at most L_j². The color-class deficits d_j=w²−Q_j sum to δ. The peak m_j satisfies Q_j≤m_j w, so both its deficit from w and the entire off-peak L1 mass are ≤d_j/w. This gives squared error ≤2d_j²/w² per class when replacing the peak by signed w and zeroing the tail. The alternative off-peak squared bound Q_j−m_j²≤Q_j(1−Q_j/w²)≤d_j independently gives the frozen estimate, justifying the minimum of the two. At the strict threshold δ<w², each pair of peaks has total magnitude >w, ruling out opposite signs by singleton supports and same-sign nonedges by a stable pair. For q=1 the peak is automatically nonzero and no pair condition is needed. The final normalization costs precisely √q(w−1/√q). The exact clique width and minimizers follow at δ=0. The complete-graph perturbation and the two-vertex edgeless perturbation have both distance and deficit asymptotically proportional to the perturbation parameter, so no o(δ) uniform rate is possible at fixed q. The repaired result's polar comparison follows by taking the zero-height section and maximizing projected norm, not by identifying an ordinary inradius with width.

## originality

PASS

This pass applies to the repaired quantitative result only. The exact baseline is demonstrably covered by the published Hansen-polar description (same date, no inference of priority), and the ordinary chain-polytope case has earlier equivalent coverage via the enriched support. The repaired finding explicitly credits both. No inspected statement gives the explicit linear deficit bound independent of graph order, or its sharp order, in the nonperfect as well as perfect χ=ω class.

## value

PASS

On a natural class wider than perfect graphs, the repaired theorem recovers a specific signed maximum clique from an almost thinnest direction, with a distance bound independent of graph order and optimal linear order in the small deficit at fixed q. Compactness for any fixed polytope gives neither a uniform constant nor this rate. The specialization also controls approximate recovery of longest chains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
