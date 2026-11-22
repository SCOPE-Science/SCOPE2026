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

## Reproducible checks

Execute `python3 CHECK.py` using the standard Python library. This constructs the nonorthogonality graph on all nonzero \(2r\)-bit vectors for \(r=1,2,3\), enumerates every clique (including the empty clique), and independently accumulates completions by subsets of explicitly generated maximum cliques. It checks the exact even-size formula, the odd-size zero-sum obstruction and positive count, the unique top even-clique extension, and the \(1,6,288\) projected maximum-clique totals.

The output includes all size distributions and terminates with `SYMPLECTIC_CLIQUE_EXTENSION_SPECTRUM_OK`. The all-rank result follows from the proof and is not certified by finite tests. No independent mathematical audit has been performed.
