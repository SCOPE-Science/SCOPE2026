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

# Reproducibility and limits

Run `python3 checker.py` with Python 3 standard library. The output file `verification_output.txt` records a run on the included source: all congruence comparisons for moduli 1 through 129 passed, along with box divisibility-support checks for 100, 300, and 600. The checker uses independent direct loops rather than relying on the symbolic CRT solution for its observed congruence counts.

The infinite assertions are supported by the explicit proof: an odd-prime reduction to a square root of minus one, Hensel lifting, the CRT, a union-bound argument eliminating large common prime divisors, and the Euler-product moment test. Enumeration is finite and cannot prove either the limiting law or divergence of the mean.

Self-review of correctness, originality, and mathematical value passed; independent mathematical audit has not been performed. A stronger implicit prior result remains an originality risk.
