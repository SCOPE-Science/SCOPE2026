---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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
Run `python3 checker.py` with `certificate.json` in the working directory. Requires Python 3 and SymPy. The checker constructs the exact cyclotomic polynomials and signed shifts, evaluates all 28 integer resultants, and verifies the supplied complete prime factorizations by full multiplication and trial division. It tests every common root modulo a listed prime and every possible lift modulo its square. The resultant identity excludes all other primes and the modular checks cover all integer arguments. There are 178 common roots and no simultaneous prime-square lifts below index 29.

The checker evaluates both index-29 witness values as exact integers and computes their entire gcd, verifying `G_29(298)=3481=59^2` and the primality of 59. Verifying only divisibility by 3481 would show nonsquarefreeness, not squarefullness of the gcd.
