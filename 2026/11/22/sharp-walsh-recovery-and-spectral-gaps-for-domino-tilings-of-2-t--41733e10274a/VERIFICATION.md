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

Run `python3 check_direct.py` and `python3 check_recurrence.py` using Python 3 standard library only. Both completed successfully when extracted from the package. `check_direct.py` enumerates domino tilings and performs full Walsh transforms for widths one through six, comparing every coefficient with an independently implemented transfer recurrence. `check_recurrence.py` counts normalized signed-continuant states through width fifteen and verifies every stated parity, nonzero spectral minimum, maximum and the constructive nullity bound, along with the five displayed exact zero counts.

The infinite-width proof is in RESULT.md. Exhaustive experiments for bounded widths are not presented as an infinite proof. Neither program computes an independent literature audit, a closed-form nullity at all widths, or a sharp \(\ell^1\) projection norm.
