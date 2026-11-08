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

# Reproduction and limits

Run both included programs using Python 3.10 or later, from the folder containing `RESULT.md`:

```
python verification/direct_update.py
python verification/phase_patterns.py
```

The direct checker performs three literal updates (not an inferred periodicity test), then checks return and nonfixity for all \(3^n\) states on every \(C_n^2\), \(5\le n\le11\), at thresholds one, two and three. It tested 796797 triples of graph, threshold and initial state. The second checker independently uses an alphabet with a nonrotating marker and phase symbols to count valid local three-round patterns; it tested 2795520 augmented assignments on \(5\le n\le10\) at thresholds two and three. It also checks the constructive lower-bound family of \(3\cdot2^m\) words for \(2\le m\le9\).

Recorded standard outputs appear in `verification/direct_update.out` and `verification/phase_patterns.out`. All assertions succeeded when the included programs were run. These checks cover only finite sizes; the universal assertions rely on the sitewise-dichotomy, directed-edge counting, complex-eigenvector, and consecutive-triangle proofs in `RESULT.md`. No independent audit has been performed.
