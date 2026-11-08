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
The proof in `RESULT.md` is self-contained and covers all odd moduli. Its critical points are: the reversed index-to-factor parametrization; the existence of a complementary divisor allocation at each prime dividing \(m\); the parity argument making the divisor minimizer unique; and the explicit sign change of \(F_a(u+1)-F_a(u)\) for odd primes.

Run `python3 verify.py` from a directory containing this file. The program directly enumerates residues and verifies the predicted unique first pair for 2,500 odd moduli between \(3\) and \(5001\), then independently compares the prime-power expressions with exact divisor optimization over a stated finite range. There is no need for external Python packages.

The program is a finite consistency check, not a certificate for the infinite theorem. Historical priority is not independently certified. Independent mathematical audit has not been performed.
