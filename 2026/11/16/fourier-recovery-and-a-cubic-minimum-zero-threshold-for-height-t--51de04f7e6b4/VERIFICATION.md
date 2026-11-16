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

Execute `python3 code/height3_verify.py` with standard Python 3. The checker independently enumerates every height-three Dyck excursion up to semilength eight, checks the affine map in both directions, calculates all integer Walsh coefficients by fast Walsh-Hadamard transformation, checks each against an independently implemented signed height-state dynamic program, and against an independent Fibonacci-path signing recurrence. It confirms integer Parseval sums, exact spectral nullities, the minimum nonzero multiplier magnitude, and minimum Hamming weight of zero frequencies. For semilength eight it verifies exactly ten degree-three zero characters and no lower-degree zero. It also tests the simple sign recurrence at semilengths up to 150; the analytic proof, not those tests, establishes the infinite quantifier.

Expected final marker: `HEIGHT3_DYCK_FIBONACCI_WALSH_PASS`.

Limits: finite enumeration does not prove the all-order claim; it is independently proven in `RESULT.md`. No independent audit was performed.
