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

# Reproducible checks

Run `python3 verify_wheel_direct.py` and `python3 verify_wheel_transfer.py` from a directory containing the embedded programs. Each is standalone Python 3 and uses only the standard library. The direct program enumerates all edge directions, detects cycles by topological elimination, and transforms the resulting indicator by exact Walsh butterflies. The transfer program independently forms the two-state integer matrix product, checks exact Parseval sums, parity spectra, and the magnitude-two/odd-zero witness families.

The executed programs returned `DIRECT_WHEEL_OK` and `TRANSFER_WHEEL_OK` for all rim sizes from three through eight. Exact direct Walsh ranks were 16, 128, 346, 2048, 6252, and 32768 in that order. Their full frequency arrays were additionally cross-compared through seven rim vertices. No numerical approximation is used; checks are finite and do not replace the all-length proof. Source priority has been reviewed only against identified accessible materials; no independent mathematical audit has been performed.
