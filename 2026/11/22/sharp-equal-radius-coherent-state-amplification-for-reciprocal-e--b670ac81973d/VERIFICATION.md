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

# Verification of the stated finding

The exact kernel formula is \(K_m(z,w)=(m/\pi)\sum_{n\ge0}(z\overline w)^n/\Gamma((n+1)/m)\) with the weight \(e^{-|z|^{2m}}\). Evaluation on two normalized kernels yields the explicit formula in the proof. The full Mittag–Leffler sector expansion with its algebraic remainder gives an exponentially small error after division by the dominant positive-axis kernel, which is needed when \(d<m\). The published sector bound forces every maximizing angular gap to zero; a quadratic optimization yields the constant \(d^2|a_d|^2/(2m^2)\) and gap constant \(d|a_d|/m^2\).

The independent exact Gaussian check uses \(K_1(z,w)=\pi^{-1}e^{z\overline w}\); maximizing \(2|a|Rs-2R^2s^2\) on \([0,1]\) gives \(|a|^2/2\) for \(R\ge|a|/2\). The standard-library-only file `verify.py` was executed against the submitted source files and printed `FINITE_CHECKS_OK 44`. The computation only samples finite radii and a finite set of exponents, and does not prove uniform error estimates, global maximality at general parameters, or literature priority.

The mathematical result has received a self-review only. The independent audit has not been performed.
