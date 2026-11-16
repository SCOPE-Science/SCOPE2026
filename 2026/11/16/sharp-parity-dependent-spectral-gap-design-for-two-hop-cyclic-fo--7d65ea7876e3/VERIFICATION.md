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

# Verification

The exact proof is self-contained in `RESULT.md`. The diagnostic script `check.py` constructs the full complex-normal cyclic shift matrices, computes dense singular values, compares the two-mode spectral envelope at 201 weights, and verifies the theorem's formula for each \(3\le n\le100\). Running `python check.py` requires Python 3 and NumPy and produced `PASS 392 independent finite assertions over n=3..100`.

The numerical comparisons use double precision and finite cycle sizes; they cannot prove uniqueness, a result for all cycle lengths, or absence of earlier equivalent results. Those claims rely on the analytic proof and literature comparison in `RESULT.md` and `REVIEW.md`. No independent audit has been performed.
