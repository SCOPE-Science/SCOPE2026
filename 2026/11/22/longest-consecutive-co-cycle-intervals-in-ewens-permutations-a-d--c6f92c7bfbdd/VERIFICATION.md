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

A standalone Python 3 script (`checker.py`) compares the exact longest-co-cycle-run distribution from every labeled permutation with a separate enumeration of set partitions weighted by the number of cyclic arrangements within blocks. It checks sizes 2–8 and prints exact rational distributions.

The script does not assert, numerically or otherwise, the almost-sure logarithmic law or the conditional Poisson limit. The infinite conclusions are justified analytically by the paintbox representation and the estimates in `RESULT.md`.

The largest-atom uniqueness, integer-threshold qualification, second-largest-mass gap, and Dickman continuity assumptions are specified in the proof. No independent audit has been performed.
