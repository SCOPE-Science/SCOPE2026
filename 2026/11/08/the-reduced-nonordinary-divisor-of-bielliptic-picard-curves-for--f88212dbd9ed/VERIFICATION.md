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

# Reproducible verification

The accompanying `verify.py` uses only Python 3's standard library. Run `python3 verify.py` in the directory containing the script. A successful run prints `VERIFY_BIELLIPTIC_PICARD_OK 15 primes`, after separate checks for each of fifteen prime characteristics from \(7\) through \(139\).

The program recomputes \([T^K](T^2+aT+1)^N\) by its multinomial formula, independently forms the factorized expressions, and checks equality coefficientwise modulo \(p\). It reconstructs the nine plane Hasse--Witt entries from their exponent triples and verifies diagonality, and checks that \(\gcd(B_m,B_m')=1\) and \(B_m(\pm2)\ne0\). Tests operate on all polynomial coefficients (not numerical random evaluations) for each tested prime.

The infinite-prime proof is in RESULT.md. A finite test does not establish an identity for all prime characteristics or all geometric coefficients. No external formal proof or independent audit is asserted.
