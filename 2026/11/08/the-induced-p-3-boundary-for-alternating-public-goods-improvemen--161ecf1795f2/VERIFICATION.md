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

The equilibrium equations (I+A)s=1 have a solution over F2 because for z in the nullspace of the symmetric matrix I+A, zᵀ(I+A)z=1ᵀz=0 (A alternating/zero-diagonal), so 1 is orthogonal to the kernel. In clique components, odd active parity is precisely best response for all; even parity makes all dissatisfied, and one improvement changes parity to odd. Thus every maximal path length is exactly the number of initially even components. Any non-cluster graph has induced P3 a−b−d; fixing d=1, other external vertices zero and flipping a,b in four legal steps yields 4-cycle. Parity forbids odd cycles; two-step reversal of a fixed bit without neighbor change is impossible. This covers all finite simple undirected graphs and unilateral strict improvements.

## originality

PASS

The prior multi-action conformist/rebel FIP criterion concerns m≥3 and edges joining opposite types with unused stubborn colors, not alternating binary parity best-response across open neighborhoods. Known 2021 parity equilibrium linear algebra covers part 1 but not all-schedules clique dichotomy. No decisive covering prior found.

## value

PASS

A sharp graph-theoretic forbidden induced subgraph criterion for convergence with an always-present equilibrium, and the exact minimal cycle and path lengths, distinguish equilibrium existence from robust improvement dynamics in a natural public-goods model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
