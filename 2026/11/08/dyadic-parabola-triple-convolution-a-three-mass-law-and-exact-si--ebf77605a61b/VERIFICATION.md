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

The standalone standard-library script `verify_dyadic_parabola.py` independently enumerated all \(N^3\) ordered triples for each \(N=2^k\), \(1\le k\le7\), and compared every target's count against the theorem. It additionally directly evaluated each discrete quadratic Fourier sum and its sixth moment for \(1\le k\le6\). Its final success line was `DYADIC_PARABOLA_TRIPLE_CONVOLUTION_CHECK_PASS`.

The all-exponent proof is the elementary change of variables, exact primitive lifting of \(a^2+ab+b^2\), valuation stratification and finite-group Parseval in `RESULT.md`. Exhaustive tests at small exponents alone do not verify the infinite theorem. No independent mathematical validation or historical-priority certification has been performed.
