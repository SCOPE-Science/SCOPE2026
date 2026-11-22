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

# Reproduction and evidence

The complete finite certificate is the pair of standalone C++17 programs `frucht4_a.cpp` and `frucht4_b.cpp`; `verify_graph_witness.py` independently checks a label isomorphism and a sharp transient witness; `verify_census.py` checks both enumerators’ output agreement and all derived counts. No precomputed transition table is required. Each program constructs all \(4^{12}=16{,}777{,}216\) successors, identifies every least-period cycle and assigns every initial state to its cycle and first entry time. The first uses indegree peeling and reverse deletion; the second uses path-marking with a distinct graph construction and update implementation.

The recorded output files `frucht4_a.out` and `frucht4_b.out` have the same `ORBITCOUNTS`, `MAX_STATES`, `BASIN_SIZES_BY_PERIOD`, and complete 72-entry `HIST` sections. The CSV `joint_census.csv` contains each nonempty entry-time/period cell. Count checks: 1,037 cycles, 4,159 periodic configurations, 16,777,216 initial configurations, and exactly 18 configurations entering a primitive four-cycle at time 27. The witness program prints `GRAPH_ISOMORPHISM_OK` and `WITNESS_OK` for initial encoding 5999879. Recompile/replay commands and precise graph definitions appear in `RESULT.md`.

The proof uses exact integer arithmetic and exhaustive traversal, not a statistical sample, numerical extrapolation, or an infinite certification assertion. The maximum 27 and orbit list refer only to this graph and update rule; no general theorem about other graphs is asserted. The review is same-model only, with no independent external audit.
