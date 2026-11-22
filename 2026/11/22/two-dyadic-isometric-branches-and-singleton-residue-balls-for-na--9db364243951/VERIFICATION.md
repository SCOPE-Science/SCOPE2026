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

With the standalone `verify.py` file in the same directory, execute `python3 verify.py`. Successful execution reports `EXHAUSTIVE_OK k=1..14`, `HIGH_PRECISION_OK 1920 matrix increment comparisons`, and `VERIFY_OK`.

The program checks exact integer matrices \(M^7\), \(M^{14}\), initial states, the two chart-value permutations at every modulus from \(2\) to \(2^{14}\), complete target coverage, least period, all singleton targets congruent to \(2\) or \(7\pmod8\), and 1,920 high-precision increments at eighty dyadic step scales. It uses Python standard-library exact integer arithmetic and no third-party input.

Finite exhaustive checking up to \(2^{14}\) and selected checks at larger exponents cannot by themselves establish the theorem at all prime powers. Universal validity is proved by the exact matrix identity, the parity of two scalar forms, and a quantified lifting argument in RESULT.md. The full singleton spectrum outside the stated congruence balls is unproved. No independent audit has been performed.
