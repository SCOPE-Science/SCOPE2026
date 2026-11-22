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

The general claims were proved by the local intertwiner table, independent block factorization, cyclic transfer trace, and positivity of the divisor-sum remainder. A standalone Python 3 checker, `checks/cyclic_check.py`, directly enumerates all maps with cyclic character and all idempotents for block counts 1 through 5. It checks every commutation equation pointwise and compares exact rank-polynomial coefficients with the claimed closed forms. Aggregate totals are 8, 104, 960, 8320, and 64000. For block counts 1 through 7, exhaustive binary-word enumeration verifies the three minimality cutoffs for the unindexed spectrum, indexed spectrum, and strict homometry; the two eight-block patterns have the same ordered autocorrelation and common centralizer size 5504. All checks finished successfully with terminal marker `LOCAL_INTERTWINER_AND_CYCLIC_SPECTRA_CHECKS_PASSED`.

Finite enumeration is supplementary and does not establish the all-degree formula; no independent external validation is claimed. The earlier literature on transformation centralizers, partition-character semigroups and homometric sets is explicitly credited. No claim is made about uniqueness of the resulting rank fingerprint outside the stated classifications and bounds.
