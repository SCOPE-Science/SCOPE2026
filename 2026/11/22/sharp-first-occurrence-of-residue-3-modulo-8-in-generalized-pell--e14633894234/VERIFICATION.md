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

The standalone `checker.py` tests the recurrence and the formal-series convolution separately. It checks every earlier index for all exceptional orders and all orders through 2000, then compares each of the 6 theoretical residue rows. The unbounded case is proved by the exact formal power-series identity and the cut-off \(k+16\le2k+2\); no finite experiment is used as proof for all orders. Independently performed audits are not claimed.
