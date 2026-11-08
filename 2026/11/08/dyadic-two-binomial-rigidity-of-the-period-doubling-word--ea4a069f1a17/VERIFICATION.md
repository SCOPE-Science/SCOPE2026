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

# Finite verification

Run `python3 verify.py` with Python 3 and no external packages. The diagnostic regenerates the binary period-doubling word by two-adic valuations, enumerates all factors at lengths \(2^k\) through \(k=11\), verifies exact moments and binomial profiles, and checks a length-five failure of global rigidity. It prints:

`VERIFY_OK levels=0..11 windows_checked=24570 pair_checks=47 five_factor_collision=confirmed`

These are finite diagnostics, not infinite proofs. The all-level proof is fully supplied in `RESULT.md`; in particular the critical steps are the complete two-rotation-orbit description, the odd-weight primitiveness and the moment-change identity. No independent scientific audit or validation has been performed.
