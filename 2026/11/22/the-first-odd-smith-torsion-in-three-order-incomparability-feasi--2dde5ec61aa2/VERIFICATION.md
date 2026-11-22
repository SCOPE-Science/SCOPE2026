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

The integer-matrix entries are reconstructed directly from the strict-coordinatewise-dominance criterion. `CERTIFICATE.json` records 25, 183, and 853 unimodular operations for parameter sizes 1, 2, and 3. `VERIFY.py` checks them one by one, verifies the final matrices including all zero off-diagonal entries, and independently checks the feasibility criterion by direct order-sign enumeration in all 4,889 positions across the three cases. It also computes ranks by exact modular Gaussian elimination over characteristics 2, 3, and 5. Execute `python3 VERIFY.py CERTIFICATE.json` from this directory; the successful terminal line is `CERTIFICATE_OK`.

Proof beyond the finite cases depends only on the Fraïssé extension property and the exact entry criterion. No Smith classification for larger named bases is claimed, and no independent mathematical audit has been performed.
