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

# Reproducible mathematical checks

This document describes finite corroboration and the independent scientific verification status. Execute `python3 checker.py` from the package directory. The checker needs only the Python standard library and performs no network actions.

The checker independently enumerates all three-valued integer one-Lipschitz assignments on grids of sizes \(3\)-by-\(3\) and \(3\)-by-\(4\), checking the exact maximum numerator; enumerates every pair of cross-separated extreme sets on grids \((3,3),(3,4),(3,5),(3,6),(4,4),(4,5)\), recording all winning geometric types; then checks the closed-form phase/tie identities for all integer \(3\le a\le b<300\). Integer arithmetic is exact.

Expected final marker:

`ALL_RECTANGULAR_DISJOINTNESS_SPREAD_CHECKS_OK`

The universal proof is in `RESULT.md`: connected tight-edge graph gives integrality, direct-product diameter two limits the range, the row/column cross-separation lemma classifies feasible extreme levels, and strict envelope inequalities yield the phase diagram. Finite experiments do not establish universal completeness; they only test the derived assertions at specified sizes. No independent mathematical audit has been performed.
