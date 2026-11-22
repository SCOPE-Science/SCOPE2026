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

The reproducible `checker.py` uses only the Python standard library. It verified exhaustive four-site classifications for the prime fields of orders 7, 11, 13 and 17. The exact counts were (14 unbalanced, 21 balanced, 0 generic), (0, 55, 275), (52, 78, 585) and (0, 136, 2244), respectively. Twenty-eight randomized complex-amplitude cases matched the analytical sixth-moment identity, threefold convolution and direct finite Fourier summation to numerical tolerance. Root isolation and additional objective bounds passed.

The general proof for all prime powers of characteristic at least seven uses Vandermonde independence, finite-field character orthogonality, exact symmetric-polynomial inequalities and a one-positive-root quartic argument. No finite test is presented as an infinite certificate. Independent audit has not been performed.
