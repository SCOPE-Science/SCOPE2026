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

# Verification scope and reproducibility

The stated result is a mathematical weak-convergence theorem, not a numerical conjecture. Its proof rests on the exact conditional Gaussian solution, the Brownian scaling endpoint argument, Brownian maximal inequalities, the uniform frozen-drift approximation on compact microtime windows, the Gaussian quadrant identity and a dominated-convergence evaluation of an integrable arcsine kernel.

The standalone file `verify_local_sign.py` was executed with Python, NumPy and SciPy and passed 26 checks. It independently compares the tail constant from positive-series summation and quadrature, checks six rate-rescaling identities, six large-lag prefactor instances, three small-lag cusp values, three deterministic endpoint variance localizations, three independent bivariate-Gaussian sign-pair simulations, and the remaining exact identities. Its simulations only check finite identities; they do not prove any infinite-horizon assertion.

The numerical constant for unit random-stiffness strength is \(K=0.538851623662\ldots\). The arbitrary fixed parameter \(a\ge0\) and the thermal intensity \(D>0\) do not enter the sign-correlation law, although \(D\) changes the scale of the limiting positions. The convergence is first at fixed rescaled horizon, then at large rescaled lag. The order of limits must not be exchanged without new estimates.
