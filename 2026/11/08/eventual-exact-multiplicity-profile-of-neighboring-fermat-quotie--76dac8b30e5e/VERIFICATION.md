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

Run `python verify.py` with the standard Python 3 library. The run prints `VERIFY_OK prime_power_cases=10 shift_cases=3 triple_at_level_one_p11=3` after checking the complete input period of ten prime-power instances, including exponent levels equal to the certified cutoff for primes three, five, seven, eleven, and thirteen. It computes pairwise intersection targets independently via Teichmüller modular lifts; all such targets are represented at least twice. The script additionally confirms that coprime shifts preserve the fiber histogram in three examples and that there are exactly three triple fibers at the low-level prime-eleven case.

For arbitrary primes and exponents, the exact theorem is derived by the algebraic norm argument in RESULT.md. The finite computation does not independently certify historical novelty, extend the theorem below the cutoff, or replace the universal proof. No independent mathematical audit has been performed.
