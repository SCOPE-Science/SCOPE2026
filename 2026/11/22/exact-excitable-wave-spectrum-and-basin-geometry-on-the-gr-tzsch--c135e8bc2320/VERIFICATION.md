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

# Verification record

All scripts use only the Python 3 standard library; `COUNTS.json` is an exact reference census, not an unexplained simulation log.

```text
python3 verify_decomposition.py
python3 verify_trajectories.py
python3 verify_irrotational.py
python3 verify_basecycle.py
```

**Checks performed:** the functional-graph algorithm enumerated every one of the 177,147 configurations and established 1,291 recurrent cycles, with periods and basins in `COUNTS.json`; direct trajectory tracing independently matched every cell and each individual basin-size histogram; the cycle-basis implementation independently obtained the 13,887-state extinction basin without simulating trajectories; the five-cycle baseline independently yielded one fixed orbit, two period-five orbits, and basins of 153, 45 and 45 configurations. The exact nine-step witness is encoded by state number 1985 in `COUNTS.json`.

**Limits:** The proof is finite, exact and machine-checkable by full enumeration; it is not a theorem about all Mycielski graphs or stochastic excitation. Independent external validation has not been performed. Historical novelty checks cannot rule out all unindexed earlier computations.
