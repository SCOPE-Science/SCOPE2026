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

# Reproducibility and verification

Run `python3 verify.py` with the Python standard library. The checker performs exact Fraction arithmetic for the three-by-three dispersal matrix, its sixth power, the stationary projector, local Beverton–Holt fixed-point values and derivatives, and 72 exact coefficient comparisons. It additionally iterates the positive fixed-point map in 75-digit Decimal arithmetic at \(k=4,\ldots,30\) and checks all 27 signs and the high-\(k\) relative error bound of two percent. The program prints PASS on all these checks.

The theorem's infinite conclusion does not rest on finite numerical tests: the analytic implicit-function expansion gives an \(O(4^{-k})\) remainder, while all six leading coefficients of size \(\Theta(2^{-k})\) are nonzero. The general positive-equilibrium existence statement is taken from the cited primary model and can also be proved via strict concavity, order preservation, primitivity and its positive linearization. The two-habitat impossibility proof concerns analytic recruitment and a noncritical perfect-mixing equilibrium; it is not asserted for arbitrary nonsmooth density dependence.

No external or independent scientific audit has been performed.
