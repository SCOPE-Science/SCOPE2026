---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The selected rook vertices are edges of K_{p,q}; their induced line graph is a forest exactly when the selected edges form a linear forest. Opposite-shore unsaturated vertices in different components could be joined; if an A vertex is unsaturated, a B vertex must also be unsaturated because 2q exceeds the forest bound, and all components have an unsaturated vertex. This forces a spanning path and hence p=q. Otherwise A is saturated and has 2p selected incidences, which gives maximality in the unbalanced case. Counting alternating labeled paths gives the stated exponential series: equal positive shore sizes give one orientation choice from the A end, and unequal sizes require division by two. For maximal unbalanced forests c paths use p+c B vertices and the ordered positive compositions of p supply the binomial coefficient, with c! for unordered paths. Complements give the feedback-vertex-set claim. Independent rook-adjacency enumeration of all 64 subsets of the 2-by-3 board and all 32,768 of the 3-by-5 board confirms the counts and maximality, including the latter's 360 one-component and 180 two-component maxima. Replay: /workspace/branches/8b663860-6b9a-46da-9225-c6481a8d838e/independent_rook_enumeration.py; adjacent independent_rook_enumeration_output.txt. This finite check does not prove the general statements. Frozen verification script and output inspected, not executed.

## originality

FAIL

The 2026-10-12 catalogue record gives a stronger enumerator and the identical extremal profile on the same labeled graphs; the 2026-10-18 record explicitly covers the identical maximality classification and size. These are distinct records and verified statement-level overlaps, not title hits or a claim about order within a shared date. No substantive claim remains outside their joint coverage.

## value

FAIL

Purity and the size/component data would be useful for the natural rook-graph feedback problem, but the submission adds no scientific content beyond the already available classification and stronger component enumerator. The bounded reproduction corroborates their common result and is not a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
