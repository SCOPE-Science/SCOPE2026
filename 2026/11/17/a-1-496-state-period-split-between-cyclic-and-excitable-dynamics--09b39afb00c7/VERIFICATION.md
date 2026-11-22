---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The 12-vertex labeled graph and both synchronous threshold-one maps are precisely defined; the two complete transition programs independently classify every one of 3^12=531441 states by functional-graph decomposition, with no trajectory cutoff. I separately implemented the transition and active-path cycle classifier in optimized C++ from the displayed 18 edges and recomputed the entire joint matrix: (1,1):52563, (3,3):282990, (4,4):62952, (5,5):90432, (6,6):24636, (7,7):12840, (8,8):3532, (8,4):1496; sum 531441. Distinct orbit lengths are exactly least periods because cycle traversal closes at its first repeated state. The LCF conjugacy and explicit period-eight/four witness are supplied; auxiliary orbit and depth totals rely on the inspected exhaustive code rather than a second independent full depth replay.

## originality

PASS

Best-of-knowledge novelty is the complete joint CCA/GHM initial-state period census on the asymmetric Frucht graph, not the already reported Petersen period-eight/four phenomenon, nor the GHM marginal Frucht period table.

## value

PASS

The Frucht graph is a canonical asymmetric cubic graph; its absence of spatial automorphisms tests whether the paired-model period discrepancy seen on symmetric Petersen networks requires symmetry. The exact 1496-class exceptional basin and complete cross-tab are a natural finite classification of two standard dynamical rules. The graph and joint invariant are motivated independently of the computed number; no unsupported generality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
