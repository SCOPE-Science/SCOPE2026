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

# Reproduction

Run `python3 CHECK.py` using Python 3 standard library. The finite exhaustive rational calculation checks all base alphabet words for \(M=2\) through \(n=8\), \(M=3\) through \(n=5\), and \(M=4\) through \(n=4\); it verifies the histogram and base-boundary-corrected index imbalance. Success marker: `HETEROCHAOS_INDEX_HISTOGRAM_OK`. The checker enumerates finite periods only; the all-degree proof is in `RESULT.md`.
