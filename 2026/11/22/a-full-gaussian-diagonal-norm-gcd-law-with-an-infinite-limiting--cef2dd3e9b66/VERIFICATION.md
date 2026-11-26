---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

# Reproducibility and limits

Run `python3 checker.py` with Python 3 standard library. The output file `verification_output.txt` records a run on the included source: all congruence comparisons for moduli 1 through 129 passed, along with box divisibility-support checks for 100, 300, and 600. The checker uses independent direct loops rather than relying on the symbolic CRT solution for its observed congruence counts.

The infinite assertions are supported by the explicit proof: an odd-prime reduction to a square root of minus one, Hensel lifting, the CRT, a union-bound argument eliminating large common prime divisors, and the Euler-product moment test. Enumeration is finite and cannot prove either the limiting law or divergence of the mean. The displayed eight-place coprimality probability, 0.44742061, uses a separate prime sieve through \(10^8\) and the explicit product-tail bound in `RESULT.md`; it is not an empirical box frequency from `checker.py`.

The checks here are computational supplements, not formal verification or a literature priority certificate.
