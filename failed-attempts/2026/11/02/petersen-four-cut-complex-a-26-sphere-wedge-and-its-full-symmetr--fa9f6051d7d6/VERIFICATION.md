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

Reconstructed the ordinary complex by nontrivial cuts in four-vertex sets. A separate set-based enumeration and depth-first acyclicity test reproduced (10,45,120,210,240,140), 3330 Hasse incidences, 369 disjoint pairs and exactly one critical vertex and 26 critical facets. Forman's theorem then gives the actual wedge, not just mod-two Betti numbers: the five-cells all attach to the sole zero-cell. Enumeration confirms the five stars are all independent 4-sets and there is no independent 5-set; intersecting stars recovers every vertex, so the label action is the full group. For a fixed face that is a union of k vertex cycles, oriented alternating trace has sign (-1)^(k-1). This independently gives top traces (26,6,-2,2,0,0,1). The characters of the standard, the two-subset permutation module minus the point permutation module, and the exterior square of the standard identify [41], [32], [311] and verify the stated multiplicities. Barycentric face flags have pointwise stabilizers when preserved setwise; quotient chains are the coinvariants, an exact functor over Q by averaging, yielding the stated top rank and no other reduced rational homology. Replay: python3 -B /workspace/branches/frozen_review_replay.py 5. The check concerns only this graph and does not assert integral results for the quotient. Frozen verifier inspected, not executed.

## originality

FAIL

Demonstrable duplicate coverage: the distinct 2026-10-25 Resultary record gives the same ordinary complex, wedge, integral homology, rational Specht decomposition and S5 quotient ranks, plus the A5 quotient. The 2026-10-18 record independently duplicates the wedge and representation. This is statement-level coverage rather than a claim about authorship or priority.

## value

FAIL

The natural small graph and equivariant invariant would be a meaningful exact benchmark absent prior coverage. Here the earlier record already provides this benchmark, including the same finite Morse strategy and a stronger quotient comparison. Swapping the matching order adds no demonstrated scientific use or distinct invariant. No surviving value-bearing repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
