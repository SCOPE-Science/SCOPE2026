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
# Verification record

Run `python3 artifacts/verify.py` using Python 3 with no third-party packages. The script directly enumerates every three-valued distance assignment over named equilateral bases of sizes one through five, checks all old/new triangle inequalities, and compares exact distance-resolved pair counts with the displayed formulas. Its successful terminal marker is `VERIFY_OK`.

The script tests finitely many parameter sizes, not all sizes. The proof of the all-size result rests on the symbolic unary classification, product counts, inclusion-exclusion and first-symbol-location partition in RESULT.md. Independent mathematical audit has not been performed.
