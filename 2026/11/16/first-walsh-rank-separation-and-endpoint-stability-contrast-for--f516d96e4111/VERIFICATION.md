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

# Exact verification instructions

With Python 3 and all included CSV files in one directory, run `python3 check.py --verify .` to regenerate and compare the full certificates. Only Python's standard library is needed.

The checker independently constructs each avoidance family via direct triple testing and the maximum-insertion recursion; checks the two support sets coincide; performs a direct sum over every frequency and a separate integer Walsh–Hadamard transform; verifies Parseval, exact ranks and zero counts for orders one through five; verifies all order-five \(123\) multipliers are \(2\pmod4\) using the ten inversion marginals; verifies the explicit \(132\) zero frequency; and verifies the Fourier-support projection kernel by both a second transform and direct character summation. It computes the sharp endpoint projection norm \(3797/512\).

The exact certificates are `signed_histograms.csv`, `spectrum5.csv`, `inversion_marginals_123_n5.csv`, and `projection_kernel_132_n5.csv`. The literal success marker is `CATALAN_PATTERN_WALSH_SEPARATION_PASS`.

Checks are exhaustive only for the stated finite orders. The mathematical interpretation of unrestricted projection optimality uses translation averaging, not a finite search over projection matrices. The source comparisons are bounded, and independent mathematical validation has not been performed.
