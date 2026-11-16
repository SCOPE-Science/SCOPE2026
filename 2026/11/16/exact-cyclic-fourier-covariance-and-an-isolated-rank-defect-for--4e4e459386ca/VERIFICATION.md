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

# Computational and analytical verification

Running `python3 check.py` enumerates all allowed labeled cyclic binary strings of orders 3–17. For each order it compares the analytical Fibonacci–Lucas number of words and every exact rational two-point spin correlation against direct enumeration, and checks Fourier covariance positivity or the order-four zero mode. At orders 20, 40, 80, 150, and 250 it compares the exact finite Fourier spectrum with the stationary limiting rational symbol. The checker prints `PASS 185 assertions` when all checks succeed. The analytical proof establishes all lengths; these finite checks cannot certify an infinite claim.

The normalization uses spin values ±1, the binary-bit covariance being one-quarter as large. All cyclic windows wrap around. Nonzero Fourier modes may occur in conjugate pairs and numerical comparison does not alter their exact mathematical multiplicities.

No independent mathematical audit has been performed.
