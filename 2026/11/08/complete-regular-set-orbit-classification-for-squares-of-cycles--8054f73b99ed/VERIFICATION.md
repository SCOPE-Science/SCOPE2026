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

# Reproducibility

Execute `python3 verify.py` (Python 3.8 or later). It needs no external packages or data files. The verifier constructs the four-bit transition graph for each of the 25 ordered parameter pairs, identifies every nonconstant cycle, and compares it against the theorem's eleven primitive words. It also independently enumerates all binary graph subsets for \(5\le n\le14\), with neighbor counts computed from graph adjacency rather than from the recurrence. Finally, all listed rotated/repeated classes are checked directly in the graphs up to \(n=180\).

Observed output from the packaged source:

```
ALL_25_PARAMETER_STATE_GRAPHS_OK 400 states 11 nonconstant primitive cycles
INDEPENDENT_EXHAUSTIVE_GRAPH_CHECK_OK n=5..14 total_bitstrings= 32736
ALL_CLASSIFIED_FAMILIES_DIRECTLY_CHECKED n=5..180
VERIFY_OK
```

The proof's exhaustive core is the finite 16-state cycle classification, not any extrapolation of the graph experiments. The 400 transitions arise from 25 parameter pairs and 16 binary states. The independent graph checks cover 32736 bit strings in the stated range, including the empty and full strings, which are deliberately excluded by the mathematical definition. This document does not claim independent external validation.
