---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Conjugate the right-shore bits to make a neighbor-majority process with a flip on ties. When n odd, one shore has at least its pivotal majority threshold, and a sequence of permitted updates drives all vertices to one polar state. When n even and t<n, all cases except balanced a=b=n/2 likewise polarize; an undeleted-index vertex at the balanced point has an exact tie and can flip to exit this case. Hence every state reaches one of two absorbing states. When n even,t=n all degrees are odd, every actual flip strictly raises the cut and recurrent states are precisely fixed points; the two-shore inequalities force either a polarization or opposite bits across each deleted pair and exactly n/2 positive indices, giving C(n,n/2). Independent direct enumeration for n=3..6, all t, computed all stable configurations and reverse reachable sets from them; every state reaches the claimed absorbing set. This bounded check does not prove all n.

## originality

PASS

Rouquier–Regnault–Thierry established foundational asynchronous minority, energy and bipartite duality, but their studied examples do not include this complete matching-deletion threshold. A separate published same-graph anti-coordination Nash-census theorem counts weak Nash equilibria and recovers the even full-deletion binomial number; this overlap is explicitly credited. For partially deleted matching, weak equilibria with ties are not absorbing under the required tie-flip dynamics, so that static theorem does not imply only two recurrent classes or almost-sure absorption. The sharp dynamic restoration theorem survives under bounded comparisons.

## value

PASS

A natural interpolation between a complete bipartite network and a crown graph has a sharp last-edge change in zero-noise asynchronous dynamics. Restoring a single edge eliminates exponentially many suboptimal absorbing configurations that retain only about half of the maximum cut. The distinction from weak local Nash stability is mathematically substantive for tie-sensitive dynamics and motivates the exact recurrence-free classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
