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

The analytical proof is self-contained in `RESULT.md`, Steps 1–6. It uses an exact nonnegative generating-function expansion, fixed-component weak convergence, a summable factorial domination, conditional concentration, and a uniform-simplex Riemann-sum limit. No finite computation is treated as an infinite-volume certificate.

To reproduce the independently implemented finite checks, execute `python verify_critical.py` using standard Python 3. The checker compares direct partition coefficient convolution with the expansion for geometric and Bernoulli bulk measures using exact fractions, and verifies finite truncations of the proposed probability series. The verified output is `PASS: 1344 exact-rational and series assertions`.

For optional numerical convergence diagnostics, execute `python finite_diagnostics.py` with NumPy and SciPy. At the indicated five volume sizes the partition normalizer approaches the stated modified-Bessel value and the one-cluster probability approaches its limit. This check does not establish convergence for arbitrary volume or bulk.

The proof's exact scope is a positive exponential-moment bulk, fixed positive perturbation and density strictly above the bulk mean. The ranked-mass convergence is in the sup-norm topology. No dynamical mixing or claims about other critical exponents are verified.
