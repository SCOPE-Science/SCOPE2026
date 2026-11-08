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

# Checks and reproducibility

`check.py` performs 377 deterministic exact-rational assertions. It reconstructs prescribed duration moments from release-phase moments in both inverse directions across nine discrete clock pairs, checks an explicit four-atom example with matched means and second spatial moments but distinct fourth spatial moments, and constructs rational null vectors for finite data depths from one through eight. The nullspace existence for **every** integer depth follows separately from the matrix dimension count in the proof.

`simcheck.py` uses a deterministic seeded simulation of 180,000 switching cycles and numerically compares the first three conditional release-phase excess-variance moments against the analytical recurrences; its relative errors are below 0.003 at this sample size. This is a stochastic consistency check, not an infinite-dimensional certificate.

Reproduce with Python 3 standard library: `python check.py` then `python simcheck.py`, from a directory containing both files. The mathematical proof requires no computation or external files.

The exact identifying theorem assumes knowledge of *all* conditional released-state spatial moments and one duration law. Finite-dimensional tests do not establish stability from finite data. No independent external audit or experimental replication was performed.
