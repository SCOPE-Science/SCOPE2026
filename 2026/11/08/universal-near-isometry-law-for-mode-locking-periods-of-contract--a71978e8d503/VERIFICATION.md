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

# Reproducibility and proof boundary

The included `verify.py` uses only the Python standard library. Execute `python verify.py` from the directory containing that file. During this review it printed `PASS: 628 exact-rational and numerical supporting checks`, `limiting mean=1.461525938803, limiting second moment=3.947841760436`.

The checker compares the published plateau endpoint difference with the claimed closed width for three exact rational contraction parameters and every coprime numerator through denominator 18; it checks that those intervals lie in the parameter domain; it checks exact rational truncated mass sums with controlled finite remainders; and it verifies moment convergence numerically for four contraction parameters. This is reproducibility support, not an exhaustive check over all \(\lambda\), all denominators, or all test functions.

The proof's noncomputational dependencies are identified: Laurent--Nogueira Theorems 3 and 4 (exact plateau formula and exceptional-parameter nullity), the elementary divisor identity and Möbius inversion, the summatory totient bound, Abel summation, and the convergence of exponentially dominated moments. There is no finite numerical certificate purporting to establish the asymptotic theorem.
