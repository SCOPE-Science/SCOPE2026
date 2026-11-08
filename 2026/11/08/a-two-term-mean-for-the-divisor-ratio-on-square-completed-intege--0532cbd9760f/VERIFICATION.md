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

# Reproducibility

Use Python 3 standard library and run `python verify.py`. The exact tests establish:

1. The algebraic prime-local generating identity through degree \(40\), using `fractions.Fraction`.
2. Equality of the product of prime-power ratios \(\prod_{p^a\parallel m}(2a+1)/2\) and the independently evaluated \(\tau(m^2)/2^{\omega(m^2)}\) for every integer \(1\le m\le360\).
3. Equality of a direct square-completion sum and the weighted complete-block decomposition, including the incomplete final block, at every integer cutoff \(1\le X\le15000\).
4. Non-rigorous finite-prime diagnostics for \(H(1)\), \(H'(1)/H(1)\), and the asymptotic constants. These diagnostics are approximate floating-point calculations, not interval certificates.

The infinite asymptotic requires the analytic Euler product and Selberg--Delange. Neither an exact finite computation nor a truncated prime product proves the stated error term. Independent mathematical audit has not been performed.
