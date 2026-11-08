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

`verify.py` is standalone Python using only the standard library. It compares the general exact stars-and-bars covariance with all six low-category formulas at every total from 0 through 500, performs separate exhaustive enumeration of small weak-composition spaces, and checks signs. On the packaged source it reports `PASS 3060 exact arithmetic and independently enumerated assertions`.

For unbounded totals, the mathematical proof uses the exact identity in `RESULT.md`, together with finite arithmetic identities for the parity-split marked-equality counts. The computational sample is not a proof for all totals, and the independent mathematical or historical validation remains unperformed.
