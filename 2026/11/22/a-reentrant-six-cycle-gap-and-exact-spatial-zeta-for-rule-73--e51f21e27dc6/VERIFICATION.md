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

Run `python3 verification/verify_transfer.py` to reconstruct all temporal-history graphs, check every integer determinant coefficient, verify the mixed-period return walks and compute the Perron bounds. The expected last line is `EXACT_TRANSFER_OK`.

Run `python3 verification/check_direct.py` to independently simulate the Rule 73 map on every binary initial state on ring lengths three through fifteen. The expected last line is `BRUTE_RING_OK`. Both programs have passed when run from the files embedded with this finding.

Finite direct simulations prove only the inspected ring sizes. The graph transfer and based-walk concatenation establish the asserted all-length statements. This work does not classify attraction basins, transients or other temporal periods. Independent external mathematical validation has not been performed.
