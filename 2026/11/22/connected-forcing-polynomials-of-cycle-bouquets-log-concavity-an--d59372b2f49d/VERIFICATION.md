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

Run `python3 CODE/bouquet_verify.py` from the extracted bundle. The script constructs the graphs independently of the petal polynomial implementation, searches all initial subsets of the stated labelled test graphs, checks connectivity and the standard forcing closure, and compares their full size distributions to independent polynomial convolution. It also checks the resulting extremal coefficients, total counts, and log-concavity on longer examples, and prints `VERIFY_OK` only after every assertion succeeds.

The checker is a finite corroboration of the exact all-order structural proof in `RESULT.md`; no inference about all graphs is drawn from a finite experiment. The log-concavity theorem uses a classical convolution theorem, and the real-zero obstruction uses a normalized Newton inequality. No independent external audit or validation has been conducted.
