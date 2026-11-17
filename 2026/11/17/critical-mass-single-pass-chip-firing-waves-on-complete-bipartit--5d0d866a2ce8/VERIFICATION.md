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

The standalone Python standard-library files `enumerate_states.py` and `construct_waves.py` independently implement the dynamics and the ordered-partition construction. Run them with `python3` from the same directory. Embedded `enumerate_states.out` and `construct_waves.out` contain the captured stdout of successful actual runs.

`enumerate_states.py` visits every nonnegative chip composition of mass \(mn\) for the nine graphs shown in its output, including all 245,157 states on \(K_{4,4}\). It uses state transitions to find periodicity and filters periodic states by exactly one firing per vertex per least period, then compares the observed census with the closed formula. This finite enumeration is not a general proof. `construct_waves.py` independently generates ordered surjections, verifies unique initial states, prescribed firing rounds and returns for five graphs. The human-readable proof establishes all positive shore sizes.

The theorem does not claim coverage of fixed points, transient attraction basins or multiple-firings-per-period sectors. Literature comparison includes explicit period constructions and general firing-pattern restrictions, with residual uncertainty from an inaccessible source-reversal paper. Self-review was completed; no independent scientific validation is asserted.
