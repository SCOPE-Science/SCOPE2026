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

The exact proof covers all even indices \(n\ge2\) and all primes by four disjoint cases (\(2\), prime divisors of \(B\), prime divisors of \(AD\), and remaining primes). The analytic prime-infinitude step is conditional on Dickson's conjecture and is not a computational check.

Run `python3 verify_local_admissibility.py` in the same directory as `RESULT.md`. It uses only the Python standard library and tests all \(17\) indices \(2,4,\dots,34\) and all \(37\) primes below \(160\), evaluating every parameter residue modulo each such prime. It checks the predicted local counts, the exact \(n=2\) three-prime example, and all Korselt divisibilities for that example. Expected output:

`LOCAL_ADMISSIBILITY_EXACT_OK indices=17 primes=37 prime_example=3`

The primality verification of the example uses exhaustive trial division up to each integer square root; it does not certify primes for unbounded parameters. There is no independent external audit or unconditional proof of Dickson's conjecture.
