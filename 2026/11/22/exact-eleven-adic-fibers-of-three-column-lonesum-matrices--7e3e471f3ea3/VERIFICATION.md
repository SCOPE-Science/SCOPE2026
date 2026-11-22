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

The proof in `RESULT.md` establishes the all-depth statement analytically. Independently, run `python3 check_lonesum_11.py` using the Python standard library; it requires no network access or external data files. The exact integer checker verifies the arithmetic expression against the first recorded values, computes all ten branch slopes and the exceptional binomial coefficients, recovers the critical center and quadratic unit to required precision through a finite eleven-adic logarithm calculation, enumerates all output fibers for moduli \(11^k\) with \(1\le k\le5\), and rejects proper period divisors for \(k\le4\).

Observed image sizes were \(7\), \(77\), \(847\), \(9317\), \(102487\) at those levels. The checker does not establish infinitely many congruences, does not constitute an independent audit and does not make claims about other primes or matrix widths. The derivative/Hensel-normal-form arguments in the proof are necessary for infinite correctness.
