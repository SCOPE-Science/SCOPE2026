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

# Verification scope

Run `python3 verify.py` in the directory containing this file and `verify.py`. It builds ordinary partial maps as tuples with `-1` for undefined values, composes every pair directly, and exhaustively measures commuting idempotent pairs rather than invoking the symbolic commutation lemma.

Direct cases: regular cyclic groups of orders 1 through 7; the Klein four-group; the symmetric group of order 6; the dihedral group of order 8. Separate arithmetic checks cover cyclic orders 1 through 150. The run prints `VERIFY_OK` on success. The verifier also implements triangular recovery of element-order multiplicities and tests them against independently measured permutation orders.

The direct enumeration is finite only; it cannot prove the theorem for every group. The written proof supplies the all-group cycle calculation, zero-map correction, and leading-coefficient reconstruction. No independent audit or certification has been performed.
