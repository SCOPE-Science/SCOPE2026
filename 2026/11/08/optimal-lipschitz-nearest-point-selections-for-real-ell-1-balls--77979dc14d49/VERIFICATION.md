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

# Verification of the sharp nearest-point selection theorem

Run `python verification/check.py` with the Python standard library. The script uses exact rational arithmetic throughout. It checks 10,589 assertions, including KKT-style positive-threshold feasibility, the exact distance-to-ball identity, finite-dimensional global Lipschitz estimates over deterministic rational test pairs for dimensions one through eight, induced \(\ell_1\) centering-matrix column sums, and boundary-simplex lower-bound witnesses. The observed successful output was:

```
L1_METRIC_SELECTION_SHARP_OK 10589
```

The proof of the universal all-selector lower bound is analytical, based on permutation averaging and minimax optimization over a zero-sum hyperplane. The finite tests do not exhaust possible selections, cannot independently certify the infinite-dimensional statement, and are not an originality or publication-priority check. The full text of the most directly relevant 2026 preprint was not available for complete comparison; the published related full results and accessible abstracts were compared under best knowledge.
