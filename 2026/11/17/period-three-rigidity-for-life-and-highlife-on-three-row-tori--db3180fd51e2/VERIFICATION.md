---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof's finite component lemma was checked using three actual code paths. `space_time_graph.cpp` constructs all 262144 pair states for each rule, enumerates 294072 or 321875 directed transitions, computes all strongly connected components, and tests all recurrent pair histories for temporal constancy. `independent_graph.py` independently constructs those transitions via a different neighborhood implementation and uses NetworkX's SCC algorithm; it reproduces two cyclic components of sizes 30 and 27 and zero time-varying cyclic vertices. `direct_evolution.cpp` checks every binary configuration at horizontal widths three through seven for both original synchronous maps, confirming zero primitive period-three states. Reproduced textual results are embedded in three separate output files.

The finite graph is exhaustive and its cyclic-walk correspondence applies for all horizontal circumferences; the direct small-width evolution is not presented as an infinite proof. No formal assistant-independent or external audit was carried out. The theorem neither classifies other temporal periods nor proves absence of larger-width oscillators. Historical-priority uncertainty persists for inaccessible catalogues and archives.
