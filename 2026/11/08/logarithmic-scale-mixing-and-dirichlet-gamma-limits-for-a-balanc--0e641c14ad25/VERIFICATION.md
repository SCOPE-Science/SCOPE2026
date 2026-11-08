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

# Reproducibility and mathematical scope

Run `python check.py` with Python 3, NumPy and SciPy. The checker operates on finite sums and prints the normalized one-decade increments for three small values of \(k\), then `PASSED 100 checks`.

The exact identity used is the sum of negative-binomial weights over the opposite part: for fixed \(M=m\), \(\sum_{n\ge0}c_k(n)e^{-\beta(\mu+Jm)n}=[1-e^{-\beta(\mu+Jm)}]^{-k}\). Its implementation is also compared with independently enumerated truncated two-dimensional sums, and with the exactly factorized zero-interaction case. The displayed high-temperature increments check the predicted coefficient to increasing accuracy rather than establishing any limiting assertion.

Analytical verification: a three-range estimate of the exact one-part series gives the coefficient of the logarithm; restricting the total occupation to the interior power window and tilting the interaction coupling gives the joint Laplace transform \((b-a)(1+t)^{-k}\); uniform weak compositions yield independent Dirichlet fractions; rescaling inverse temperature in the partition ratio gives gamma total energy and its moments. The argument applies to all fixed integers \(k\ge1\) and all fixed positive \(\mu,J\), not merely to the finite numerical cases.

No independent external audit or formal certification was performed. No statement is made about a thermodynamic limit in graph size or a physical phase transition.
