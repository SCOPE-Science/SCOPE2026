---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify_frobenius.py` with SymPy. The script verifies the Cartier coefficient matrix, rank-one decompositions, the polynomial identity for the correctly ordered product \(M^{(11)}M\), and the root and isomorphism-orbit calculations over the prime field. The polynomial identities and gcds apply over the algebraic closure. `verify_coefficients.py` is unchanged and verifies only coefficient extraction, not stable rank. The geometric isomorphism and automorphism theorems are attributed to the published source; the script checks their application to this locus.
