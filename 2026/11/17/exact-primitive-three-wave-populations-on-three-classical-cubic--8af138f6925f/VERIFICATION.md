---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

On a connected graph, a GH configuration of exact temporal period 3 has all vertices cycle phases or is all resting; a resting vertex cannot neighbor an always-cycling vertex. Fully cycling phase coloring c(v) in Z3 advances iff each vertex has some neighbor c(v)+1. On three connected cubic bipartite incidence graphs with shore sizes m=8/9/10, fix first point phase to zero, enumerate all 3^(m-1) remaining point colors and each allowed line phase; require union of point-successor coverage masks = all point vertices. Factor 3 for global color rotation. The disjoint cover count yields 54036,134478,645180 phase states and 18012,44826,215060 primitive three-orbits. Independent new inclusion-exclusion algorithm using graph encodings reproduced the full three integer counts; no inference from sample or partial census.

## originality

PASS

Best-of-knowledge: Gravner–Lyu–Sivakoff (2018) defines exactly the 3-color GH dynamics and characterizes synchronization/activity by conservative initial forms and cycle winding (Theorem 3) on arbitrary graphs, but does not list these exact primitive-three phase counts. Published full-subdivision GH 3-periodic formula concerns graphs with inserted degree-2 edge vertices, not these entirely degree-3 Möbius–Kantor/Pappus/Desargues Levi graphs. Other GH line graph and Heawood population counts concern different objects and/or thresholds. A targeted search for named 16/18/20-vertex populations found no numerical implication. Unindexed specialized color-count tables remain a risk.

## value

PASS

The three historically canonical finite cubic symmetric incidence graphs are natural objects, and exact primitive-three excitation population is a dynamical invariant with a clear definition, useful for benchmarking constrained waves versus total recurrent populations. It is an independently unknown exact census of nontrivial graph/coloring interaction, requiring full 3^(m-1) mask cover enumeration, not a gratuitous tiny arbitrary slice. No general/all-period classification or downstream theorem is required for this independently useful exact finite fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
