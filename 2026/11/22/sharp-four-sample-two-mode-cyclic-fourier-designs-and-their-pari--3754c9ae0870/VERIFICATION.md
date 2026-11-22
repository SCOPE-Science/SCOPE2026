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

Run `python3 check.py` using only the Python 3 standard library. The checker enumerates all four-site subsets for every cyclic order from 4 through 36, computes independent root sums, Gram determinants, extremal eigenvalues, and inverse traces, then matches the entire extremizer family. The observed output was `CHECK_PASS orders=4..36 four_subsets=435897`. The all-order result follows from the analytic geometric argument in `RESULT.md`, not from this finite check. No independent audit has been conducted.
