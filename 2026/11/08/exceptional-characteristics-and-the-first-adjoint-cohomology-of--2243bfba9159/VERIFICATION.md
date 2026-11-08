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

Run `python verify.py` with Python 3 and SymPy to regenerate all integer identities and Smith invariant factors for the complete table in RESULT.md. The checker independently computes modular ranks at primes 2,3,5,7,11,13,17 and verifies an explicit nonnilpotent characteristic-eleven derivation on all 512 ordered basis pairs/output coordinates. The integer Smith invariant factors, not extrapolation from prime samples, prove the ranks for every field. `verification_output.txt` is the actual captured standard output of this successful run. No independent mathematical audit has been performed.
