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

## Checks performed
Replayed `verify_patterns.py` with Python 3 standard library. The script passed 362934 exact assertions: every permutation through order eight, deterministic pattern-cardinality bounds, aligned-shift matchings through length seven, and exact equality-event probabilities for every feasible pair of windows of total length at most eight. The exact output at order eight was \(\mathbb E X_8=27823/1260\), agreeing numerically with the previously reported value near 22.08.

## Proof boundary
The general theorem is established by deterministic factorial cutoffs, an alternating-matching argument for overlapping windows, factorial tail sums and Stirling's formula. Finite enumeration is a consistency check only. No independent mathematical audit, concentration proof, or publication-priority certification has been performed.
