---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

A closed-neighborhood identifying code C is exactly a mask whose 14 bitwise neighborhood intersections are nonempty and pairwise different. Since there are 2^14=16384 masks, enumerating all 0<=|C|<=7 is complete: no masks size<=6 qualify, exactly 268 size-seven codes qualify. A legal slide between two codes changes exactly one chosen vertex to an adjacent nonchosen vertex, equivalent to two bits in the XOR and adjacency of the two changed vertices. Independent full-pair enumeration yields precisely 210 slide edges; connected components have sizes 4 (56) and 22 (2), with degree fingerprints (1,1,1,3) and (1 repeated 21,21), forcing the claimed star forest. This is a true finite exhaustive proof, with no extrapolation to other Heawood-like graphs.

## originality

PASS

No claim-dominating theorem was found in inspected primary sources and published mathematical record searches; originality is best of knowledge with explicit residual risks.

## value

PASS

Identifying codes are a standard natural code invariant on the canonical Fano incidence graph; token-slide connectivity encodes local reconfiguration feasibility. The complete star-forest fragmentation, despite an existing much more connected unrestricted token-jump graph, is a meaningful finite structural graph classification rather than just another code count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
