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

The standalone `checker.py` runs directly in Python 3 with the standard library. It reconstructs independent binary visit histories and checks exact rational mass normalization, full and OR Fisher information, the complete-history boundary chi-squared formula, the data-processing inequality, and the unbiased occupancy estimator's variance. It also examines the bounded and divergent replication regimes and numerical lattice-phase approximations. Executing `python3 checker.py` from this directory returned `PASS 191 exact and numerical assertions`.

Analytical proof, including uniform bounds over all integer replicate counts and the one-sided asymptotic, is in `RESULT.md`. Finite checks establish no exhaustive statement about the continuous parameter range; the proof supplies it. This file contains no independent or external audit claims. A cited 1985 repeated-testing study was available only in abstract and remains a material historical-priority limitation.
