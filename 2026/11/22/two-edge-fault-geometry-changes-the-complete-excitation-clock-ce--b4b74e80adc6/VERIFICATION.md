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

The proof uses an exact multiplicity-invariant quotient by the universal-twin color support. `verification/signature_certificate.py` directly constructs the 189 and 567 possible finite signatures, checks every classified support coefficient against the displayed ten-cell tables, and verifies that their surjection-weighted populations simplify to the closed all-order formula. The final output marker is `SIGNATURE_CERTIFICATE_OK`.

`verification/direct_enumeration.py` builds the original neighbor-based global map for both deletion patterns independently of the signature reduction, extracts all functional-graph cycles and backwards transient depths, and checks the complete first-entry/period census on every size from five through nine. The final marker is `DIRECT_ENUMERATION_OK`.

Both programs were run successfully from the actual package paths. Small graph enumeration independently corroborates the table but by itself cannot prove all orders; the finite quotient and a direct surjection argument provide the unbounded-size step. The result does not certify individual nonzero attraction basins or general edge deletions. No independent external audit has been carried out.
